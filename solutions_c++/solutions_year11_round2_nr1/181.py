#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

typedef long double ld;
string data[128];
int N;

ld OWP[128];
ld WP[128];

int main() {
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; ++tt) {
		cin >> N;
		for (int i = 0; i < N; ++i) {
			cin >> data[i];
		}
		for (int i = 0; i < N; ++i) {
			{
				int wins = 0, lose = 0;
				for (int j = 0; j < N; ++j) {
					if (data[i][j] == '1') {
						wins++;
					} else if (data[i][j] == '0') {
						lose++;
					}
				}
				WP[i] = wins;
				WP[i] /= (wins + lose);
			}

			OWP[i] = 0;
			int opponents = 0;
			for (int j = 0; j < N; ++j) {
				int wins = 0, lose = 0;
				if (data[i][j] == '.') {
					continue;
				}
				for (int k = 0; k < N; ++k) {
					if (k == i) continue;
					if (data[j][k] == '1') {
						wins++;
					} else if (data[j][k] == '0') {
						lose++;
					}
				}
				ld wp = wins;
				wp /= (wins + lose);
				OWP[i] += wp;
				opponents++;
			}
			OWP[i] /= opponents;
		}

		cout << "Case #" << tt << ":" << endl;

		for (int i = 0; i < N; ++i) {
			ld OOWP = 0;
			int opponents = 0;
			for (int j = 0; j < N; ++j) {
				if (data[i][j] == '.') {
					continue;
				}
				OOWP += OWP[j];
				opponents++;
			}
			OOWP /= opponents;

			ld RPI = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP;

			cout.precision(12);
			cout.setf(ios::fixed);
			cout << RPI << endl;
		}
	}
	return 0;
}

