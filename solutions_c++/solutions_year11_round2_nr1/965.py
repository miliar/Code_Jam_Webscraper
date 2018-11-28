#include <iostream>
#include <fstream>
#include <string>
using namespace std;

const int MAXN = 105;

ofstream fout("a.out");
string grid[MAXN];
int T, N;
int win[MAXN], tot[MAXN];
double wp[MAXN], owp[MAXN], oowp[MAXN];

int main() {
	cin >> T;
	string input;
	for (int t = 1; t <= T; t++) {
		cin >> N;
		memset(win, 0, sizeof(win));
		memset(tot, 0, sizeof(tot));
		memset(wp, 0, sizeof(wp));
		memset(owp, 0, sizeof(owp));
		memset(oowp, 0, sizeof(oowp));

		for (int i = 0; i < N; i++) {
			cin >> grid[i];
			for (int j = 0; j < N; j++) {
				if (grid[i][j] != '.')
					tot[i]++;
				if (grid[i][j] == '1')
					win[i]++;
			}

			wp[i] = (double)win[i] / tot[i];
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (grid[i][j] == '.') continue;
				if (grid[i][j] == '0') owp[i] += (double)(win[j] - 1) / (tot[j] - 1);
				else owp[i] += (double)win[j] / (tot[j] - 1);
			}
			
			owp[i] /= tot[i];
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (grid[i][j] == '.') continue;
				oowp[i] += owp[j];
			}
			oowp[i] /= tot[i];
		}

		fout << "Case #" << t << ":\n";
		for (int i = 0; i < N; i++) {
			fout << 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] << "\n";
		}
	}
}