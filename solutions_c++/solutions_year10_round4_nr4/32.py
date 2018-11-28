#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;

const double PI = acos(-1.0);

double ret[123];

int x[2], y[2];

double dis(double x1, double y1, double x2, double y2)
{
	double dx = x1 - x2;
	double dy = y1 - y2;
	return sqrt(dx * dx + dy * dy);
}

double gogo(double th)
{
	return min(max(th, -1.0), 1.0);
}

double go(int xx, int yy)
{
	if (x[0] == x[1] && y[0] == y[1]) {
		double d = dis(x[0], y[0], xx, yy);
		return PI * d * d;
	}
	if (xx == x[0] && yy == y[0]) {
		return 0;
	}
	if (xx == x[1] && yy == y[1]) {
		return 0;
	}
	double d1 = dis(x[0], y[0], x[1], y[1]);
	double d2 = dis(x[0], y[0], xx, yy);
	double d3 = dis(x[1], y[1], xx, yy);
	double th = acos(gogo((d2 * d2 + d1 * d1 - d3 * d3) / (2 * d2 * d1)));
	double ret = th * d2 * d2;
	double a = d2 * sin(th) * d2 * cos(th);
	ret -= a;
	double th2 = acos(gogo((d3 * d3 + d1 * d1 - d2 * d2) / (2 * d3 * d1)));
	double ret2 = th2 * d3 * d3;
	double a2 = d3 * sin(th2) * d3 * cos(th2);
	ret2 -= a2;
	return ret + ret2;
}

int run()
{
	int n, m;
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; ++i) {
		scanf("%d %d", x + i, y + i);
	}
	int xx, yy;
	for (int i = 0; i < m; ++i) {
		scanf("%d %d", &xx, &yy);
		ret[i] = go(xx, yy);
	}
	return m;
}

int main()
{
	freopen("D1.in", "r", stdin);
	freopen("D1.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		int n = run();
		printf("Case #%d:", i);
		for (int j = 0; j < n; ++j) {
			printf(" %.10lf", ret[j]);
		}
		puts("");
	}
	return 0;
}