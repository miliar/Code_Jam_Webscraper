#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>
#include <stdint.h>
#include <list>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
using namespace std;

struct Team_data {
	double WP;
	double OWP;
	double OOWP;
	int total;
	int wins;
};

void handleCase(int T)
{
	int N;
	cin >> N;
	vector<string> data(N);
	vector<Team_data> team_data(N);
	for (int i = 0; i < N; i++) {
		cin >> data[i];
		int total = 0, wins = 0;
		for (int j = 0; j < N; j++) {
			if (data[i][j] == '1') {
				total++;
				wins++;
			} else if (data[i][j] == '0') {
				total++;
			}
		}
		team_data[i].WP = (double)wins / (double)total;
		team_data[i].total = total;
		team_data[i].wins = wins;
	}
	for (int i = 0; i < N; i++) {
		int total = 0, wins = 0;
		double OWP = 0.0;
		for (int j = 0; j < N; j++) {
			if (data[i][j] == '1') {
				total = team_data[j].total - 1;
				wins = team_data[j].wins;
				OWP += (double)wins / (double)total; 
			} else if (data[i][j] == '0') {
				total = team_data[j].total - 1;
				wins = team_data[j].wins - 1;
				OWP += (double)wins / (double)total;
			}
		}
		team_data[i].OWP = OWP/(double)team_data[i].total;
		
	}
	for (int i = 0; i < N; i++) {
		int total = 0, wins = 0;
		double OOWP = 0.0;
		for (int j = 0; j < N; j++) {
			if (data[i][j] == '1') {
				OOWP += team_data[j].OWP; 
			} else if (data[i][j] == '0') {
				OOWP += team_data[j].OWP;
			}
		}
		team_data[i].OOWP = OOWP/(double)team_data[i].total;
	}
	cout << "Case #" << T + 1 << ":" << endl;
	cout.precision(12);
	for (int i = 0; i < N; i++) {
		cout << (0.25 * team_data[i].WP + 0.5 * team_data[i].OWP + 0.25 * team_data[i].OOWP) << endl;
	}
}

int main(int argc, char *argv[])
{
	int N;

	cin >> N;

	for (int i = 0; i < N; i++) {
		handleCase(i);
	}
	return 0;
}
