#include <stdio.h>

char sche[101][101];
int n;
int cnt[101];
int w[101];
double wp[101];
double owp[101];
double oowp[101];
double rpi[101];

void solve() {
	int i, j;

	scanf("%d", &n);
	for (i=0;i<n;i++) {
		scanf("%s", sche[i]);
		w[i]=cnt[i]=0;
		for (j=0;j<n;j++) {
			if (sche[i][j] != '.' ) {
				cnt[i]++;
				if (sche[i][j] == '1' ) {
					w[i]++;
				}
			}	
		}

		wp[i] = 1.0 * w[i] / cnt[i];
	}
	
	for (i=0;i<n;i++) {
		owp[i] = 0;
		for (j=0;j<n;j++) {
			if (sche[i][j] != '.') {
				if (sche[i][j] == '1' ) {
					owp[i] += 1.0 * w[j] / (cnt[j]-1);
				} else {
					owp[i] += 1.0 * (w[j]-1) / (cnt[j]-1);
				}
			}
		}
		owp[i] /= cnt[i];
	}

	for (i=0;i<n;i++) {
		oowp[i] = 0;
		for (j=0;j<n;j++) {
			if (sche[i][j] != '.') {
				oowp[i] += owp[j];
			}
		}
		oowp[i] /= cnt[i];
	}

	for (i=0;i<n;i++ ){
		rpi[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
		printf("%.12lf\n", rpi[i]);
	}
	
}

int main() {
	int t, i;
	scanf("%d", &t);
	for (i=1;i<=t;i++) {
		printf("Case #%d:\n", i);
		solve();
	}
	return 0;
}
