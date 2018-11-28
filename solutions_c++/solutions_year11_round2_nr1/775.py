#include <cstdio>
#include <cstring>

char mat[100][101];
int WP[100];
int ngames[100];
double OWP[100];
double OOWP[100];

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int n;
		scanf("%d\n", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%s", mat[i]);
		}
		// calculate WP's
		for (int i = 0; i < n; ++i) {
			ngames[i] = 0;
			WP[i] = 0;
			for (int j = 0; j < n; ++j) {
				if (mat[i][j] == '1') {
					++ngames[i];
					WP[i] += 1;
				} else if (mat[i][j] == '0') {
					++ngames[i];
				}
			}
		}

		// calculate OWP's
		for (int i = 0; i < n; ++i) {
			int nopponents = 0;
			OWP[i] = 0;
			for (int j = 0; j < n; ++j) {
				if (mat[i][j] == '1') {
					OWP[i] += (double)WP[j]/(double)(ngames[j] - 1);
					++nopponents;
				} else if (mat[i][j] == '0') {
					OWP[i] += (double)(WP[j] - 1)/(double)(ngames[j] - 1);
					++nopponents;
				}
			}
			OWP[i] /= (double)nopponents;
		}

		// calculate OOWP's
		for (int i = 0; i < n; ++i) {
			int nopponents = 0;
			OOWP[i] = 0;
			for (int j = 0; j < n; ++j) {
				if (mat[i][j] != '.') {
					OOWP[i] += OWP[j];
					++nopponents;
				}
			}
			OOWP[i] /= (double)nopponents;
		}

		printf("Case #%d:\n", t);
		for (int i = 0; i < n; ++i) {
			double RPI;
			RPI = 0.25*(double)WP[i]/(double)ngames[i];
			RPI += 0.5 * OWP[i];
			RPI += 0.25 * OOWP[i];
			//printf("%.12f\n", RPI);
			printf("%.13lf\n", RPI);
		}
		

	}
	return 0;
}
