#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

const double EPS = 1e-8;

struct Point {
	double x, y;
	Point(double x = 0.0, double y = 0.0) : x(x), y(y) {}
	bool operator < (const Point& p) const {
		return x < p.x - EPS || (x < p.x + EPS && y < p.y - EPS);
	}
};

int T, W, L, U, G;
Point u[100], l[100];

inline double gao(double w) {
	double ret = 0.0;
	for (int i = 1; i < U; ++i) {
		if (u[i].x < w) {
			ret += (u[i].y + u[i - 1].y) / 2 * (u[i].x - u[i - 1].x);
		} else {
			double y = (u[i].y - u[i - 1].y) / (u[i].x - u[i - 1].x) * (w - u[i - 1].x) + u[i - 1].y;
			ret += (y + u[i - 1].y) / 2 * (w - u[i - 1].x);
			break;
		}
	}
	//printf("ret = %lf\n", ret);
	for (int i = 1; i < L; ++i) {
		if (l[i].x < w) {
			ret -= (l[i].y + l[i - 1].y) / 2 * (l[i].x - l[i - 1].x);
		} else {
			double y = (l[i].y - l[i - 1].y) / (l[i].x - l[i - 1].x) * (w - l[i - 1].x) + l[i - 1].y;
			ret -= (y + l[i - 1].y) / 2 * (w - l[i - 1].x);
			break;
		}
	}
	return ret;
}

int main() {
	scanf("%d", &T);
	for (int caseNum = 1; caseNum <= T; ++caseNum) {
		scanf("%d%d%d%d", &W, &L, &U, &G);
		for (int i = 0; i < L; ++i) {
			scanf("%lf%lf", &l[i].x, &l[i].y);
		}
		for (int i = 0; i < U; ++i) {
			scanf("%lf%lf", &u[i].x, &u[i].y);
		}
		sort(l, l + L);
		sort(u, u + U);
		printf("Case #%d:\n", caseNum);
		double area = gao(W);
		for (int i = 1; i < G; ++i) {
			double w = area / G * i;
			double pl = 0, pr = W;
			for (int j = 0; j < 1000; ++j) {
				double pm = (pl + pr) / 2;
				double cur = gao(pm);
				if (cur < w) {
					pl = pm;
				} else {
					pr = pm;
				}
			}
			printf("%.13lf\n", pr);
		}
	}
	return 0;
}
