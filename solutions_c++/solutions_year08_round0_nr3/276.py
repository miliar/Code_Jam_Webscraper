#include <stdio.h>
#include <math.h>
#include <assert.h>
#include <algorithm>
using namespace std;

const double eps = 1e-7;

int main() {
	int tc;
	scanf("%d", &tc);
	for (int x=1; x<=tc; ++x) {
		double f, R, t, r, g;
		scanf("%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);
		if (2*f >= g) {
			printf("Case #%d: %.6lf\n", x, 1.0);
			continue;
		}
		// determine number of strings in one direction in one quarter
		int k = (int)floor((R - t - r) / (2*r + g));
		t += f;
		double area = 0;
		for (int i=0; i<=k; ++i) {
			double xl = i * (2*r + g) + r + f;
			double xu = xl + g - 2*f;
			for (int j=0; j<=k; ++j) {
				double yl = j * (2*r + g) + r + f;
				if (xl * xl + yl * yl >= (R - t) * (R - t))
					break;
				double yu = yl + g - 2*f;
				if (xu * xu + yu * yu <= (R - t) * (R - t)) {
					area += (g - 2*f) * (g - 2*f) * 2;
					continue;
				}
				double x1, y1, x2, y2;
				if (xu * xu + yl * yl >= (R - t) * (R - t)) {
					x1 = sqrt((R-t)*(R-t) - yl*yl);
					assert(x1 >= xl && x1 <= xu);
					y1 = yl;
				}
				else {
					x1 = xu;
					y1 = sqrt((R-t)*(R-t) - xu*xu);
					assert(y1 >= yl && y1 <= yu);
					double tx = yl * (x1 / y1);
					if (tx < xl) {
						double ty = xl * (y1 / x1);
						assert(ty >= yl && ty <= yu);
						area -= (ty - yl) * (xl - tx);
					}
					else
						assert(tx >= xl && tx <= xu);
					area += (y1 - yl) * (xu - tx);
				}
				assert(fabs(x1*x1+y1*y1 - (R-t)*(R-t)) < eps);
				if (xl * xl + yu * yu >= (R - t) * (R -t)) {
					x2 = xl;
					y2 = sqrt((R-t)*(R-t) - xl*xl);
					assert(y2 >= yl && y2 <= yu);
				}
				else {
					y2 = yu;
					x2 = sqrt((R-t)*(R-t) - yu*yu);
					assert(x2 >= xl && x2 <= xu);
					double ty = xl * (y2 / x2);
					if (ty < yl) {
						double tx = yl * (x2 / y2);
						assert(tx >= xl && tx <= xu);
						area -= (tx - xl) * (yl - ty);
					}
					else
						assert(ty >= yl && ty <= yu);
					area += (x2 - xl) * (yu - ty);
				}
				assert(fabs(x2*x2+y2*y2 - (R-t)*(R-t)) < eps);
				assert(y2 * x1 >= y1 * x2);
				double phi1 = atan(y1 / x1);
				double phi2 = atan(y2 / x2);
				double phi = phi2 - phi1;
				assert(phi >= 0);
				if (xl * y1 >= yl * x1) {
					double temp = phi * (R-t) * (R-t) - sin(phi) * (xl / cos(phi1)) * (xl / cos(phi2));
					assert(temp >= 0);
					area += temp;
					continue;
				}
				double temp = phi * (R-t) * (R-t) - sin(phi) * (yl/sin(phi1)) * (yl/sin(phi2));
				if (xl * y2 > yl * x2) {
					double tx = yl * x2 / y2;
					double ty = xl * y2 / x2;
					assert(tx <= xl);
					assert(ty >= yl && ty <= yu);
					temp -= (ty - yl) * (xl - tx);
				}
				assert(temp >= 0);
				area += temp;
			}
		}
		printf("Case #%d: %.6lf\n", x, 1.0 - area/(R*R*acos(0.0)));
	}
	return 0;
}
