#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Team {
	vector<Team *> opponents;
	int wins, losses;
	string info;
	int team;
};

double getWP(Team *team, Team *bad = 0) {
	int wins = team->wins;
	int losses = team->losses;
	if (bad) {
		char out = team->info[bad->team];
		if (out == '1') {
			wins--;
		} else if (out == '0') {
			losses--;
		}
	}

	return wins / (double)(losses + wins);
}

double getOWP(Team *team) {
	double average = 0;
	for (int i = 0; i < team->opponents.size(); ++i) {
		average += getWP(team->opponents[i], team);
	}
	average = average / (double)(team->opponents.size());
	return average;
}

double getOOWP(Team *team) {
	double average = 0;
	for (int i = 0; i < team->opponents.size(); ++i) {
		average += getOWP(team->opponents[i]);
	}
	average /= (double)team->opponents.size();
	return average;
}

double getRPI(Team *team) {
	double rpi = getWP(team)/4 + getOWP(team)/2 + getOOWP(team)/4;
	return rpi;
}

int main() {
	int cases = 0;
	cin >> cases;

	for (int z = 0; z < cases; ++z) {
		int numTeams = 0;
		cin >> numTeams;
		vector<Team *> teams;
		for (int i = 0; i < numTeams; ++i) {
			string info;
			cin >> info;
			Team *team = new Team;
			team->info = info;
			team->wins = 0;
			team->losses = 0;
			team->team = i;
			teams.push_back(team);
		}
		for (int i = 0; i < numTeams; ++i) {
			for (int x = 0; x < numTeams; ++x) {
				char out = teams[i]->info[x];
				if (out == '1') {
					teams[i]->wins += 1;
					teams[i]->opponents.push_back(teams[x]);
				} else if (out == '0') {
					teams[i]->losses += 1;
					teams[i]->opponents.push_back(teams[x]);
				}
			}

		}
		cout << "Case #" << z+1 <<": " << endl;
		for (int i = 0; i < numTeams; ++i) {
			cout << getRPI(teams[i]) << endl;
		}
	}
}