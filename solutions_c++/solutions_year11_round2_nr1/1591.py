// Test.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>

using namespace std;

double calcWP (const vector<char>& mat, int excTeam)
{
	int numGames(0), wonGames(0);
	for (int i = mat.size()-1; i >= 0; i--) {
		if (excTeam == i)
			continue;
		if (mat[i] == '1') {
			++wonGames;
			++numGames;
		}
		else if (mat[i] == '0')
			++numGames;
	}
	return (double)wonGames / (double)numGames;
}

int main()
{
	int numCases = 0;
	cin >> numCases;

	for (int i = 0; i < numCases; ++i) 
	{
		int numTeams = 0;
		cin >> numTeams;

		vector<vector<char> > mat;
		mat.resize(numTeams);
		for (int m = 0; m < numTeams; ++m) {
			mat[m].resize(numTeams);
			for (int n = 0; n < numTeams; ++n) {
				char c = '.';
				cin >> mat[m][n];
			}
		}

		cout << "Case #" << i+1 << ": " << endl;

		vector<double> wp, owp;
		for (int j = 0; j < numTeams; j++) {
			wp.push_back(calcWP(mat[j], -1));
			int numGames(0);
			double sum(0.0);
			for (int k = 0; k < numTeams; k++) {
				if (mat[j][k] != '.') {
					sum += calcWP(mat[k], j);
					++numGames;
				}
			}
			owp.push_back(sum / (double) numGames);
		}

		for (int j = 0; j < numTeams; j++) {
			double RPI = 0.25 * wp[j] + 0.50 * owp[j];
			int numGames(0);
			double sum(0.0);
			for (int k = 0; k < numTeams; k++) {
				if (mat[j][k] != '.') {
					sum += owp[k];
					++numGames;
				}
			}
			RPI += 0.25 * sum / (double) numGames;

			cout << RPI << endl;
		}
	}

	return 0;
}

