#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>

struct point {
	int x, y, r;
} p[60];

double dist(int a, int b) {
	int dx = p[a].x - p[b].x;
	int dy = p[a].y - p[b].y;
	return sqrt(dx*dx + dy*dy);
}

double max(double a, double b) {
	if (a > b) return a;
	return b;
}

int main(void) {
	int T;
	scanf("%d", &T);
	for (int C=1; C<=T; C++) {
		int n;
		double min = (double) INT_MAX;
		scanf("%d", &n);
		for (int i=0; i<n; i++)
			scanf("%d %d %d", &p[i].x, &p[i].y, &p[i].r);
		if (n == 1) {
			printf("Case #%d: %lf\n", C, (double) p[0].r);
		} else if (n == 2) {
			printf("Case #%d: %lf\n", C, max(p[0].r, p[1].r));
		} else {
			for (int i=0; i<n; i++) {
				for (int j=i+1; j<n; j++) {
					double t = dist(i,j) + p[i].r + p[j].r;
					if (t < min) min = t;
				}
			}
			printf("Case #%d: %lf\n", C, min / 2.0);
		}
	}
	return 0;
}
