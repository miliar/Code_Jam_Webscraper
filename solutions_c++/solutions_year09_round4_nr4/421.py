#include <cmath>
#include <algorithm>
#include <cstdio>
using namespace std;

double dist(double x1, double y1, double x2, double y2) {
	return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
}

int main() {
	int t, n;

	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		scanf("%d", &n);
		if (n == 1) {
			double x, y, r;
			scanf("%lf %lf %lf", &x, &y, &r);
			printf("Case %d: %.6lf\n", i+1, r);
		}
		else if (n == 2) {
			double x1, y1, r1, x2, y2, r2;
			scanf("%lf %lf %lf %lf %lf %lf", &x1, &y1, &r1, &x2, &y2, &r2);
			printf("Case %d: %.6lf\n", i+1, max(r1, r2));
		}
		else if (n == 3) {
			double x1, y1, r1, x2, y2, r2, x3, y3, r3;
			scanf("%lf %lf %lf %lf %lf %lf %lf %lf %lf", &x1, &y1, &r1,
					&x2, &y2, &r2, &x3, &y3, &r3);

			double r12 = (dist(x1,y1,x2,y2) + r1 + r2) / 2;
			double r13 = (dist(x1,y1,x3,y3) + r1 + r3) / 2;
			double r23 = (dist(x2,y2,x3,y3) + r2 + r3) / 2;

			double t1 = max(r12, r3);
			double t2 = max(r13, r2);
			double t3 = max(r23, r1);
			printf("Case #%d: %.6lf\n", i+1, min(min(t1,t2),t3));
		}
	}
}

