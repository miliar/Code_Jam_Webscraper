#include <iostream>
#include <string>
#include <queue>
#include <algorithm>
#include <sstream>
#include <vector>

using namespace std;

int tab[101][101]; // 0 = loss, 1 = win, 2 = not played
double WP[101];
double WPx[101][101];	// winning percentage excluding j
double OWP[101];

int main() {
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int N; cin >> N;
		memset(tab,0,sizeof(tab));
		memset(WP,0,sizeof(WP));
		memset(WPx,0,sizeof(WPx));
		memset(OWP,0,sizeof(OWP));
		for (int i = 0; i < N; i++) {
			int numWin = 0; int numTot = 0;
			for (int j = 0; j < N; j++) {
				char ch; cin >> ch;
				if (ch == '.') {
					tab[i][j] = 2;
					continue;
				}
				tab[i][j] = ch - '0';
				if (tab[i][j]) numWin++;
				numTot++;
			}
			WP[i] = ((double)numWin)/numTot;
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				// win excluding j
				int numWin = 0; int numTot = 0;
				for (int k = 0; k < N; k++) {
					if (k == j) continue;
					if (tab[i][k] == 2) continue;
					if (tab[i][k]) numWin++;
					numTot++;
				}
				WPx[i][j] = ((double)numWin)/numTot;
			}
		}
		// calculate owp
		for (int i = 0; i < N; i++) {
			double owp = 0;
			int totOpp = 0;
			for (int j = 0; j < N; j++) {
				if (tab[i][j] != 2) {
					totOpp++;
					owp += WPx[j][i];
				}
			}
			OWP[i] = owp / totOpp;
		}
		// calculate finals
		cout << "Case #" << (t+1) << ":\n";
		for (int i = 0; i < N; i++) {
			double oowp = 0;
			int totOpp = 0;
			for (int j = 0; j < N; j++) {
				if (tab[i][j] != 2) {
					totOpp++;
					oowp += OWP[j];
				}
			}
			oowp /= totOpp;
			double rpi = WP[i] * 0.25 + OWP[i] * 0.5 + 0.25 * oowp;
			cout << rpi << "\n";
		}
	}
	return 0;
}