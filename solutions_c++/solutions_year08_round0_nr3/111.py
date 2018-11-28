#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

#define abs(x) (((x) > 0.0) ? (x) : -(x))

const double EPSILON = 1e-9;
double f, R, t, r, g;

double triangle(double x1, double y1, double x2, double y2, double x3, double y3) {
	double p = x1 * y2 + x2 * y3 + x3 * y1;
	p -= (x1 * y3 + x2 * y1 + x3 * y2);
	return abs(p) / 2.0;
}

int main() {
	int Q;
	scanf("%d", &Q);

	for (int cn = 1; cn <= Q; ++cn) {
		scanf("%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);

		int line = 2 + (int)(1.0 * (R - t) / (g + 2 * r));
		double total = M_PI / 4.0 * R * R;
		double empty = 0.0;
		double square = (g - 2 * f) * (g - 2 * f);

		for (int i = 0; i < line; ++i) {
			for (int j = 0; j < line; ++j) {
				double x1 = r + f + i * (g + 2 * r);
				double x2 = g + r - f + i * (g + 2 * r);
				double y1 = r + f + j * (g + 2 * r);
				double y2 = g + r - f + j * (g + 2 * r);

				if (x1 - x2 > -EPSILON) continue;
				if (sqrt(x2 * x2 + y2 * y2) < R - t - f + EPSILON) {
					empty += square;
					continue;
				}
				if (sqrt(x1 * x1 + y1 * y1) > R - t - f + EPSILON) continue;
				int posLeftUp, posRightDown;
				double xa, ya, xb, yb;

				if (sqrt(x1 * x1 + y2 * y2) > R - t - f  - EPSILON) {
					posLeftUp = 1;
					xa = x1, ya = sqrt((R - t - f) * (R - t - f) - x1 * x1);
				} else {
					posLeftUp = 2;
					xa = sqrt((R - t - f ) * (R - t - f ) - y2 * y2), ya = y2;
				}
				if (sqrt(x2 * x2 + y1 * y1) > R - t - f  - EPSILON) {
					posRightDown = 1;
					xb = sqrt((R - t - f ) * (R - t - f ) - y1 * y1), yb = y1;
				} else {
					posRightDown = 2;
					xb = x2, yb = sqrt((R - t - f ) * (R - t - f) - x2 * x2);
				}

				double angle1 = atan2(xa, ya);
				double angle2 = atan2(xb, yb);

				switch (posLeftUp * 2 + posRightDown) {
					case 3:
						empty += (xb - xa) * (ya - yb) / 2.0;
						empty += 0.5 * (R - t - f) * (R - t - f) * (angle2 - angle1);
						empty -= triangle(0, 0, xa, ya, xb, yb);
						break;
					case 4:
						empty += (x2 - x1) * (ya + yb - 2 * y1) / 2.0;
						empty += 0.5 * (R - t - f) * (R - t - f) * (angle2 - angle1);
						empty -= triangle(0, 0, xa, ya, xb, yb);
						break;
					case 5:
						empty += (y2 - y1) * (xa + xb - 2 * x1) / 2.0;
						empty += 0.5 * (R - t - f) * (R - t - f) * (angle2 - angle1);
						empty -= triangle(0, 0, xa, ya, xb, yb);
						break;
					case 6:
						empty += square;
						empty -= (x2 - xa) * (y2 - yb) / 2.0;
						empty += 0.5 * (R - t - f) * (R - t - f) * (angle2 - angle1);
						empty -= triangle(0, 0, xa, ya, xb, yb);
						break;
				}
			}
		}
		printf("Case #%d: %.8lf\n", cn, 1.0 - empty / total);
	}
}

