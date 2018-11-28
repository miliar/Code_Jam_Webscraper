#include <stdio.h>

#define eq(a, b) if (a > (b)) a = (b)

int n, m, v, g[5000], c[5000], cost[10000][2];

int main() {
	FILE * fin = fopen("cheating.in", "r"), * fout = fopen("cheating.out", "w");
	int i, j, x;
	fscanf(fin, "%d", &n);
	for (i = 1; i <= n; ++i) {
		fscanf(fin, "%d%d", &m, &v);
		for (j = 1; j <= (m - 1) >> 1; ++j) {
			fscanf(fin, "%d%d", g + j, c + j);
			cost[j][0] = 10000;
			cost[j][1] = 10000;
		}
		for ( ; j <= m; ++j) {
			fscanf(fin, "%d", &x);
			if (x) {
				cost[j][1] = 0;
				cost[j][0] = 10000;
			} else {
				cost[j][0] = 0;
				cost[j][1] = 10000;
			}
		}
		for (j = (m - 1) >> 1; j > 0; --j) {
			if (g[j]) {
				eq(cost[j][1], cost[j << 1][1] + cost[(j << 1) ^ 1][1]);
				eq(cost[j][0], cost[j << 1][1] + cost[(j << 1) ^ 1][0]);
				eq(cost[j][0], cost[j << 1][0] + cost[(j << 1) ^ 1][1]);
				eq(cost[j][0], cost[j << 1][0] + cost[(j << 1) ^ 1][0]);
				if (c[j]) {
					eq(cost[j][1], cost[j << 1][1] + cost[(j << 1) ^ 1][0] + 1);
					eq(cost[j][1], cost[j << 1][0] + cost[(j << 1) ^ 1][1] + 1);
				}
			} else {
				eq(cost[j][1], cost[j << 1][1] + cost[(j << 1) ^ 1][1]);
				eq(cost[j][1], cost[j << 1][1] + cost[(j << 1) ^ 1][0]);
				eq(cost[j][1], cost[j << 1][0] + cost[(j << 1) ^ 1][1]);
				eq(cost[j][0], cost[j << 1][0] + cost[(j << 1) ^ 1][0]);
				if (c[j]) {
					eq(cost[j][0], cost[j << 1][1] + cost[(j << 1) ^ 1][0] + 1);
					eq(cost[j][0], cost[j << 1][0] + cost[(j << 1) ^ 1][1] + 1);
				}
			}
		}
		if (cost[1][v] < 10000) {
			fprintf(fout, "Case #%d: %d\n", i, cost[1][v]);
		} else {
			fprintf(fout, "Case #%d: IMPOSSIBLE\n", i);
		}
	}
	return 0;
}
