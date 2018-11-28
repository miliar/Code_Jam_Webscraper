#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <sstream>
#include <set>
#include <math.h>
#include <map>
using namespace std;

#define N 505
#define eps 0.0000000001

struct pt {
	double x;
	double y;
	double z;
	friend pt operator + (pt a, pt b) {
		pt c;
		c.x = a.x + b.x;
		c.y = a.y + b.y;
		c.z = a.z + b.z;
		return c;
	}
	friend pt operator * (pt a, double b) {
		pt c;
		c.x = a.x *b;
		c.y = a.y *b;
		c.z = a.z *b;
		return c;
	}
	void clear() {
		x = y = z = 0;
	}
	double dist() {
		return x * x + y * y + z * z;
		return sqrt(x * x + y * y + z * z);
	}
};

pt a[N], v[N];
pt p, p1, p2;

int i, j, k, n, m, t, T;
double l, r, c1, c2, dx, x, y;
double inf;

double ab(double x) {
	return x >= 0 ? x : -x;
}

double cm(double t) {
	int i;
	pt p, p1, p2, p3;
	p.clear();
	for (i = 0; i < n; i ++) {
		p1 = a[i] + v[i] * t;
		p = p + p1;
	}
	p = p * (1.0 / n);
	return p.dist();
}

double rt, rd;
int cmp(double x, double y) {
	double epss = 0.000000000001;
	if (ab(x - y) < epss) {
		return 1;
	}
	if (ab(x / y - 1.0) < epss) {
		return 1;
	}
	return 0;
}

double get() {
	int i;
	double x, y, z, t;
	pt p, p1, p2;
	p.clear();
	p1.clear();
	p2.clear();
	x = y = 0;
	for (i = 0; i < n; i ++) {
//		x += (a[i].x*v[i].x + a[i].y * v[i].y + a[i].z * v[i].z);
//		y += v[i].x * v[i].x + v[i].y * v[i].y + v[i].z * v[i].z;
		p1 = p1 + a[i];
		p2 = p2 + v[i];
	}
	x = p1.x * p2.x + p1.y * p2.y + p1.z * p2.z;
	x = -x;
	y = p2.x * p2.x + p2.y * p2.y + p2.z * p2.z;
	if (ab(y) < eps) {
		return 0;
	}
	t = x / y;
	if (t < 0) {
		return 0;
	}
	return t;
}

int main() {
	freopen("large.in", "r", stdin);
	freopen("large.out", "w", stdout);

	cin >> T;
	inf = 1000000;
	for (t = 1; t <= T; t ++) {
		cin >> n;
		for (i = 0; i < n; i ++) {
			cin >> a[i].x >> a[i].y >> a[i].z >> v[i].x >> v[i].y >> v[i].z;
		}
/*		l = 0;
		r = inf;
		dx = r;
		while (dx > eps) {
			dx *= (2.0 / 3.0);
			c2 = l + dx;
			c1 = r - dx;
			x = cm(c1);
			y = cm(c2);
			if (cmp(x, y)) {
				r = c2;
			} else if (x > y) {
				l = c1;
			} else {
				r = c2;
			}
		}
		rt = (l + r) / 2;
		rd = sqrt(cm(rt));
*/
		rt = get();
		rd = sqrt(cm(rt));
		printf("Case #%d: %.6lf %.6lf\n", t, rd, rt);
	}
	return 0;
}

/*
1
3
-5 0 0 1 0 0
-7 0 0 1 0 0
-6 3 0 1 0 0

*/

