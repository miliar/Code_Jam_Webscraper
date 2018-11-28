#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

#define SQR(a) ((a)*(a))
#define EPSILON 1e-9
#define PI (4*atan(1))

int main() {
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; ++tt) {
		int n, m;
		scanf("%d %d", &n, &m);

		long double x1, y1, x2, y2;
		scanf("%Lf %Lf %Lf %Lf", &x1, &y1, &x2, &y2);

		long double d = sqrt(SQR(x2-x1) + SQR(y2-y1));

		printf("Case #%d:", tt);

		long double xq, yq;
		for (int i = 0; i < m; ++i) {
			scanf("%Lf %Lf", &xq, &yq);

			long double res = 0;

			long double r = sqrt(SQR(xq-x1) + SQR(yq-y1));
			long double R = sqrt(SQR(xq-x2) + SQR(yq-y2));

			if (fabs(d-r-R) < EPSILON) {
				res = 0;
			} else {
				res = r*r*acos((d*d+r*r-R*R)/(2*d*r))
			        + R*R*acos((d*d+R*R-r*r)/(2*d*R))
			        - sqrt( (-d+r+R)*(d+r-R)*(d-r+R)*(d+r+R) )/2;
			}

			printf(" %.7Lf", res);
		}
		printf("\n");
	}
}
