#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN = 512;
long long a[MAXN][MAXN], s[MAXN][MAXN], x[MAXN][MAXN], y[MAXN][MAXN];

int main() {
	int re, r, c, ans;

	scanf("%d", &re);
	for (int ri = 1; ri <= re; ++ri) {
		scanf("%d%d%*d", &r, &c);
		memset(a, 0, sizeof(a));
		memset(s, 0, sizeof(s));
		memset(x, 0, sizeof(x));
		memset(y, 0, sizeof(y));
		for (int i = 1; i <= r; ++i) {
			for (int j = 1; j <= c; ++j) {
				scanf("%1lld", &a[i][j]);
				s[i][j] = a[i][j];
				x[i][j] = a[i][j] * i;
				y[i][j] = a[i][j] * j;
			}
		}

		for (int i = 1; i <= r; ++i) {
			for (int j = 1; j <= c; ++j) {
				s[i][j] += s[i][j - 1];
				x[i][j] += x[i][j - 1];
				y[i][j] += y[i][j - 1];
			}
			for (int j = 1; j <= c; ++j) {
				s[i][j] += s[i - 1][j];
				x[i][j] += x[i - 1][j];
				y[i][j] += y[i - 1][j];
			}
		}

		ans = -1;
		for (int k = min(r, c); ans == -1 && k >= 3; --k) {
			for (int i = k; ans == -1 && i <= r; ++i) {
				for (int j = k; ans == -1 && j <= c; ++j) {
					long long ss = s[i][j] + s[i - k][j - k] - s[i][j - k] - s[i - k][j];
					long long sx = x[i][j] + x[i - k][j - k] - x[i][j - k] - x[i - k][j];
					long long sy = y[i][j] + y[i - k][j - k] - y[i][j - k] - y[i - k][j];
					for (int ii = i - k + 1; ii <= i; ii += k - 1) {
						for (int jj = j - k + 1; jj <= j; jj += k - 1) {
							ss -= a[ii][jj];
							sx -= a[ii][jj] * ii;
							sy -= a[ii][jj] * jj;
						}
					}
				//	printf("(%d, %d, %d) = %lld %lld %lld\n", k, i, j, ss, sx, sy);
					if (sx * 2 == ss * (i + i - k + 1) && sy * 2 == ss * (j + j - k + 1)) {
						ans = k;
					}
				}
			}
		}
		printf("Case #%d: ", ri);
		if (ans == -1) {
			puts("IMPOSSIBLE");
		} else {
			printf("%d\n", ans);
		}
	}

	return 0;
}

