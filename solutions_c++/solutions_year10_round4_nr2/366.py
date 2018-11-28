#include <cstdio>

#define min(x, y) ((x) < (y) ? (x) : (y))

#define MAX 1000000000
#define P_MAX 10

int t, p, m[1 << P_MAX], w[1 << P_MAX];
int d[1 << (P_MAX + 1)][P_MAX + 1];

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int lt, i, j, k, v;
	scanf("%d", &t);
	for (lt = 1; lt <= t; lt++) {
		scanf("%d", &p);
		for (i = 0; i < (1 << p); i++) {
			scanf("%d", &m[i]);
			for (j = 0; j <= p; j++) {
				d[(1 << p) + i][j] = (j < p - m[i] ? MAX : 0);
			}
		}
		for (i = p - 1; i >= 0; i--) {
			for (j = 0; j < (1 << i); j++) {
				v = (1 << i) + j;
				scanf("%d", &w[v]);
				for (k = 0; k <= p; k++) {
					d[v][k] = (k ? d[v][k - 1] : MAX);
					d[v][k] = min(d[v][k], d[2 * v][k] + d[2 * v + 1][k]);
					if (k != p)
						d[v][k] = min(d[v][k], d[2 * v][k + 1] + d[2 * v + 1][k + 1] + w[v]);
				}
			}
		}
		printf("Case #%d: %d\n", lt, d[1][0]);
	}
	return 0;
}