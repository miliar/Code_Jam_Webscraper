#include <iostream>
#include <vector>
#include <string>


using namespace std;


//
// Main Function
//

int main()
{
	// Obtain the number of test cases
	int T;
	cin >> T;
	
	// Handle each test case
	for (int k = 0; k < T; k++) {
		
		// Obtain the number of teams
		int N;
		cin >> N;
	
		vector< vector<int> > sched;
		sched.resize(N);
		for (int i = 0; i < N; i++)
			sched[i].resize(N);
			
		vector<int> wins;
		wins.resize(N);
		
		vector<int> games;
		games.resize(N);
		
		vector<double> WP;
		WP.resize(N);
		
		vector<double> OWP;
		OWP.resize(N);
		
		vector<double> OOWP;
		OOWP.resize(N);

		vector<double> RPI;
		RPI.resize(N);
		
		// Process each team's schedule
		for (int i = 0; i < N; i++) {
			string s;
			cin >> s;
			
			// Check each game's result
			wins[i]  = 0;
			games[i] = 0;
			for (int j = 0; j < N; j++) {
				switch (s[j]) {
					case '1':
						sched[i][j] = 1;
						(wins[i])++;
						(games[i])++;
						break;
					case '0':
						sched[i][j] = 0;
						(games[i])++;
						break;
					default:
						sched[i][j] = -1;
						break;
				}
			}
			
			// Determine the team's win percentage
			WP[i] = (double) wins[i] / (double) games[i];
			
		}
		
		// Compute each team's OWP
		for (int i = 0; i < N; i++) {
			double sumWP = 0;
			double count = 0;
			for (int j = 0; j < N; j++) {
				if ((i == j) || (sched[j][i] < 0))
					continue;
				int oppWins  = wins[j];
				int oppGames = games[j] - 1;
				if (sched[j][i] > 0)
					oppWins--;
				sumWP += (double) oppWins / (double) oppGames;
				count++;
			}
			OWP[i]= sumWP / count;
		}
		
		// Compute each team's OOWP
		for (int i = 0; i < N; i++) {
			double sumOWP = 0;
			double count  = 0;
			for (int j = 0; j < N; j++) {
				if ((i == j) || (sched[j][i] < 0))
					continue;
				sumOWP += OWP[j];
				count++;
			}
			OOWP[i] = sumOWP / count;
		}
		
		// Compute each team's RPI
		cout << "Case #" << k + 1 << ":" << endl;
		for (int i = 0; i < N; i++) {
			double RPI = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
			cout << RPI << endl;
		}
	}
	
	return 0;
}
