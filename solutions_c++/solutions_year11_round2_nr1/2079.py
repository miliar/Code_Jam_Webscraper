#include <iostream>
#include <string>
#include <sstream>

#define WIN 1
#define LOSE 0
#define NEVER_PLAYED -1
#define NONE -10

using namespace std;

ifstream in("D:/JAM/input");
ofstream out("D:/JAM/out.txt");


double calculate_wp(int team, int ignore, vector<vector<int>>& grid)
{
	double w = 0;
	double n = 0;

	for (int i = 0; i < grid.size(); i++)
	{
		if (grid[team][i] == WIN && i != ignore) w++;
		if (grid[team][i] != NEVER_PLAYED && i != ignore) n++;
	}

	return w / n;
}








double calculate_owp(int team, vector<vector<int>>& grid)
{
	double owp = 0;
	int n = 0;
	for (int i = 0; i < grid.size(); i++)
	{
		if (grid[team][i] != NEVER_PLAYED) 
		{
			owp += calculate_wp(i, team, grid);
			n++;
		}
	}
	return owp / n;
}

double calculate_oowp(int team, vector<vector<int>>& grid)
{
	double oowp = 0;
	int n = 0;
	for (int i = 0; i < grid.size(); i++)
	{
		if (grid[team][i] != NEVER_PLAYED)
		{
			n++;
			oowp += calculate_owp(i, grid);
		}
	}
	return oowp / n;
}

double solve_team(int team, vector<vector<int>>& grid)
{
	double wp = calculate_wp(team, NONE, grid);
	double owp = calculate_owp(team, grid);
	double oowp = calculate_oowp(team, grid);
	return 0.25 * wp + 0.5 * owp + 0.25 * oowp;
}

vector<double> solve_case(vector<vector<int>> grid) 
{
	vector<double> n;

	for (int i = 0; i < grid.size(); i++)
	{
		n.push_back(solve_team(i, grid));
	}

	return n;
}

int main() 
{
	int n_cases;
	in >> n_cases;
	
	for (int i = 1; i <= n_cases; i++) {
		int n_teams;
		in >> n_teams;
		vector<vector<int>> grid;
		string str;
		getline(in, str);

		for (int i = 0; i < n_teams; i++) {
			vector<int> row;
			string str;
			getline(in, str);
			for (int j = 0; j < n_teams; j++) {
				if (str[j] == '.') row.push_back(NEVER_PLAYED);
				else if (str[j] == '1') row.push_back(WIN);
				else row.push_back(LOSE);
			}
			grid.push_back(row);
		}

		out << "Case #" << i << ":" << endl;
		vector<double> result = solve_case(grid);
		for (int i = 0; i < result.size(); i++) {
			out << result[i] << endl;
		}
	}
}



