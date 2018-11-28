#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cassert>
#include <string>
#include <cstdio>
#include <cmath>
#include <stack>
#define sz(x) ((int)(x.size()))
#define all(c) (c).begin(),(c).end() 
#define pb push_back 
#define mp make_pair
#define foreach(T, x, it) for (T::iterator it = x.begin(); it != x.end(); ++it)
using namespace std;
typedef long long lint;
typedef pair<int, int> pii;
typedef vector<int> vi;

struct Point {
	double x, y;
	Point(double x = 0.0, double y = 0.0) : x(x), y(y) {}
};
//------------------------------------------------------------------------------
const double eps = 1e-8;
//------------------------------------------------------------------------------
inline bool Eq(long double x, long double y) { return fabs(x - y) <= eps; }
inline bool Le(long double x, long double y) { return x <= y || Eq(x, y); }
inline bool Lt(long double x, long double y) { return x < y && !Eq(x, y); }
inline bool Ge(long double x, long double y) { return x >= y || Eq(x, y); }
inline bool Gt(long double x, long double y) { return x > y && !Eq(x, y); }
inline Point operator +(Point a, Point b) { return Point(a.x + b.x, a.y + b.y); }
inline Point operator -(Point a, Point b) { return Point(a.x - b.x, a.y - b.y); }
inline Point operator *(Point a, double b) { return Point(a.x * b, a.y * b); }
inline double Vect(Point a, Point b) { return a.x * b.y - a.y * b.x; }
inline double Scal(Point a, Point b) { return a.x * b.x + a.y * b.y; }
inline double Sqr(double x) { return x * x; }
inline double Dist(Point a) { return sqrt(Sqr(a.x) + Sqr(a.y)); }
inline int Sgn(double x) { return Eq(x, 0.0) ? 0 : (x > 0 ? 1 : -1); }


int N;
vector<Point> P;
vector<double> R;

double Get(vector<pair<Point, double> > o) {
	if (sz(o) == 1) return o[0].second;
	if (sz(o) == 2) {
		double d = Dist(o[0].first - o[1].first);
		d += o[0].second + o[1].second;
		return d * 0.5;
	}
	assert(false);
	return false;
}

bool Test(int x, int p) { return (x >> p) & 1; }

bool Check(double r) {
	for (int use = 1; use < (1 << N) - 1; ++use) {
		vector<pair<Point, double> > o1, o2;
		for (int i = 0; i < N; ++i) {
			if (Test(use, i)) {
				o1.pb(mp(P[i], R[i]));
			}
			else {
				o2.pb(mp(P[i], R[i]));
			}
		}
		double r1 = Get(o1);
		double r2 = Get(o2);
		double mx = max(r1, r2);
		if (Ge(r, mx)) return true;
	}
	return false;
}

void Solve(int num) {
	cin >> N;	
	P.assign(N, Point());
	R.assign(N, 0);
	for (int i = 0; i < N; ++i) {
		cin >> P[i].x >> P[i].y >> R[i];
	}

	if (N == 1) {
		double an = R[0];
		printf("Case #%d: %0.6lf\n", num, an);
		return;
	}

	double lo = 0.0, hi = 1e9;
	while (fabs(hi - lo) > 1e-7) {
		double mid = (lo + hi) * 0.5;
		if (Check(mid)) hi = mid;
		else lo = mid;
	}
	double ans = lo;
	printf("Case #%d: %0.6lf\n", num, ans);
}


int main() {	
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int tst;
	cin >> tst;
	for (int i = 1; i <= tst; ++i) Solve(i);
	return 0;
}

