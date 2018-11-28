#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int m[8092], p, c[20][8092];
long long dp[20][8092][20];
bool set[20][8092][20];

long long min(long long a, long long b)
{
	if (a < b) return a;
	return b;
}

void dpset(int r, int i, int j, long long v)
{
	if (!set[r][i][j] || dp[r][i][j] > v) dp[r][i][j] = v;
	set[r][i][j] = true;
}

int main()
{
	int cas, cases, i, j, k, l, r;
	assert(scanf("%d", &cases) == 1);
	for (cas = 1; cas <= cases; cas++) {
		assert(scanf("%d", &p) == 1);
		for (i = 0; i < (1 << p); i++) {
			assert(scanf("%d", &m[i]) == 1);
			assert(m[i] >= 0 && m[i] <= p);
		}
		for (r = 1; r <= p; r++) {
			for (i = 0; i < (1 << (p - r)); i++) {
				assert(scanf("%d", &c[r][i]) == 1);
			}
		}
		memset(set, 0, sizeof(set));
		for (r = 0; r <= p; r++) {
			for (i = 0; i < (1 << (p - r)); i++) {
				if (r == 0) {
					dpset(r, i, m[i], 0);
				} else {
					for (j = 0; j <= p; j++) {
						if (!set[r - 1][2 * i][j]) continue;
						for (k = 0; k <= p; k++) {
							if (!set[r - 1][2 * i + 1][k]) continue;
							l = min(j, k);
							//printf("%d: %d/%d -> %d\n", i, j, k, l);
							dpset(r, i, l, dp[r - 1][2 * i][j] + dp[r - 1][2 * i + 1][k] + c[r][i]);
							if (l > 0) dpset(r, i, l - 1, dp[r - 1][2 * i][j] + dp[r - 1][2 * i + 1][k]);
						}
					}
				}
				//printf("%d/%d: ", r, i);
				//for (l = 0; l <= p; l++) if (set[r][i][l]) printf(" %d/%lld", l, dp[r][i][l]);
				//printf("\n");
			}
		}
		printf("Case #%d: %lld\n", cas, dp[p][0][0]);
	}
	return 0;
}
