#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <map>
#include <algorithm>

using namespace std;

string readLine() {
	char sz[1000];
	fgets(sz, 1000, stdin);
	int l = strlen(sz);
	if (sz[l-1] == '\n') sz[l-1] = 0;
	return sz;
}

int readIntLine() {
	string s = readLine();
	return atoi(s.c_str());
}

#define PI 3.14159265358979

double csecArea(double R, double c) {
	double a = 2*asin(c/(2*R)), h = sqrt(R*R-(c/2)*(c/2));

	return a*R*R/2 - c*h/2;
}

double rtriArea(double R, double x0, double y0, double x1, double y1) {
	return csecArea(R, sqrt((x0-x1)*(x0-x1) + (y0-y1)*(y0-y1))) +
		fabs(x0-x1)*fabs(y0-y1)/2;
}

double rAxx(double R, double x0, double x1) {
	return rtriArea(R, x0, sqrt(R*R-x0*x0), x1, sqrt(R*R-x1*x1));
}
double rAxy(double R, double x0, double y1) {
	return rtriArea(R, x0, sqrt(R*R-x0*x0), sqrt(R*R-y1*y1), y1);
}
double rAyy(double R, double y0, double y1) {
	return rAxx(R, y0, y1);
}

double solveIt(double f, double R, double t, double r, double g) {
	if (r+t+f >= R || g <= 2*f) return 1.0;

	double aa = PI*R*R;

	r += f;
	t += f;
	R -= t;
	g -= 2*f;

	double g2r = g+2*r;

	double sa = 0.0;

// x0: r, 3r+g, 5r+2g, 7r+4g ...
//     0,  g2r, 2*g2r, 3*g2r ...

	int ct = 0;
	for (double y0 = r; y0 < R; y0 += g2r) {
		double y1 = y0+g;
		for (double x0 = r; x0 < R; x0 += g2r) {
			ct++;
			double x1 = x0+g;
			if (x0*x0+y0*y0 >= R*R) break;
			if (x1*x1+y1*y1 <= R*R) {
				sa += g*g;
				continue;
			}

			double ba = 0.0, ca = 0.0;
			if (x1*x1+y0*y0 > R*R) {
				if (x0*x0+y1*y1 > R*R) {
					ba = rAxy(R, x0, y0);
//printf("R %.6lf, x0 %.6lf, y0 %.6lf\n", R, x0, y0);
				} else {
					ba = rAyy(R, y0, y1);
					double x2 = sqrt(R*R-y1*y1);
					ca = (x2-x0)*g;
				}
			} else {
				if (x0*x0+y1*y1 > R*R) {
					ba = rAxx(R, x0, x1);
					double y2 = sqrt(R*R-x1*x1);
					ca = (y2-y0)*g;
				} else {
					ba = rAxy(R, x1, y1);
					double x2 = sqrt(R*R-y1*y1),
						y2 = sqrt(R*R-x1*x1);
					ca = (x2-x0)*g + (y2-y0)*g -
						(x2-x0)*(y2-y0);
				}
			}
//			printf("ba %.6lf, ca %.6lf\n", ba, ca);

			sa += ba+ca;
		}
	}
	sa *= 4;
	return (aa-sa)/aa;
}

int main() {
	int N = readIntLine();
	for (int cn = 1; cn <= N; cn++) {
		double f, R, t, r, g;

		scanf("%lf %lf %lf %lf %lf ", &f, &R, &t, &r, &g);

		double res = solveIt(f, R, t, r, g);

		printf("Case #%d: %.8lf\n", cn, res);
	}
	return 0;
}

