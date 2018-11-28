#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

int main()
{
	int t, n, i, j, count[200], win[200];
	double wp[200], owp[200], oowp[200];
	char schedule[200][200];
	scanf("%d", &t);
	for (int c = 1; c <= t; c++) {
		printf("Case #%d:\n", c);
		scanf("%d", &n);
		for (i = 0; i < n; i++) {
			scanf("%s", schedule[i]);
			count[i] = win[i] = 0;
			for (j = 0; j < n; j++) {
				if (schedule[i][j] != '.') count[i]++;
				if (schedule[i][j] == '1') win[i]++;
			}
			wp[i] = (double) win[i] / count[i];
			//printf("%s %f\n", schedule[i], wp[i]);
		}
		for (i = 0; i < n; i++) {
			owp[i] = 0;
			for (j = 0; j < n; j++) {
				if (schedule[i][j] != '.') {
					//printf("%f ", (double) (win[j] - (schedule[j][i] == '1' ? 1 : 0)) / (count[j] - 1));
					owp[i] += (double) (win[j] - (schedule[j][i] == '1' ? 1 : 0)) / (count[j] - 1);
				}
			}
			owp[i] /= count[i];
			//printf("%.8f\n", owp[i]);
		}
		for (i = 0; i < n; i++) {
			oowp[i] = 0;
			for (j = 0; j < n; j++) {
				if (schedule[i][j] != '.') {
					oowp[i] += owp[j];
				}
			}
			oowp[i] /= count[i];
			//printf("%f\n", oowp[i]);
			printf("%.8f\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
		}
	}
	return 0;
}
