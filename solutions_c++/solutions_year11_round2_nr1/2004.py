#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Compute and return fraction of games won, after first throwing out the games they played against team 'throw_away'
// (if throw_away is -1, return total percent of games won)
double average(string schedule, int throw_out = -1)
{
	int won_games = 0;
	int total_games = 0;
	for(unsigned i=0; i<schedule.length(); i++)
	{
		if(i == throw_out) continue;
		if(schedule[i] == '1')
			won_games++;
		if(schedule[i] != '.')
			total_games++;
	}

	if(total_games == 0)
	{
		return -1;
	}
	else
	{
		return (double)won_games/(double)total_games;
	}
}

double calculate_OWP(vector<string> &schedules, int team)
{
	int opponents = 0;
	double opponents_WP = 0; // sum of opponents WP
	for(unsigned n2=0; n2<schedules.size(); n2++)
	{
		if(n2 == team) continue;
		if(schedules[n2][team] == '.') continue;
		double opponent_WP = average(schedules[n2], team);
		if(opponent_WP >= 0)
		{
			opponents++;
			opponents_WP += opponent_WP;
		}
	}

	// opponents should not be zero, as 'Every team plays at least two other teams'
	return opponents_WP / opponents;
}

int main(int argc, char* argv[])
{
	int T; // bumber of test cases;
	cin >> T;

	for(int t=1; t<=T; t++)
	{
		cout << "Case #" << t << ":" << endl;
		
		int N; // number of teams;
		cin >> N;

		// Read team schedules
		vector<string> schedules(N);
		for(int n=0; n<N; n++)
		{
			cin >> schedules[n];
		}

		// Calculate and dislay RPI of each team
		for(int n=0; n<N; n++)
		{
			double WP = average(schedules[n]);
			double OWP = calculate_OWP(schedules, n);

			int opponents = 0; // number of opponents of team
			double OOWPsum = 0;
			for(int n2=0; n2<N; n2++)
			{
				if(n2 == n) continue;
				if(schedules[n][n2] == '.') continue;

				opponents++;
				// Note OWP of each team will be calculated several times, but I have a fast computer :)
				OOWPsum += calculate_OWP(schedules, n2);
			}
			double OOWP = OOWPsum / opponents;
			//cout << "WP=" << WP << " OWP=" << OWP << " OOWP=" << OOWP<< endl;

			double RPI = 0.25 * WP + 0.5 * OWP + 0.25 * OOWP;
			cout.precision(12);
			cout << RPI << endl;
		}
	}

	return 0;
}

