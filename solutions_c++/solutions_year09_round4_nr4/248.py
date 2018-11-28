#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <ctime>
#include <map>
#include <utility>


using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())
#define ensure(condition) if (!(condition)) fprintf(stderr, "failed: %s\n", #condition), exit(239)
#define x first
#define y second
#define pb push_back

int INF = 1000000000;

const int MAXN = 120;

int n;
int x[123], y[56], r[56];

double minx, maxx, miny, maxy;

inline double fun(double x1, double y1, double x2, double y2) {
	double res = -1;
	forn(i, n) {
		double d1 = sqrt((x[i] - x1) * (x[i] - x1) + (y[i] - y1) * (y[i] - y1));
		double d2 = sqrt((x[i] - x2) * (x[i] - x2) + (y[i] - y2) * (y[i] - y2));
		res = max(res , min(d1 + r[i], d2 + r[i]));
	}
	return res;
}

double f3(double x1, double y1, double x2) {
	double l = miny, r = maxy;
	forn(it, 46) {
		double tl = l + (r - l) / 3;
		double tr = tl + (r - l) / 3;
		if (fun(x1, y1, x2, tl) < fun(x1, y1, x2, tr))
			r = tr;
		else
			l = tl;
	}
	return fun(x1, y1, x2, (l + r) / 2);
}

double f2(double x1, double y1) {
	double l = minx, r = maxx;
	forn(it, 46) {
		double tl = l + (r - l) / 3;
		double tr = tl + (r - l) / 3;
		if (f3(x1, y1, tl) < f3(x1, y1, tr))
			r = tr;
		else
			l = tl;
	}
	return f3(x1, y1, (l + r) / 2);
}

double f1(double x1) {
	double l = miny, r = maxy;
	forn(it, 46) {
		double tl = l + (r - l) / 3;
		double tr = tl + (r - l) / 3;
		if (f2(x1, tl) < f2(x1, tr))
			r = tr;
		else
			l = tl;
	}
	return f2(x1, (l + r) / 2);
}

double f() {
	double l = minx, r = maxx;
	forn(it, 46) {
		double tl = l + (r - l) / 3;
		double tr = tl + (r - l) / 3;
		if (f1(tl) < f1(tr))
			r = tr;
		else
			l = tl;
	}
	return f1((l + r) / 2);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tu;
	cin >> tu;
	forn(tt, tu) {
		cin >> n;
		
		minx = 1e9, miny = 1e9, maxx = -1e9, maxy = -1e9;
		forn(i, n){
			cin >> x[i] >> y[i] >> r[i];
			maxx = max(maxx, 0. + x[i]);
			minx = min(minx, 0. + x[i]);
			maxy = max(maxy, 0. + y[i]);
			miny = min(miny, 0. + y[i]);
		}
		double res = f();
		cerr << tt + 1 << endl;
		printf("Case #%d: %.9lf\n", tt + 1, res);
	}


	
	return 0;
}