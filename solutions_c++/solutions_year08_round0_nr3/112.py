#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <sstream>
#include <iostream>
#include <queue>
#include <set>
#include <map>

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define LD long double
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define DFOR(a,b) for(int a=b-1;a>=0;a--)
#define CLR(a,b) memset(a,b,sizeof(a))
#define eps 1e-13

#define PI 3.1415926535897932384626433832795
#define point pair<double, double>

using namespace std;

double f, R, t, r, g;
double rad, a, d0, d;

double GetArea(vector<point> a) {
	double res = 0;
	int n = SZ(a);
	FOR(i, n) res += a[i].first * a[(i+1)%n].second - a[i].second * a[(i+1)%n].first;
	return 0.5 * ABS(res);
}

double CircleArea(point p1, point p2) {
	double x = sqrt(SQR(p1.first - p2.first) + SQR(p1.second - p2.second));
	return rad*rad*asin(0.5*x/rad) - 0.5*x*sqrt(rad*rad-0.25*x*x);
}

double calc(double x, double y) {
	double dist1 = sqrt(x*x + y*y);
	if (dist1 >= rad - eps) return 0;
	double dist2 = sqrt(SQR(x+a)+SQR(y+a));
	if (dist2 <= rad + eps) return a*a;
	vector<point> p;
	point p1, p2;
	p.PB(MP(x,y));
	// first point
	dist1 = sqrt(SQR(x+a)+SQR(y));
	if (dist1 <= rad - eps) {
		p.PB(MP(x+a, y));
		p1.first = x+a;
		p1.second = sqrt(SQR(rad) - SQR(x+a));
		p.PB(p1);
	} else {
		p1.first = sqrt(SQR(rad) - SQR(y));
		p1.second = y;
		p.PB(p1);
	}
	// second point
	dist2 = sqrt(SQR(x)+SQR(y+a));
	if (dist2 <= rad - eps) {
		p2.first = sqrt(SQR(rad)-SQR(y+a));
		p2.second = y+a;
		p.PB(p2);
		p.PB(MP(x, y+a));
	} else {
		p2.first = x;
		p2.second = sqrt(SQR(rad)-SQR(x));
		p.PB(p2);
	}
	return GetArea(p) + CircleArea(p1, p2);
}

void solvecase() {
	scanf("%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g);
	a = g - 2 * f;
	d0 = r + f;
	d = 2 * r + g;
	rad = R - t - f;
	double ans;
	if (rad <= 0 || a <= 0) {
		ans = 1.0;
	} else {
		double area = 0;
		for (double x = d0; ; x += d) {
			int k = 0;
			for (double y = d0; ; y += d) {
				double t = calc(x, y);
				if (t < eps) break;
				area += t;
				k++;
			}
			if (k == 0) break;
		}
		ans = 1 - (4 * area) / (PI * R * R);
	}
	printf("%.7lf", ans);
}

void solve() {
	int n;
	scanf("%d\n", &n);
	FOR(i, n) {
		printf("Case #%d: ", i+1);
		solvecase();
		printf("\n");
	}
}

int main() {
	freopen("c2", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}