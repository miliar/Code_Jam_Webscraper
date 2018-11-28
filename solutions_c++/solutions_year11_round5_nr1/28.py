#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long int64;
#define E(c) cerr<<#c
#define Eo(x) cerr<<#x<<" = "<<(x)<<endl

struct Point {
    double x, y;
    Point(double _x = 0.0, double _y = 0.0) : x(_x), y(_y) {}

	Point operator- (Point b) const {
		return Point(x-b.x, y-b.y);
	}
};

double w;
int n[2], g;
Point pts[2][128];
vector<double> cuts;

double Calc(double cx) {
	double res = 0.0;

	for (int i = 0; i<2; i++) {
		double sgn = (i ? 1.0 : -1.0);

		int j;
		for (j = 0; j<n[i]; j++)
			if (pts[i][j+1].x > cx)
				break;
		if (j == n[i]) j--;
		int k = j;

		for (j = 0; j<k; j++)
			res += sgn * (pts[i][j].y + pts[i][j+1].y)/2.0 * (pts[i][j+1].x - pts[i][j].x);

		double cy = pts[i][j].y + (pts[i][j+1].y - pts[i][j].y) / (pts[i][j+1].x - pts[i][j].x) * (cx - pts[i][j].x);
		res += sgn * (pts[i][j].y + cy)/2.0 * (cx - pts[i][j].x);
	}

	return res;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {

		scanf("%lf", &w);
		scanf("%d%d%d", &n[0], &n[1], &g);

		for (int i = 0; i<2; i++) {
			for (int j = 0; j<n[i]; j++)
				scanf("%lf%lf", &pts[i][j].x, &pts[i][j].y);
			n[i]--;
		}

		double full = 0.0;
		for (int i = 0; i<2; i++) {
			for (int j = 0; j<n[i]; j++) {
				double sgn = (i ? 1.0 : -1.0);
				full += sgn * (pts[i][j].y + pts[i][j+1].y)/2.0 * (pts[i][j+1].x - pts[i][j].x);
			}
		}

		cuts.clear();
		for (int i = 1; i<=g-1; i++) {
			double area = full * i / g;

			double left = 0.0;
			double right = w;
			static const double DELTA = 1e-9;
			int iters = int(log((right-left) / DELTA) / log(2.0)) + 10;
			fprintf(stderr, "%d\n", iters);

			for (int t = 0; t<iters; t++) {
				double middle = (left + right) * 0.5;
				if (Calc(middle) > area)
					right = middle;
				else
					left = middle;
			}

			cuts.push_back(left);
		}

		printf("Case #%d:\n", tt);
		for (int i = 0; i<cuts.size(); i++) printf("%0.12lf\n", cuts[i]);
		fflush(stdout);
	}
	return 0;
}
