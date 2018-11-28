/*
FROM: GCJ (Google Code Jam) Qualification Round 2008
PROB: B Train Timetable
KEYW: greedy, heap

LANG: GNU C++ (g++ (GCC) 4.3.1 20080612 (Red Hat 4.3.1-2))
OPT: -lm -O2
*/

#include <cstdio>
#include <cmath>
#include <cassert>

const double EPS = 1e-9;

double rx;//R - t - f
//\int sqrt (rx*rx - x*x) dx from l to u
double integr (double l, double u) {
	return (u * sqrt (rx * rx - u * u)
		  - l * sqrt (rx * rx - l * l)
		  + rx * rx * asin (u / rx)
		  - rx * rx * asin (l / rx)) / 2.;
}

void test_integr () {
	rx = 10.;
	double s1 = integr (0, rx) * 4;
	double s2 = M_PI * rx * rx;
	printf ("%lf %lf\n", s1, s2);
	assert (fabs (s1 - s2) < 1e-6);
	//IT WORKS :) :) 3x huray for mathematics
}

bool in_cir (double x, double y) {
	return hypot (x, y) < rx + EPS;
}

double get_x_intersect (double y) {
	return sqrt (rx * rx - y * y);
}

int _type;
double f, R, t, r, g;
double calc (int x, int y) {
	double lx, ly, ux, uy;
	lx = (2. * r + g) * x + r + f;
	ly = (2. * r + g) * y + r + f;
	ux = (2. * r + g) * x + r + g - f;
	uy = (2. * r + g) * y + r + g - f;

	if (in_cir (ux, uy)) {
		_type = 0;//whole is in
		return (g - 2. * f) * (g - 2. * f);
	}
	if (!in_cir (lx, ly)) {
		_type = 1;//whole is out
		return 0.;
	}

	_type = 2;//somewhere in between
	if (in_cir (lx, uy) && in_cir (ux, ly)) {
		double cx = get_x_intersect (uy);
		return (cx - lx) * (uy - ly)
			+ integr (cx, ux) - ly * (ux - cx);
	}

	if (in_cir (lx, uy)) {
		double cx1 = get_x_intersect (uy);
		double cx2 = get_x_intersect (ly);
		return (cx1 - lx) * (uy - ly)
			+ integr (cx1, cx2) - ly * (cx2 - cx1);
	}

	if (in_cir (ux, ly)) {
		return integr (lx, ux) - ly * (ux - lx);
	}

	//only lx ly is in
	double cx = get_x_intersect (ly);
	return integr (lx, cx) - ly * (cx - lx);
}

int main () {
	int tc;
	scanf ("%d", &tc);

	for (int ctc = 1; ctc <= tc; ++ctc) {
		scanf ("%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);
		rx = R - t - f;

		//there is certainly room for improvement here
		double tot = 0;
		for (int x = 0;; ++x) {
			tot += calc (x, 0);
			if (_type == 1)
				break;
			for (int y = 1;; ++y) {
				tot += calc (x, y);
				if (_type == 1)
					break;
			}
		}

		printf ("Case #%d: %lf\n", ctc, 1. - (4. * tot) / (M_PI * R * R));
	}

	return 0;
}
