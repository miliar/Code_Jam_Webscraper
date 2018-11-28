#include <iostream>

using namespace std;

char team[100][100];
double WP[100];
int played[100];

double owp(int i,int N) {
	double OWP = 0;
	int count = 0;
	for(int j = 0; j < N;++j) {
		if(team[i][j] != '.') {
			OWP += (WP[j] * played[j] - (team[j][i] == '1'?1:0)) / double(played[j] - 1);
			++ count;
		}
	}
	if(count)
		return OWP / double(count);
	else
		return 0;
}

int main()
{
	int T;
	cin >> T;
	double RPI;
	cout.precision(12);
	for(int testCase=1; testCase <= T; ++testCase) {
		int N; // number of teams
		cin >> N;
		for(int i = 0; i < N; ++i) {
			int wins = 0, loses = 0;
			played[i] = 0;
			for (int j = 0; j < N; ++j) {
				char ch;
				cin >> ch;
				team[i][j] = ch;
				if(ch == '1') {
					++wins;
				}
				else if (ch == '0') {
					++loses;
				}
			}
			played[i] = loses + wins;
			WP[i] = wins / double(played[i]);
//			cout << "\n****WP:" << WP[i] << endl;
		}

		cout << "Case #" << testCase << ":" << endl;
		for(int i = 0; i < N; ++i) {
			RPI = 0.25 * WP[i];
			double OOWP = 0;
//			cout << "\n*****OWP"<< i <<":" << owp(i, N);
			RPI += 0.50 * owp(i, N);
			int count = 0;
			OOWP = 0;
			for(int j = 0; j < N;++j) {
				if(team[i][j] != '.') { // oponent
					OOWP += owp(j, N);
					count++;
				}
			}
			if(count)
				OOWP = OOWP / double(count);
			else
				OOWP = 0;

//			cout << "\n******OOWP" << i << ":" <<  OOWP << endl;
			RPI += 0.25 * OOWP;
			cout << RPI << endl;
		}
	}
	return 0;
}
