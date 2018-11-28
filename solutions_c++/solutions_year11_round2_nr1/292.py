#include <cstdio>
#include <cmath>

char maz[110][110];

double wp[110];
double owp[110];
double oowp[110];
double res[110];
int n;

double getwp(int i, int j) {
	double twp = 0;
	double x = 0, y = 0;
	for (int k = 1; k <= n; k++) {
		if (k == i) continue;
		if (maz[j][k] == '.') continue;
		x++;
		if (maz[j][k] == '1') y++;
	}
	if (x != 0)
		return y / x;
	else return 0;
}

int main() {
	int T;
	int i, j, k;
	scanf("%d", &T);
	int cas = 1;
	while (T--) {
		scanf("%d", &n);
		for (i = 1; i <= n; i++) {
			scanf("%s", maz[i] + 1);
		}
		
		for (i = 1 ; i <= n; i++) {
			double sumwp = 0;
			double cnt = 0;
			double cnt2 = 0;
			for (j = 1; j <= n; j++) {
				if (maz[i][j] != '.') {
					cnt++;
					if (maz[i][j] == '1') cnt2++;
					double twp = getwp(i, j);
					sumwp += twp;
				}
			}
			wp[i] = cnt2 / cnt;
			owp[i] = sumwp / cnt;
			//printf("%f\n", wp[i]);
			//printf("%f\n", owp[i]);
		}
		printf("Case #%d:\n", cas++);
		for (i = 1; i <= n; i++) {
			oowp[i] = 0;
			double sum = 0;
			for (j = 1; j <= n; j++) {
				if (maz[i][j] != '.') {
					sum++;
					oowp[i] += owp[j];
				}
			}
			oowp[i] /= sum;
			//printf("%f\n", oowp[i]);
			res[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
			printf("%0.7f\n", res[i]);
		}
	}
	return 0;
}