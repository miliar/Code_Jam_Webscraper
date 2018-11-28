#include <cstdio>
#include <cstring>

const int N = 128;
char cscore[N][N];
int score[N][N];
int cnt[N], sct[N];
double wp[N], owp[N], oowp[N];


int main() {
	int t;
	scanf("%d", &t);
	for (int kase = 0; kase < t; ++kase) {
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%s", cscore[i]);
		}
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				score[i][j] = cscore[i][j] == '.'? -1 : (cscore[i][j] == '0'? 0 : 1);
			}
		}
		for (int i = 0; i < n; ++i) {
			cnt[i] = sct[i] = 0;
			for (int j = 0; j < n; ++j) {
				if (score[i][j] != -1) {
					cnt[i] ++;
					sct[i] += score[i][j];
				}
			}
			wp[i] = (double)sct[i] / cnt[i];
		}
		for (int i = 0; i < n; ++i) {
			owp[i] = 0.;
			for (int j = 0; j < n; ++j) {
				if (score[i][j] != -1) {
					owp[i] += (double)(sct[j] - score[j][i]) / (cnt[j] - 1);
				}
			}
			owp[i] /= cnt[i];
		}
		for (int i = 0; i < n; ++i) {
			oowp[i] = 0.;
			for (int j = 0; j < n; ++j) {
				if (score[i][j] != -1)
					oowp[i] += owp[j];
			}
			oowp[i] /= cnt[i];
		}
		printf("Case #%d:\n", kase + 1);
		for (int i = 0; i < n; ++i) {
			printf("%.7lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
		}
	}
	return 0;
}

