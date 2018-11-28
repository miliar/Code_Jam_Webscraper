#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

#define sz(a) ((int)((a).size()))
#define sqr(a) ((a)*(a))
#define eps (1e-9)
typedef pair<int, int> ii;
typedef long long LL;

struct pt {
	double x, y, r;
	pt(double X, double Y, double R) { x = X; y = Y; r = R; }
};

double dist(double x1, double y1, double x2, double y2) {
	return sqrt(sqr(x1 - x2) + sqr(y1 - y2));
}

pt go(double x1, double y1, double r1, double x2, double y2, double r2) {
	double d = dist(x1, y1, x2, y2);
	if (r1 > d + r2 - eps) return pt(x1, y1, r1);
	if (r2 > d + r1 - eps) return pt(x2, y2, r2);
	double c = (d + r1 - r2) / 2.0;
	return pt(c * x1 + (1 - c) * x2, c * y1 + (1 - c) * y2, (d + r1 + r2) / 2.0);
}

int main() {
	freopen("D.in", "rt", stdin);
	freopen("D.out", "wt", stdout);
	int tests;
	scanf("%d\n", &tests);
	for (int test = 1; test <= tests; test++) {
		int n;
		scanf("%d", &n);
		double X[3], Y[3], R[3];
		for (int i = 0; i < n; i++) scanf("%lf%lf%lf", &X[i], &Y[i], &R[i]);
		double ans = 1e100;
		if (n == 1) {
			ans = R[0];
		} else if (n == 2) {
			ans = max(R[0], R[1]);
		} else if (n == 3) {
			pt ans0 = go(X[1], Y[1], R[1], X[2], Y[2], R[2]);
			pt ans1 = go(X[2], Y[2], R[2], X[0], Y[0], R[0]);
			pt ans2 = go(X[0], Y[0], R[0], X[1], Y[1], R[1]);
			ans = min(ans, max(ans0.r, R[0]));
			ans = min(ans, max(ans1.r, R[1]));
			ans = min(ans, max(ans2.r, R[2]));
		} else ans = -1;
		printf("Case #%d: %.6lf\n", test, ans);
	}
	return 0;
}
