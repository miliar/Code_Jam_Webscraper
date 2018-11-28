#include <stdio.h>
#include <math.h>
#define SQR(x) ((x)*(x))
double f, R, t, r, g;
int main() {
	int N;
	scanf("%d", &N);
	for (int _42 = 1; _42 <= N; _42++) {
		printf("Case #%d: ", _42);
		scanf("%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);
		if (R - t - r <= f || g <= f) {
			printf("1.000000\n");
			continue;
		}
		t += f;
		r += f;
		g -= 2*f;
		double drg = 2.*r+g;
		double area = 0.;
		for (double y = r; y < R - t; y += drg) {
			double k = sqrt(SQR(R-t) - SQR(y+g));
			if (isnan(k))
				k = 0.;
			double kk = sqrt(SQR(R-t) - SQR(y));
			if (isnan(kk))
				kk = 0.;
			double temp = floor((k + r)/drg);
			area += temp*g*g;
			int p1, p2;
			double P1x, P1y, P2x, P2y;
			double theta1, theta2;
			for (double x = temp*drg + r; x <= kk; x += drg) {
				if (k - x >= 0) {
					p1 = 0;
					P1y = y+g;
					P1x = k;
				} else {
					p1 = 1;
					P1y = sqrt(SQR(R-t) - SQR(x));
					P1x = x;
				}
				if (kk - x <= g) {
					p2 = 0;
					P2x = kk;
					P2y = y;
				} else {
					p2 = 1;
					P2y = sqrt(SQR(R-t) - SQR(x+g));
					P2x = x+g;
				}
				if (p1 == 0)
					area += (P1x-x)*g;
				if (p2 == 1)
					area += (P2y-y)*g;
				if (p1 == 0 && p2 == 1)
					area -= (P1x-x)*(P2y-y);
				theta1 = atan2(P1y, P1x);
				theta2 = atan2(P2y, P2x);
				area += (P1y - P2y)*(P2x - P1x)/2;
				double theta = theta1 - theta2;
				area += SQR(R-t)*(theta - sin(theta))/2.;
			}
		}
		area *= 4;
		double r = (M_PI*SQR(R) - area)/(M_PI*SQR(R));
		printf("%.6lf\n", r);
	}
	return 0;
}
