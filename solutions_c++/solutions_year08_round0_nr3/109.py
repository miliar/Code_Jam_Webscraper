#include <vector>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <string>
#include <cstdlib>
#include <map>
#include <queue>
#include <cmath>

using namespace std;

#define FOR(i,a,n) for (int i = (a); i < (n); ++i)
#define FORE(i,a,n) for (int i = (a); i <= (n); ++i)
#define FORD(i,a,b) for (int i = (a); i >= (b); --i)
#define REP(i,n) FOR(i,0,n)
#define REPE(i,n) FORE(i,0,n)
#define LL long long
#define FIR(n) REP(i,n)
#define FJR(n) REP(j,n)
#define ALL(v) v.begin(), v.end()

#define FI FIR(n)
#define FJ FJR(n)
#define FR(i,a) FOR(i,a,n)
#define REPN(i) REP(i,n)

typedef pair<int, int> PI;
typedef vector<PI> VPI;
// TYPES
template<class T> struct point_t {
	T x;
	T y;
	point_t(T x = T(), T y = T()) : x(x), y(y) {}

	bool operator<(const point_t<T>& p) const {
		return x == p.x ? y < p.y : x < p.x;
	}

	bool operator==(const point_t<T>& p) const {
		return x == p.x && y == p.y;
	}
};

template<class T> T inline vp (point_t<T> p1, point_t<T> p2) {
	return p1.x*p2.y - p1.y*p2.x;
}
template<class T> T inline cp (point_t<T> p1, point_t<T> p2) {
	return p1.x*p2.x + p1.y*p2.y;
}
template<class T> point_t<T> operator-(point_t<T> p1, point_t<T> p2) {
	return point_t<T>(p1.x - p2.x, p1.y - p2.y);
}

typedef point_t<double> point;
typedef vector<point> VPT;

#define sqrt2 1.414213562373095048801688724209
#define double long double

double rr;

VPT p;
point p1, p2;

double polyarea() {
	double r = 0;
	FOR(i,1, p.size())r += vp(p[i], p[i-1]);
	return abs(r)/2;
}

double segment(double r) {
	point p = p1-p2;
	double d = sqrt(cp(p,p))/2;
	double alpha = 2*asin(d/r);
	return rr/2*(alpha - sin(alpha));
}

double area(double x, double y, double g, double r) {
	if (x*x +y*y >= rr) return 0;

	double x2 = x+g, y2 = y + g;
	if (x2*x2 + y2*y2 <= rr) return g*g;

	p.clear();
	p.push_back(point(x, y));

	double x1 = x, y1 = y + g;

	if (x1*x1 + y1*y1 <= rr) {
		p.push_back(point(x1, y1));
		p.push_back(p1 = point(sqrt(rr-y1*y1), y1));
	} else {
		y1 = sqrt(rr-x1*x1);
		p.push_back(p1 = point(x1, y1));
	}

	double x3 = x + g, y3 = y;
	if (x3*x3 + y3*y3 <= rr) {
		p.push_back(p2 = point(x3, sqrt(rr-x3*x3)));
		p.push_back(point(x3, y3));
	} else {
		x3 = sqrt(rr-y3*y3);
		p.push_back(p2 = point(x3, y3));
	}
	p.push_back(point(x, y));
	
	return polyarea() + segment(r);
}

struct Task {

	double solve(double r, double W, double g) {
		rr =r*r;
		double res = 0, add = g+2*W;
		for(double x = W; x < r; x += add) {
			for (double y = W; x*x+y*y < rr; y += add) 
				res += area(x, y, g, r);
		}
		return 4*res;
	}

	double solve() {
		double f, R, t, r, g;
		cin >> f >> R >> t >> r >> g;

		double radius = R - t - f;
		double barW = r + f; if (barW >= radius) return 1;
		double gap = g - 2*f;  if (gap <= 0) return 1;

		return 1-solve(radius, barW, gap) / (3.1415926535897932384626433*R*R);
	}
};

int main() {
freopen("C-large.in", "rt", stdin);
freopen("C-large.out", "w", stdout);

	int tc; cin >>tc;
	REP(TC, tc) {
		Task t;
		double res = t.solve();
		printf("Case #%d: %.6lf\n", TC+1, res);
	}

fclose(stdout);
}
