#include <cstdio>
#include <cmath>

double distance(int ax, int ay, int bx, int by) {
	return sqrt((ax - bx) * (ax - bx) + (ay - by) * (ay - by));
}


int main() {
	int t, n;
	scanf("%d", &t);
	int x[16], y[16], r[16];
	for (int kase = 0; kase < t; ++kase) { 
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%d%d%d", &x[i], &y[i], &r[i]);
		}
		double ret = 1e10;
		if (n == 1) {
			ret = r[0];
		} else if (n == 2) {
			ret = r[0] >? r[1];
		} else if (n == 3) {
			ret <?= (distance(x[0], y[0], x[1], y[1]) + r[0] + r[1])/2 >? r[2];
			ret <?= (distance(x[0], y[0], x[2], y[2]) + r[0] + r[2])/2 >? r[1];
			ret <?= (distance(x[2], y[2], x[1], y[1]) + r[1] + r[2])/2 >? r[0];
		}
		printf("Case #%d: %lf\n", kase + 1, ret);
	}
	return 0;
}

