#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <cstring>

using namespace std;

int main() {

	int m[100][100];

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		memset(m, 0, sizeof(m));
		int N;
		cin >> N;

		int win[100];
		int loss[100];
		double owp[100];
		double wp[100];
		double oowp[100];
		memset(win, 0, sizeof(win));
		memset(loss, 0, sizeof(loss));
		memset(wp, 0.0, sizeof(wp));
		memset(owp, 0.0, sizeof(owp));
		memset(oowp, 0.0, sizeof(oowp));

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				char c;
				cin >> c;
				switch (c) {
				case '1':
					m[i][j] = 1;
					win[i]++;
					break;
				case '0':
					m[i][j] = 0;
					loss[i]++;
					break;
				case '.':
					m[i][j] = -1;
					break;
				}
			}
		}

		//WP
		for (int i = 0; i < N; i++) {
			wp[i] = (double) ((double)win[i] / (double)(win[i] + loss[i]));
		}
		//OWP

		for (int i = 0; i < N; i++) {
			double owpsum = 0.0;
			for (int j=0;j<N;j++) {
				if (i==j) continue;
				if (m[j][i] != -1) {
					if (m[j][i] == 1) {
//						double factor = (double)((double)1.0/(double)(win[j]+loss[j]));
						owpsum += (double)(win[j]-1) / (double)(win[j] + loss[j] -1);
					} else {
						owpsum += (double)(win[j]) / (double)(win[j] + loss[j] -1);
					}
				}
			}

			owp[i] = (double) owpsum/(double)(win[i]+loss[i]);
		}

		//OOWP
		for (int i = 0; i < N; i++) {
			double oowpsum = 0.0;
			for (int j=0;j<N;j++) {
				if (i==j) continue;
				if (m[i][j] == -1) continue;
				oowpsum += owp[j];
			}
			oowp[i] = (double) oowpsum/(double)(win[i]+loss[i]);
		}

		cout << "Case #" << t << ": " << endl;
		for (int i = 0; i < N; i++) {
			double R = 0.25 * wp[i] + 0.5 * owp[i] + 0.25*oowp[i];
			cout.precision(12);
			cout << R << endl;
		}


	}

	return 0;
}
