#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cctype>
#include <cmath>

#include <iostream>
#include <sstream>
#include <string>
#include <iomanip>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

#define pb push_back
#define mp make_pair

#define min(x, y) ((x) < (y) ? (x) : (y))
#define max(x, y) ((x) > (y) ? (x) : (y))
#define abs(x) ((x) < 0 ? (-(x)) : (x))

typedef double dbl;
typedef long double ldbl;
typedef long long i64;

const ldbl EPS = 1e-9;
const ldbl eps = 1e-9;

struct P {
	int x, y, r;
	bool operator<(const P &w) const {
		return r > w.r;
	}
} p[1000000];
struct Q {
	double x, y, r;
} q[1000000];
int u[1000000];

void draw(int i, int j, int k, double &x, double &y, double r) {
	dbl x1 = p[i].x, y1 = p[i].y, r1 = r - p[i].r;
	dbl x2 = p[j].x, y2 = p[j].y, r2 = r - p[j].r;
	dbl A, B, C, D, _D, E;
	if (abs(y2 - y1) >= eps) {
		A = (r1 * r1 - r2 * r2 + x2 * x2 - x1 * x1 + y2 * y2 - y1 * y1) / (2.0 * (y2 - y1));
		B = (x1 - x2) / (y2 - y1);
		C = 1 + B * B; D = A * B - x1 - B * y1; E = x1 * x1 + y1 * y1 + A * A - 2 * A * y1 - r1 * r1;
		_D = D * D - C * E;
		if (_D > -eps) {
			if (abs(_D) < eps) _D = 0.0;
			else _D = sqrt(_D);
			if (k == 0) {
				x = (-D + _D) / C;
				y = A + B * x;
			} else {
				x = (-D - _D) / C;
				y = A + B * x;
			}
		}
    } else {
		A = (r1 * r1 - r2 * r2 + y2 * y2 - y1 * y1 + x2 * x2 - x1 * x1) / (2.0 * (x2 - x1));
		B = (y1 - y2) / (x2 - x1);
		C = 1 + B * B; D = A * B - y1 - B * x1; E = y1 * y1 + x1 * x1 + A * A - 2 * A * x1 - r1 * r1;
		_D = D * D - C * E;
		if (_D > -eps) {
			if (abs(_D) < eps) _D = 0.0;
			else _D = sqrt(_D);
			if (k == 0) {
				y = (-D + _D) / C;
				x = A + B * y;
			} else {
				y = (-D - _D) / C;
				x = A + B * y;
			}
		}
	}
}

inline double distance(dbl x1, dbl y1, dbl x2, dbl y2) {
	return sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
}

bool check(int n, double r) {
	int c = 0;
	for (int i = 0; i < n; ++i) {
		q[c].x = p[i].x; q[c].y = p[i].y; ++c;
		for (int j = i + 1; j < n; ++j) {
			double x11, y11, x12, y12;
			draw(i, j, 0, x11, y11, r);
			draw(i, j, 1, x12, y12, r);
			q[c].x = x11; q[c].y = y11; ++c;
			q[c].x = x12; q[c].y = y12; ++c;
//			cout << i << " " << j << " " << x11 << " " << y11 << endl;
//			cout << i << " " << j << " " << x12 << " " << y12 << endl;
		}
	}
	for (int i = 0; i < c; ++i) {
		for (int t = 0; t < n; ++t) {
			if ((distance(q[i].x, q[i].y, p[t].x, p[t].y) + p[t].r < r + EPS)) {
				u[t] = 1;
			} else {
				u[t] = 0;
			}
		}
		for (int j = i + 1; j < c; ++j) {
			bool f = true;
			for (int t = 0; t < n; ++t) if (!u[t]) {
				if ((distance(q[j].x, q[j].y, p[t].x, p[t].y) + p[t].r < r + EPS)) {
					u[t] = 2;
				} else {
					f = false;
					break;
				}
			}
			if (f) return true;
			for (int t = 0; t < n; ++t) if (u[t] == 2) {
				u[t] = 0;
			}
		}
	}
	return false;
}

int main() {
	int T; scanf("%d", &T);
	for (int tt = 0; tt < T; ++tt) {
		double result = 0;
		int n; scanf("%d", &n);
		double l = 0.0, r = 1e6;
		for (int i = 0; i < n; ++i) {
			scanf("%d %d %d", &p[i].x, &p[i].y, &p[i].r);
			l = max(l, p[i].r);
		}
		sort(p, p + n);
		int m = 0;
		for (int i = 0; i < n; ++i) {
			bool f = false;
			for (int j = 0; j < i; ++j) {
				if (distance(p[j].x, p[j].y, p[i].x, p[i].y) + p[i].r <= p[j].r) {
					f = true;
					break;
				}
			}
			if (!f) {
				p[m++] = p[i];
			}
		}
		n = m;
		if (n < 3) {
			result = l;
		} else {
			while (l + EPS <= r) {
				double t = (l + r) * 0.5;
				if (check(n, t)) {
					r = t;
				} else {
					l = t;
				}
			}
			result = l;
		}
		printf("Case #%d: %.8lf\n", tt + 1, result);
		fflush(stdout);
	}
	return 0;
}
