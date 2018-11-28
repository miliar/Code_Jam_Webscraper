#include <stdio.h>

char a[103][103];
int i, j, k, n;
char s[1003];
double wp[103], owp[103], oowp[103];

int main() {
	int cases,kejs;
	scanf("%d", &cases);
	for (kejs = 1; kejs <= cases; kejs++) {
		printf("Case #%d:\n", kejs);
		scanf("%d", &n);
		for (i = 0; i < n; i++) {
			scanf("%s", a[i]);
		}
		for (i = 0; i < n; i++) {
			int cnt = 0, sum = 0;
			for (j = 0; j < n; j++) {
				if (a[i][j] == '1') {
					cnt++;
					sum++;
				}
				if (a[i][j] == '0') {
					cnt++;
				}
			}
			wp[i] = ((double) sum) / cnt;
		}
		for (k = 0; k < n; k++) {
			owp[k] = 0;
			int nn = 0;
			for (i = 0; i < n; i++) {
				if (i == k) continue;
				if (a[i][k] == '.') continue;
				nn++;
				int cnt = 0, sum = 0;
				for (j = 0; j < n; j++) {
					if (j == k) continue;
					if (a[i][j] == '1') {
						cnt++;
						sum++;
					}
					if (a[i][j] == '0') {
						cnt++;
					}
				}
				owp[k] += ((double) sum) / cnt;
			}
			owp[k] /= nn;
		}
		for (k = 0; k < n; k++) {
			oowp[k] = 0;
			int nn = 0;
			for (i = 0; i < n; i++) {
				if (i == k) continue;
				if (a[i][k] == '.') continue;
				nn++;
				oowp[k] += owp[i];
			}
			oowp[k] /= nn;
//			printf("%.10lf\n", oowp[k]);
			printf("%.10lf\n", 0.25 * wp[k] + 0.50 * owp[k] + 0.25 * oowp[k]);
		}
	}
	return 0;
}
