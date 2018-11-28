#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES
#include <iostream>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <queue>
using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define all(c) c.begin(), c.end()
#define pb push_back
typedef vector<int> VI;

const double EPS = 1E-9;

#define x first
#define y second

typedef pair<double, double> Point;

double f, R, r, l, g;
double mx, my;

bool lessAng(Point p1, Point p2) {
	return atan2(p1.y - my, p1.x - mx) < atan2(p2.y - my, p2.x - mx);
}

bool onCircle(Point p) {
	return fabs(r - f - hypot(p.x, p.y)) < EPS;
}

vector<Point> intersect(Point p1, Point p2) {
	double a = p2.y - p1.y;
	double b = p1.x - p2.x;
	double c = -a * p1.x - b * p1.y;
	double ds = a * a + b * b;
	double sq = (r - f) * (r - f) * ds - c * c;
	if (sq < EPS) return vector<Point>(0);
	sq = sqrt(sq);
	vector<Point> res(2);
	res[0].x = (-a * c + b * sq) / ds;
	res[0].y = (-b * c - a * sq) / ds;

	res[1].x = (-a * c - b * sq) / ds;
	res[1].y = (-b * c + a * sq) / ds;
	return res;
}

double getAns() {
	if (f > r) return 1.0;
	if (2 * f > g - EPS) return 1.0;
	double ans = 0.0;
	for(int i = 0; ; ++i) {
		double lx = l + 2 * l * i + g * i;
		if (lx + f > r - f - EPS) break;
		double rx = lx + g - f;
		lx += f;
		for(int j = 0; ; ++j) {
			double ly = l + 2 * l * j + g * j;
			if (ly + f > r - f - EPS) break;
			double ry = ly + g - f;
			ly += f;
			vector<Point> a(4);
			a[0] = make_pair(lx, ly);
			a[1] = make_pair(rx, ly);
			a[2] = make_pair(rx, ry);
			a[3] = make_pair(lx, ry);
			bool allInside = true;
			forn(k, 4)
				if (hypot(a[k].x, a[k].y) > r - f + EPS) {
					allInside = false;
					break;
				}
			if (allInside) {
				ans += (rx - lx) * (ry - ly);
				continue;
			}
			vector<Point> b;
			forn(k, 4) {
				Point p1 = a[k], p2 = a[(k + 1) & 3];
				if (hypot(p1.x, p1.y) < r - f + EPS)
					b.pb(p1);
				if ((hypot(p1.x, p1.y) > r - f - EPS) ^ (hypot(p2.x, p2.y) > r - f - EPS)) {
					vector<Point> tmp = intersect(p1, p2);
					forn(tt, tmp.size())
						if (tmp[tt].x > 0 && tmp[tt].y > 0)
							b.pb(tmp[tt]);
				}
			}
			mx = 0.0;
			my = 0.0;
			forn(k, b.size()) {
				mx += b[k].x;
				my += b[k].y;
			}
			mx /= b.size();
			my /= b.size();

			sort(all(b), lessAng);
			double as = 0.0;
			forn(k, b.size()) {
				Point p1 = b[k], p2 = b[(k + 1) % b.size()];
				if (onCircle(p1) && onCircle(p2)) {
					double sn = fabs(p1.x * p2.y - p1.y * p2.x) 
						/ hypot(p1.x, p1.y) / hypot(p2.x, p2.y);
					if (sn > 1.0) sn = 1.0;
					if (sn < -1.0) sn = -1.0;
					ans += 0.5 * (r - f) * (r - f) * (asin(sn) - sn);
				}
				as += p1.x * p2.y - p1.y * p2.x;
			}
			ans += 0.5 * fabs(as);
		}
	}
	return 1.0 - 4 * ans / (M_PI * R * R);
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int tk;
	cin >> tk;
	for(int tc = 1; tc <= tk; ++tc) {
		double tmp;
		cin >> f >> R >> tmp >> l >> g;
		r = R - tmp;
		printf("Case #%d: %.6lf\n", tc, getAns());
	}

	return 0;
}