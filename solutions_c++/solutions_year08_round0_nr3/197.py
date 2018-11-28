#include <stdio.h>
#include <math.h>
#define E 0.0000000001
int i, j, k, tt, T;

double f, R, t, r, g, s, c, res;
double pi;

double x, y, z;

double fp(double x) {
	return (x * sqrt(R*R - x*x) + R*R * asin(x / R) ) / 2.0;
}
double fn(double x) {
	if (x <= 0) {
		return 0;
	}
	return sqrt(R*R - x*x);
}

double gets(double x1, double y1, double x2, double y2) {
	double x, y, z;
	if (x1*x1 + y1 * y1 >= R*R) {
		return 0;
	}
	if (x2*x2 + y2 * y2 <= R*R) {
		return (y2 - y1) * (x2 - x1);
	}
	
	if (x1 * x1 + y2 * y2 >= R*R - 0.0001) {
		if (x2*x2 + y1*y1 < R*R) {
			x = fp(x2) - fp(x1);
			y = (x2 - x1) * y1;
			return x - y;
		} else {
			x2 = fn(y1);
			x = fp(x2);
			x -= fp(x1);
			y = (x2 - x1) * y1;
			return x - y;
		}
	} else {
		z = fn(y2);
		x = (z - x1) * (y2 - y1);
		y = gets(z, y1, x2, y2);
		return x + y;
	}
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	pi = 2 * acos(0.0);
	scanf("%d", &T);
	for (tt = 1; tt <= T; tt ++) {
		scanf("%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g);
		s = pi * R * R;
		R = R - t - f;
		r += f;
		g -= f + f;
		if (g <= 0) {
			printf("Case #%d: 1.00000000\n", tt);
			continue;
		}
		c = 0;
		for (x = r; x <= R; x += r + r + g) {
			for (y = r; y <= R; y += r + r + g) {
				z = gets(x, y, x + g, y + g);
				if (z == 0) {
					break;
				}
				c += z;
			}
		}
		c *= 4;
		c = s - c;
		res = c / s;

		printf("Case #%d: %.8lf\n", tt, res);
	}
	return 0;
}


