#include <stdio.h>
#include <math.h>

#define max(x, y) (x > y ? x : y)
#define min(x, y) (x < y ? x : y)
#define dist(p, q) (sqrt((double) (x[p] - x[q]) * (x[p] - x[q]) + (y[p] - y[q]) * (y[p] - y[q])))

int T, n, x[50], y[50], r[50];
double d, tmp;

int main() {
	int lT, i;
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	scanf("%d", &T);
	for (lT = 1; lT <= T; lT++) {
		scanf("%d", &n);
		for (i = 1; i <= n; i++)
			scanf("%d%d%d", &x[i], &y[i], &r[i]);
		if (n == 1) {
			d = r[1];
		} else if (n == 2) {
			d = max(r[1], r[2]);
		} else if (n == 3) {
			d = max(r[1], (dist(1, 2) + r[1] + r[2]) / 2);
			d = min(d, max(r[2], (dist(1, 3) + r[1] + r[3]) / 2));
			d = min(d, max(r[3], (dist(2, 3) + r[2] + r[3]) / 2));
		}
		printf("Case #%d: %.6lf\n", lT, d);
	}
	return 0;
}