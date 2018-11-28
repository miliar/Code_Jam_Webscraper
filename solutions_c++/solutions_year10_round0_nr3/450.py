#include <cstdio>

int main () {
	int t, r, k, n, g[1005], l;
	long long c[31][1005][2], fill;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		scanf("%d %d %d", &r, &k, &n);
		for (int j = 0; j < n; j++) {
			scanf("%d", g + j);
		}
		for (int j = 0; j < n; j++) {
			fill = g[j];
			for (l = (j + 1) % n; l != j && fill + g[l] <= k; l = (l + 1) % n) {
				fill += g[l];
			}
			c[0][j][0] = fill;
			c[0][j][1] = l;
		}
		for (int j = 1; j < 31; j++) {
			for (int l = 0; l < n; l++) {
				c[j][l][0] = c[j-1][l][0] + c[j-1][c[j-1][l][1]][0];
				c[j][l][1] = c[j-1][c[j-1][l][1]][1];
			}
		}
		long long sum = 0;
		int point = 0;
		for (int j = 0; j < 31; j++) {
			if ((r & (1<<j)) != 0) {
				sum += c[j][point][0];
				point = c[j][point][1];
			}
		}
		printf("Case #%d: %lld\n", i, sum);
	}
	return 0;
}
