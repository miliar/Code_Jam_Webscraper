#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

char s[105][105];
int w[105], l[105], cnt[105];
double owp[105];
int n;
int main() {
	int T; scanf("%d", &T);
	int cas = 0;
	while (T--) {
		memset(s, 0, sizeof(s));
		memset(w, 0, sizeof(w));
		memset(l, 0, sizeof(l));
		memset(owp, 0, sizeof(owp));
		printf("Case #%d:\n", ++cas);
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) scanf("%s", s[i]);
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (s[i][j] == '1') {
					++w[i];
				} else if (s[i][j] == '0') {
					++l[i];
				}
			}
		}
		double towp = 0;
		memset(cnt, 0, sizeof(cnt));
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (s[j][i] == '.') continue;
				++cnt[i];
				int f = 0;
				if (s[j][i] == '1') f = -1;
				owp[i] += (w[j] + f) * 1. / (w[j] + l[j] - 1);
			}
			owp[i] /= cnt[i];
		}
		for (int i = 0; i < n; ++i) {
			double wp = w[i] * 1. / (w[i] + l[i]);
			double twp = 0;
			for (int j = 0; j < n; ++j) {
				if (s[j][i] == '.') continue;
				twp += owp[j];
			}
			//printf("%f %f %f\n", wp, owp[i], (twp  / (n - 1));
			printf("%.8f\n", 0.25 * wp + 0.5 * owp[i] + 0.25 * (twp)/ (cnt[i]));
		}
	}
	return 0;
}
