#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

int tests, n, m;
long double x[100], y[100], pi = 2.0 * acosl(0.0);

long double dist(long double a, long double b, long double c, long double d) {
	return sqrtl(powl(a - c, 2.0) + powl(b - d, 2.0));
}

int main() {
	scanf("%d", &tests);
	for (int tc = 1; tc <= tests; tc++) {
		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; i++)
			scanf("%Lf %Lf", &x[i], &y[i]);
		long double x0 = x[0], y0 = y[0];
		long double x1 = x[1], y1 = y[1];
		long double d = dist(x0, y0, x1, y1);
		printf("Case #%d:", tc);
		for (int i = 0; i < m; i++) {
			long double wx, wy;
			scanf("%Lf %Lf", &wx, &wy);
			long double r = dist(x0, y0, wx, wy);
			long double R = dist(x1, y1, wx, wy);
			if (R < r) swap(R, r);
			long double ans;
			if (d > r + R) ans = 0.0; // shouldn't happen
			else if (d < R - r) ans = pi * r * r;
			else ans = r*r*acos((d*d+r*r-R*R)/(2*d*r))+R*R*acos((d*d+R*R-r*r)/(2*d*R))-
					0.5*sqrt((-d+r+R)*(d+r-R)*(d-r+R)*(d+r+R));
			printf(" %.9Lf", ans);
		}
		printf("\n");
	}
	return 0;
}