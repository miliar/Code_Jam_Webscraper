#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <cstdio>
using namespace std;

double rpi(double wp, double owp, double oowp) {
	return 0.25 * wp + 0.50 * owp + 0.25 * oowp;
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("output.out","w",stdout);
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		int n;
		cin >> n;
		vector<string> teams(n);
		vector<int> wins(n, 0);
		vector<vector<double> > WP(n, vector<double>(n, -1.0));
		vector<double> OWP(n);
		vector<double> OOWP(n);

		vector<int> games(n, 0);
		for (int i = 0; i < n; ++i)
			cin >> teams[i];
		cout << "Case #" << t + 1 << ":" << endl;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (teams[i][j] != '.') {
					++games[i];
					if (teams[i][j] == '1')
						++wins[i];
				}
			}
		}

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (teams[j][i] != '.') {
					if (teams[j][i] == '1') {
						WP[i][j] = (double)(wins[j] - 1) / (games[j] - 1);
					}
					else {
						WP[i][j] = (double)wins[j] / (games[j] - 1);
					}
				}
			}
		}

		for (int i = 0; i < n; ++i) {
			double sum = 0.0;
			for (int j = 0; j < n; ++j) {
				if (teams[i][j] != '.') {
					sum += WP[i][j];
				}
			}
			OWP[i] = sum / games[i];
		}

		for (int i = 0; i < n; ++i) {
			double sum = 0.0;
			for (int j = 0; j < n; ++j) {
				if (teams[i][j] != '.') {
					sum += OWP[j];
				}
			}
			OOWP[i] = sum / games[i];
		}

		for (int i = 0; i < n; ++i) {
			cout << fixed << setprecision(10) << rpi((double)wins[i] / games[i], OWP[i], OOWP[i]) << endl;
		}

	}
	return 0;
}
