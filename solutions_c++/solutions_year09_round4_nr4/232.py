#include <iostream>
#include <math.h>
using namespace std;

struct pt {
	double x, y;
	double r;
};

double dist(pt a, pt b) {
	return sqrt( (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y) ) + a.r + b.r;
};

int i, j, k, n, m, t, T;

double x, y, z, r, res;

double miin(double x, double y) {
	return x < y ? x : y;
}
double maax(double x, double y) {
	return x > y ? x : y;
}
pt p[5];


int main() {
	freopen("small.in", "r", stdin);
	freopen("small.out", "w", stdout);
	cin >> T;
	for (t = 1; t <= T; t ++) {
		cin >> n;
		for (i = 0; i < n; i++) {
			cin >> p[i].x >> p[i].y >> p[i].r;
		}
		res = 10000000;
		if (n == 1) {
			res = p[0].r;
		} else if (n == 2) {
			res = maax(p[0].r, p[1].r);
		} else {
			x = maax(p[0].r*2, dist(p[1], p[2]));
			res = miin(res, x);
			x = maax(p[1].r*2, dist(p[0], p[2]));
			res = miin(res, x);
			x = maax(p[2].r*2, dist(p[0], p[1]));
			res = miin(res, x);
			res /= 2;
		}
		printf("Case #%d: %.7lf\n", t, res);
	}
	return 0;
}

