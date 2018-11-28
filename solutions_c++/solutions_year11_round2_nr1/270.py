#include <iostream>

using namespace std;

const int N = 102;

char s[N][N];

double wp[N];
double owp[N];
double oowp[N];

double rpi[N];

int w[N], sum[N];

int main() {

	int Tc;
	
	freopen( "A-large.in", "r", stdin );
	freopen( "A-large-out", "w", stdout );

	scanf("%d", &Tc);

	for (int tc = 1; tc <= Tc; ++tc) {

		int n;

		scanf("%d", &n);

		for (int i = 0; i < n; ++i) {
			scanf("%s", s[i]);
		}
		

		for (int i = 0; i < n; ++i) {
			w[i] = 0;
			sum[i] = 0;

			for (int j = 0; j < n; ++j) {
				if (s[i][j] == '1') {
					w[i]++;
				}
				if (s[i][j] == '1' || s[i][j] == '0') {
					sum[i]++;
				}
			}

			wp[i] = 1.0 * w[i] / sum[i];
		}

		for (int i = 0; i < n; ++i) {
			owp[i] = 0.0;
			for (int j = 0; j < n; ++j) {
				if (s[i][j] == '0' || s[i][j] == '1') {
					double tmp = 0.0;
					if (s[i][j] == '0') {
						tmp = 1.0 * (w[j] - 1) / (sum[j] - 1);
					} else {
						tmp = 1.0 * w[j] / (sum[j] - 1);
					}

					owp[i] += tmp;
				}
			}

			owp[i] /= sum[i];
		}

		for (int i = 0; i < n; ++i) {
			oowp[i] = 0.0;

			for (int j = 0; j < n; ++j) {
				if (s[i][j] == '0' || s[i][j] == '1') {
					oowp[i] += owp[j];
				}
			}

			oowp[i] /= sum[i];
		}
		

		for (int i = 0; i < n; ++i) {
			rpi[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
		}

		printf("Case #%d:\n", tc);

		for (int i = 0; i < n; ++i) {
			printf("%lf\n", rpi[i]);
		}
	}

	return 0;
}






