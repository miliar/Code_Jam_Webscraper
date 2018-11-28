#include <stdio.h>
#include <string.h>
#include <algorithm>

int n, k, b, t;

int res[64][64];
int st[64], vel[64];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		scanf("%d%d%d%d", &n, &k, &b, &t);
		for (int i = 0; i<n; i++) scanf("%d", st+i);
		for (int i = 0; i<n; i++) scanf("%d", vel+i);

		memset(res, 63, sizeof(res));
		res[0][0] = 0;
		for (int i = 0; i<n; i++) {
			bool can = (st[i] + vel[i] * t >= b);
			for (int j = 0; j<=i; j++) if (res[i][j] < 1000000000) {
				if (can)
					if (res[i+1][j+1] > res[i][j])
						res[i+1][j+1] = res[i][j];
				if (res[i+1][j] > res[i][j] + j)
					res[i+1][j] = res[i][j] + j;
			}
		}

		int ans = 1000000000;
		for (int i = k; i<=n; i++) if (res[n][i] < ans) ans = res[n][i];
        
		printf("Case #%d: ", tt);
		if (ans == 1000000000) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}
	return 0;
}
