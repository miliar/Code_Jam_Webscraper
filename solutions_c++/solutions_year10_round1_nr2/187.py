#include <cstdio>
#include <cmath>
#include <algorithm>

#define INF 1000000000
#define MAXN 128
#define MAXV 256

int a[MAXN];
int f[MAXN][MAXV + 1];

using namespace std;

int main() {
	freopen("smooth.in", "r", stdin);
	freopen("smooth.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int ti = 0; ti < t; ti++) {
		fprintf(stderr, "%d\n", ti);
		int del, ins, m, n;
		scanf("%d%d%d%d", &del, &ins, &m, &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", &a[i]);
		}

		for (int i = 0; i <= n; i++) {
			for (int j = 0; j <= MAXV; j++) {
				f[i][j] = INF;
			}
		}

		f[0][MAXV] = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j <= MAXV; j++) {
				if (f[i][j] == INF) {
					continue;
				}

				// Delete the current one
				f[i + 1][j] = min(f[i][j] + del, f[i + 1][j]);
				
				// Move the current one
				for (int k = 0; k < MAXV; k++) {
					if (j != MAXV && abs(k - j) > m) {
						continue;
					}
					f[i + 1][k] = min(f[i][j] + abs(k - a[i]), f[i + 1][k]);
				}
			}

			// Insert after this one
			for (int j = 0; j < MAXV; j++) {
				for (int k = 0; k <= MAXV; k++) {
					if (f[i + 1][j] == INF || m == 0) {
						continue;
					}
					int cnt = (k != MAXV) ? (abs(j - k) + m - 1) / m : 1;
					f[i + 1][j] = min(f[i + 1][k] + cnt * ins, f[i + 1][j]);
				}
			}
		}
		
		int res = INF;
		for (int j = 0; j <= MAXV; j++) {
			res = min(f[n][j], res);
		}
		printf("Case #%d: %d\n", ti + 1, res);
	}
	return 0;
}