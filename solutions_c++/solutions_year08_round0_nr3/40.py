#include <stdio.h>
#include <string.h>
#include <math.h>

double pi = acos(-1.0);

double f, r, t, R, g;

bool inCircle(double x, double y, double R) {
	return x * x + y * y <= R * R;
}

double func(double R, double t) {
	return sqrt(R * R - t * t);
}

double func2(double R, double x) {
	if (x > R - 1e-10) {
		return pi / 2;
	}
	return atan(x / func(R, x));
}

double area(double R, double x1, double x2, double y) {
//	return (x2 * func(R, x2) - x1 * func(R, x1) + R * R * (func2(R, x2) - func2(R, x1))) / 2 - (x2 - x1) * y;
	double t = (x2 * func(R, x2) - x1 * func(R, x1) + R * R * (func2(R, x2) - func2(R, x1))) / 2 - (x2 - x1) * y;
	double y1 = func(R, x1);
	double y2 = func(R, x2);
	double x = x1 * y2 / y1;
	double t2 = R * R * (acos(x1 / R) - acos(x2 / R)) / 2 - (x2 - x) * y2 / 2 - (x1 - x) * (y1 - y2) / 2 + (y2 - y) * (x2 - x1);
	return t2;
}

double getArea(double x, double y, double l) {
	if (inCircle(x + l, y + l, R)) return l * l;
	double t1, t2;
	if (inCircle(x, y + l, R)) {
		if (inCircle(x + l, y, R)) {
			t1 = func(R, y + l);
			t2 = func(R, x + l);
			return (t2 - y) * l + (t1 - x) * (y + l - t2) + area(R, t1, x + l, t2);
		}
		else {
			t1 = func(R, y + l);
			t2 = func(R, y);
			return (t1 - x) * l + area(R, t1, t2, y);
		}
	}
	else {
		if (inCircle(x + l, y, R)) {
			return area(R, x, x + l, y);
		}
		else {
			t2 = func(R, y);
			return area(R, x, t2, y);
		}
	}
	return 0;
}

double getProb() {
	double p = 0, total;
	if (R - t - f < 1e-8) return 1;
	total = pi * R * R;
	r += f;
	g -= 2 * f;
	if (g < 1e-8) return 1;
	R -= t + f;
	double x, y, tx, ty;
	x = y = r;
	while (inCircle(x, y, R)) {
		tx = x;
		ty = y;
		while (inCircle(tx, ty, R)) {
			p += getArea(tx, ty, g);
			ty += g + 2 * r;
		}
		x += g + 2 * r;
	}
	return 1 - 4 * p / total;
}

int main() {
	freopen("C.in", "r", stdin);
	freopen("C.out","w",stdout);
	int testcases, k;
	scanf("%d", &testcases);
	for (k = 0; k < testcases; k++) {
		scanf("%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);
		printf("Case #%d: %.9lf\n", k + 1, getProb());
	}
	return 0;
}
