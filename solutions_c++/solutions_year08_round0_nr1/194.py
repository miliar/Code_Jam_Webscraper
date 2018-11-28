#include <stdio.h>
#include <map>
#include <string>
using namespace std;

#define inf 1000000

int i, j, k, T, t, n, q;
int fre, x, y, mn;

int dp[1005][1005];

map<string, int> m;

char a[1005], cc;
int miin(int x, int y) {
	return x < y ? x : y;
}
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for (t = 1; t <= T; t ++) {
		fre = 0;
		m.clear();
		for (i = 0; i < 1005; i ++) {
			for (j = 0; j < 1005; j ++) {
				dp[i][j] = inf;
			}
		}

		scanf("%d%c", &n, &cc);
		for (i = 0; i < n; i ++) {
			memset(a, 0, sizeof(a));
			gets(a);
			m[a] = fre ++;
		}
		scanf("%d%c", &q, &cc);
		if (q == 0) {
			printf("Case #%d: 0\n", t);
			continue;
		}
		for (i = 0; i < q; i ++) {
			memset(a, 0, sizeof(a));
			gets(a);
			x = m[a];
			if (i == 0) {
				for (j = 0; j < n; j ++) {
					dp[0][j] = 0;
				}
				dp[0][x] = inf;
				continue;
			}
			for (j = 0; j < n; j ++) {
				if (j == x) {
					dp[i][j] = inf;
					continue;
				}
				mn = inf;
				for (k = 0; k < n; k++) {
					if (k == j) {
						mn = miin(dp[i-1][k], mn);
					} else {
						mn = miin(dp[i-1][k] + 1, mn);
					}
				}
				dp[i][j] = mn;
			}
		}
		mn = inf;
		for (j = 0; j < n; j ++) {
			mn = miin(mn, dp[i-1][j]);
		}
		printf("Case #%d: %d\n", t, mn);
	}
	return 0;
}


	

