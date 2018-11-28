#define _CRT_SECURE_NO_WARNINGS
#include <map> 
#include <set> 
#include <cmath> 
#include <queue> 
#include <vector> 
#include <string> 
#include <cstdio> 
#include <cstdlib> 
#include <climits> 
#include <cstring> 
#include <cassert> 
#include <numeric> 
#include <algorithm> 
#include <iostream> 
#include <sstream> 
#include "float.h" 
#include <ctime> 
using namespace std; 

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (int i((n)-1); i >= 0; --i)
#define ALL(c) (c).begin(), (c).end()

typedef long long int64;
typedef unsigned long long uint64;

template<typename T> int size(const T& c) { return (int)c.size(); }
template<typename T> void remin(T& a, const T& b) { if (b < a) a = b; }
template<typename T> void remax(T& a, const T& b) { if (b > a) a = b; }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }

const double eps = 1e-9;

int cmp(double x, double y) {
	return fabs(x-y) < eps ? 0 : x < y ? -1 : +1;
}

int sgn(double x) {
	return cmp(x, 0);
}

struct Circle {
	double x, y, r;
	Circle(double x = 0, double y = 0, double r = -1): x(x), y(y), r(r) { }
	bool inside(double px, double py) const {
		return cmp(sqr(px-x)+sqr(py-y), sqr(r)) <= 0;
	}
};

bool insideAll(const vector<Circle>& cs, double px, double py) {
	REP(i, size(cs))
		if (!cs[i].inside(px, py))
			return false;
	return true;
}

bool inters(double x1, double y1, double r1, double x2, double y2, double r2, double& px1, double& py1, double& px2, double& py2) {
	double d = sqrt(sqr(x1-x2)+sqr(y1-y2));
	if (cmp(d, r1+r2) > 0 || cmp(r1, r2+d) > 0 || cmp(r2, r1+d) > 0)
		return false;
	double alfa = acos((sqr(r1)+sqr(d)-sqr(r2))/(2*r1*d));
	double vx = (x2-x1)*r1/d, vy = (y2-y1)*r1/d;
	px1 = x1+vx*cos(alfa)-vy*sin(alfa);
	py1 = y1+vx*sin(alfa)+vy*cos(alfa);
	alfa = -alfa;
	px2 = x1+vx*cos(alfa)-vy*sin(alfa);
	py2 = y1+vx*sin(alfa)+vy*cos(alfa);
	/*assert(cmp(sqr(px1-x1)+sqr(py1-y1), sqr(r1)) == 0);
	assert(cmp(sqr(px1-x2)+sqr(py1-y2), sqr(r2)) == 0);
	assert(cmp(sqr(px2-x1)+sqr(py2-y1), sqr(r1)) == 0);
	assert(cmp(sqr(px2-x2)+sqr(py2-y2), sqr(r2)) == 0);*/
	return true;
}

bool bla(vector<Circle> cs, double r, double& px, double& py) {
	int n = size(cs);
	REP(i, n) cs[i].r = r-cs[i].r;
	REP(i, n)
		if (insideAll(cs, cs[i].x, cs[i].y)) {
			px = cs[i].x;
			py = cs[i].y;
			return true;
		}
	REP(i, n) REP(j, i) {
		double x1, y1, x2, y2;
		if (inters(cs[i].x, cs[i].y, cs[i].r, cs[j].x, cs[j].y, cs[j].r, x1, y1, x2, y2)) {
			if (insideAll(cs, x1, y1)) {
				px = x1;
				py = y1;
				return true;
			}
			if (insideAll(cs, x2, y2)) {
				px = x2;
				py = y2;
				return true;
			}
		}
	}
	return false;
}

double minRadius(const vector<Circle>& cs, double& rx, double& ry) {
	int n = size(cs);
	if (n == 0) return 0;
	if (n == 1) return cs[0].r;
	double L = 0;
	REP(i, n)remax(L, cs[i].r);
	double R = 2*L;
	while (!bla(cs, R, rx, ry)) {
		L = R;
		R *= 2;
	}
	int iter = 132;
	while (R-L > 1e-20 && iter-- > 0) {
		double M = (L+R)/2;
		if (bla(cs, M, rx, ry))
			R = M;
		else
			L = M;
	}
	bool flag = bla(cs, R, rx, ry);
	assert(flag);
	return (L+R)/2;
}

int n;
vector<Circle> cs;
vector<int> kind;

double solve() {
	vector<Circle> circles;
	REP(i, n)
		if (kind[i] == 1)
			circles.push_back(cs[i]);
	double x, y;
	double r = minRadius(circles, x, y);
	circles.clear();
	REP(i, n)
		//if (cmp(sqrt(sqr(cs[i].x-x)+sqr(cs[i].y-y))+cs[i].r, r) > 0)
		if (kind[i] == 2)
			circles.push_back(cs[i]);
	return max(r, minRadius(circles, x, y));
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int ntests;
	scanf("%d", &ntests);
	FOR(test, 1, ntests) {
		double res = 1e32;
		scanf("%d", &n);
		cs.resize(n);
		REP(i, n) scanf("%lf%lf%lf", &cs[i].x, &cs[i].y, &cs[i].r);
		kind.resize(n);
		fill(ALL(kind), 2);
		REP(i, n) {
			kind[i] = 1;
			remin(res, solve());
			FOR(j, i+1, n-1) {
				kind[j] = 1;
				remin(res, solve());
				FOR(k, j+1, n-1) {
					kind[k] = 1;
					remin(res, solve());
					kind[k] = 2;
				}
				kind[j] = 2;
			}
			kind[i] = 2;
		}
		printf("Case #%d: %.13lf\n", test, res);
	}

	exit(0);
}
