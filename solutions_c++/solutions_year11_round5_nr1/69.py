#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <numeric>
using namespace std;

#define FOR(i,a,b) for(int i=(a); i<(int)(b); ++i)
#define ALL(a) (a).begin(),(a).end()
#define PB(a) push_back(a)
#define MP(a,b) make_pair((a),(b))
#define sqr(a) ((a)*(a))
typedef long long i64;
typedef unsigned long long u64;

int nextInt() {
	int x;
	scanf("%d", &x);
	return x;
}

long long nextLong() {
	long long x;
	scanf("%I64d", &x);
	return x;
}

double nextDouble() {
	double x;
	scanf("%lf", &x);
	return x;
}

const int BUFSIZE = 1000000;
char buf[BUFSIZE + 1];
string nextString() {
	scanf("%s", buf);
	return buf;
}

typedef vector<vector<int> > Adj;

struct Point {
	double x, y;
	Point () {}
	Point (double x, double y) : x(x), y(y) {}
};

Point nextPoint() {
	double x = nextDouble();
	double y = nextDouble();
	return Point(x, y);
}

vector<Point> nextPolyline(int n) {
	vector<Point> poly(n);
	for (int i = 0; i < n; ++i) {
		poly[i] = nextPoint();
	}
	return poly;
}

double getArea(vector<Point> &poly, double x) {
	double res = 0;
	for (int i = 1; i < poly.size(); ++i) {
		if (poly[i].x <= x) {
			res += (poly[i - 1].y + poly[i].y) / 2 * (poly[i].x - poly[i - 1].x);
		} else {
			double y = poly[i - 1].y + (poly[i].y - poly[i - 1].y) * (x - poly[i - 1].x) / (poly[i].x - poly[i - 1].x);
			res += (poly[i - 1].y + y) / 2 * (x - poly[i - 1].x);
			break;
		}
	}
	return res;
}

double getArea(vector<Point> &upper, vector<Point> &lower, double x) {
	return getArea(upper, x) - getArea(lower, x);
}

double getCutX(vector<Point> &upper, vector<Point> &lower, double area, double W) {
	double R = 0.5 * W, dr = 0.5 * R;
	while (dr > 1e-12) {
		double cur = getArea(upper, lower, R);
		if (cur > area) {
			R -= dr;
		} else {
			R += dr;
		}
		dr *= 0.5;
	}
	return R;
}

int main() {
	double maxErr = 0;
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	int T = nextInt();
	for (int cas = 1; cas <= T; ++cas) {
		double W = nextDouble();
		int L = nextInt();
		int U = nextInt();
		int G = nextInt();
		vector<Point> lower = nextPolyline(L);
		vector<Point> upper = nextPolyline(U);
		double totalArea = getArea(upper, lower, W);
		vector<double> res;
		for (int i = 1; i < G; ++i) {
			double x = getCutX(upper, lower, totalArea / G * i, W);
			double err = fabs(getArea(upper, lower, x) - totalArea / G * i);
			if (err > maxErr) {
				maxErr = err;
				cerr << err << endl;
			}
			res.push_back(x);
		}
		cerr << cas << endl;
		printf("Case #%d:\n", cas);
		for (int i = 0; i < res.size(); ++i) {
			printf("%.10lf\n", res[i]);
		}
	}
	return 0;
}