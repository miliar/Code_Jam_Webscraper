#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

#define for0(i,n) for(int i = 0; i < (n); i ++)

int n;

int games[105][105];

int numGames[105];
int numWins[105];

double wp[105];
double owp[105];
double oowp[105];

int main() {
	
	int kases; cin >> kases;
	
	for0(kase, kases) {
		cin >> n;
		
		string xs;
		
		for0(i, n) {
			cin >> xs;
			for0(j, n) {
				games[i][j] = xs[j] == '.' ? -1 : 
						(xs[j] == '1' ? 1 : 0);
			}
		}
		
		for0(i, n) {
			numWins[i] = numGames[i] = 0;
			for0(j, n) {
				if (games[i][j] != -1) numGames[i] ++;
				if (games[i][j] == 1) numWins[i] ++;
			}
			if (numGames[i] == 1) {
				cout << "derp"; return -1;
			}
			wp[i] = ((double)numWins[i]) / ((double)numGames[i]);
		}
		
		for0(i, n) {
			owp[i] = 0;
			for0(j, n) {
				if (games[i][j] == 0)
					owp[i] += ((double)numWins[j]-1) / (numGames[j] - 1.0);
				else if (games[i][j] == 1)
					owp[i] += ((double)numWins[j]) / (numGames[j] - 1.0);
			}
			owp[i] /= numGames[i];
		}
		
		for0(i, n) {
			oowp[i] = 0;
			for0(j, n) {
				if (games[i][j] != -1) oowp[i] += owp[j];
			}
			oowp[i] /= numGames[i];
		}
		
		cout << "Case #" << (kase+1) << ":" << endl;
		for0(i, n) {
			cout << (0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]) << endl;
		}
	}
}