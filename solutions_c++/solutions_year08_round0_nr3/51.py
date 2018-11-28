#define _CRT_SECURE_NO_DEPRECATE

#include<algorithm>

#include<cstdio>

#include<cstdlib>

#include<iostream>

#include<sstream>

#include<fstream>

#include<map>

#include<vector>

#include<cmath>

using namespace std;

const double pi = acos(-1.0);

const double err = 1e-9;

int testcases;

double f, R, t, r, g;

double dist(double x, double y);

double sqr(double x); 

double cal(double, double, double);


FILE *fin = fopen("C.in", "r");

FILE *fout = fopen("C.out", "w");

int main() {

	fscanf(fin, "%d", &testcases);

	for (int cases = 1; cases <= testcases; cases++) {

		fscanf(fin, "%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g); // need change g to g - 2 f

		if (g <= 2 * f + err) { fprintf(fout, "Case #%d: %.6lf\n", cases, 1.0); continue; }

		if (R <= t + f + err) { fprintf(fout, "Case #%d: %.6lf\n", cases, 1.0); continue; }

		g -= 2 * f;

		r += f;

		t += f;

		double total = pi * R * R;

		double gap = 0;

		for (int i = 0; dist((2 * r + g) * i + r, r) <= R -t ; i++) {

			double x = (2 * r + g) * i + r;

			double y = sqrt(sqr(R - t) - sqr(x) + err);

			int k = (y - r) / (2 * r + g) + err;  // k + 1 

			y = (2 * r + g) * k + r;

			while (k >= 0) {

				if (dist(x + g, y + g) <= R - t + err) { gap += (k + 1) * g * g; break; }

				gap += cal(x, y, R - t);

				--k;

				y -= 2 * r + g;
			}
		}

		gap *= 4;

		fprintf(fout, "Case #%d: %.6lf\n", cases, (total - gap) / total);
	}

	return 0;
}

double dist(double x, double y) {

	return sqrt(x * x + y * y);
}

double sqr(double x) {

	return x * x;
}

double circle(double x1, double y1, double x2, double y2, double r) {

	double a1 = acos(x1 / r);

	double a2 = acos(x2 / r);

    double a = fabs(a2 - a1);

	double ans = r * r * a / 2;

    ans -= r * r * sin(a) / 2;

	return ans;
}


double cal(double x, double y, double r) {

	double x1, y1, x2, y2;


	if (dist(x, y + g) >= r) {

		x1 = x;

		y1 = sqrt(r * r - x1 * x1);
	}

	else {

		y1 = y + g;

		x1 = sqrt(r * r - y1 * y1);
	}


	if (dist(x + g, y) >= r) {


		y2 = y;

		x2 = sqrt(r * r - y2 * y2);
	}

	else {

		x2 = x + g;

		y2 = sqrt(r * r - x2 * x2);
	}


	double ans = circle(x1, y1, x2, y2, r);

	if (dist(x, y + g) >= r && dist(x + g, y) >= r) {

		ans += (y1 - y) * (x2 - x) / 2;
	}

	else if (dist(x, y + g) < r && dist(x + g, y) >= r) {

		ans += (x1 - x + x2 - x) * g / 2;
	}

	else if (dist(x, y + g) >= r && dist(x + g, y) < r) {

		ans += (y1 - y + y2 - y) * g / 2;
	}

	else {

		ans += g * g - (x + g - x1) * (y + g - y2) / 2;
	}

	return ans;
}
