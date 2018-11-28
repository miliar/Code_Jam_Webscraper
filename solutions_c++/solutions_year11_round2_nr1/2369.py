#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <vector>

using std::cout;
using std::endl;
using std::pair;
using std::string;
using std::vector;

typedef pair<int, int> Frac;
typedef vector<vector<int> > Schedule;

vector<Schedule> ParseInput(const string& filename) {
	vector<Schedule> schedules;

	std::ifstream fin;
	fin.open(filename.c_str(), std::ifstream::in);
	if (fin.fail()) {
		cout << "Failed to open " << filename << endl;
		return schedules;
	}

	int num_schedules;
	fin >> num_schedules;
	for (int i = 0; i < num_schedules; ++i) {
		int num_teams;
		fin >> num_teams;
		Schedule schedule(num_teams, vector<int>(num_teams, 0));
		for (int r = 0; r < num_teams; ++r) {
			for (int c = 0; c < num_teams; ++c) {
				char token;
				fin >> token;
				switch (token) {
					case '1':
						schedule[r][c] = 1;
						break;
					case '0':
						schedule[r][c] = 0;
						break;
					case '.':
						schedule[r][c] = -1;
						break;
				}
			}
		}
		schedules.push_back(schedule);
	}

	fin.close();

	return schedules;
}

int GCD(int a, int b) {
	int aa = a;
	int bb = b;
	while (bb != 0) {
		int tmp = bb;
		bb = aa % bb;
		aa = tmp;
	}
	return aa;
}

int LCM(int a, int b) {
	return a * b / GCD(a, b);
}

Frac FracAdd(const Frac& a, const Frac& b) {
	int lcm = LCM(a.second, b.second);
	Frac res(0,1);
	res.second = lcm;
	res.first = a.first * (lcm / a.second) + b.first * (lcm / b.second);
	return res;
}

vector<double> ComputeRPI(const Schedule& schedule) {
	int num_teams = schedule.size();
	vector<double> rpi(num_teams, 0.0);

	// compute Winning Percentage
	vector<Frac> WP(num_teams, Frac(0,1));
	for (int i = 0; i < num_teams; ++i) {
		int games_played = 0;
		int games_won = 0;
		for (int j = 0; j < num_teams; ++j) {
			if (schedule[i][j] == -1)
				continue;
			games_played++;
			if (schedule[i][j] == 1)
				games_won++;
		}
		WP[i].first = games_won;
		WP[i].second = games_played;
		//cout << "Team " << i+1 << "'s WP = " << WP[i].first << "/" << WP[i].second << endl;
	}

	// compute Opponents' Winning Percentage
	vector<Frac> OWP(num_teams, Frac(0,1));
	vector<int> teams_played(num_teams, 0);
	for (int i = 0; i < num_teams; ++i) {
		int cur_team = i;
		for (int j = 0; j < num_teams; ++j) {
			if (schedule[i][j] == -1 || j == cur_team)
				continue;
			teams_played[i]++;
			int games_played = 0;
			int games_won = 0;
			for (int k = 0; k < num_teams; ++k) {
				if (schedule[j][k] == -1 || k == cur_team)
					continue;
				games_played++;
				if (schedule[j][k] == 1)
					games_won++;
			}
			OWP[i] = FracAdd(OWP[i], Frac(games_won, games_played));
		}
		// take the average
		OWP[i].second *= teams_played[i];
		//cout << "Team " << i+1 << "'s OWP = " << OWP[i].first << "/" << OWP[i].second << endl;
	}

	// compute Opponents' Opponents' Winning Percentage
	vector<Frac> OOWP(num_teams, Frac(0,1));
	for (int i = 0; i < num_teams; ++i) {
		int cur_team = i;
		for (int j = 0; j < num_teams; ++j) {
			if (schedule[i][j] == -1 || j == cur_team)
				continue;
			OOWP[i] = FracAdd(OOWP[i], OWP[j]);
		}
		OOWP[i].second *= teams_played[i];
		//cout << "Team " << i+1 << "'s OOWP = " << OOWP[i].first << "/" << OOWP[i].second << endl;
	}

	for (int i = 0; i < num_teams; ++i) {
		WP[i].second *= 4;
		OWP[i].second *= 2;
		OOWP[i].second *= 4;
		Frac sum = FracAdd(WP[i], OWP[i]);
		sum = FracAdd(sum, OOWP[i]);
		rpi[i] = static_cast<double>(sum.first) / sum.second;
	}

	return rpi;
}

int main(int argc, char** argv) {
	vector<Schedule> schedules = ParseInput(string(argv[1]));

	std::ofstream fout;
	fout.open("output.txt", std::ofstream::out);
	if (fout.fail()) {
		cout << "Failed to open output.txt for writing." << endl;
		return 1;
	}

	int num_schedules = schedules.size();
	for (int i = 0; i < num_schedules; ++i) {
		Schedule schedule = schedules[i];
		int num_teams = schedule.size();
		vector<double> rpi = ComputeRPI(schedule);
		fout << "Case #" << i+1 << ":" << endl;
		for (int j = 0; j < num_teams; ++j)
			fout << std::setprecision(12) << rpi[j] << endl;
	}

	fout.close();

	return 0;
}