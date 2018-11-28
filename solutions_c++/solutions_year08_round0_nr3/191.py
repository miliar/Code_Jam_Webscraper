#include <cstdio>
#include <cmath>
#include <algorithm>

#define pi 2.0 * acos(0.0)
#define eps 1.0e-9

using namespace std;

FILE *fp_r, *fp_w;
int t;
int i, j, k;
double p;
double fr, rr, d, rb, lb, d2;
double a, b;
double r, area, h, w;
int c;
double px1, py1, px2, py2;

double dist(double _x1, double _y1, double _x2, double _y2) {
	return sqrt((_x1 - _x2) * (_x1 - _x2) + (_y1 - _y2) * (_y1 - _y2));
}

int main() {

	fp_r = fopen("C-large.in", "r");
	fp_w = fopen("C.out", "w");

	fscanf(fp_r, "%d", &t);
	for(i = 0; i < t; i++) {
		fscanf(fp_r, "%lf %lf %lf %lf %lf", &fr, &rr, &rb, &lb, &d);

		a = 0.0;
		b = pi * rr * rr / 4.0;
		r = rr - rb - fr;

		if (d - 2.0 * fr < 0.0) 
			p = 1.0;
		else {
			d = max(0.0, d - 2.0 * fr);
			lb += fr;

			c = (int)(floor(r / (d + lb * 2.0)) + eps);

			for(j = 0; j <= c; j++) {
				w = lb + d + (d + lb * 2.0) * j;
				for(k = 0; k <= c; k++) {
					h = lb + d + (d + lb * 2.0) * k;
					if (sqrt(w * w + h * h) <= r)
						a += d * d;
					else if (sqrt((w-d) * (w-d) + (h-d) * (h-d)) <= r) {
						px1 = w - d;
						py1 = sqrt(r * r - px1 * px1);
						py2 = h - d;
						px2 = sqrt(r * r - py2 * py2);

						int flag = 0;

						if (fabs(py1 - (h-d)) > d) {
							flag++;
							py1 = h;
							px1 = sqrt(r * r - py1 * py1);
						}
						if (fabs(px2 - (w-d)) > d) {
							flag += 2;
							px2 = w;
							py2 = sqrt(r * r - px2 * px2);
						}

						double _d = dist(px1, py1, px2, py2);
						double ang = acos((2.0 * r * r - _d * _d) / (2.0 * r * r));
						double s = r + _d / 2.0;

						a += r * r * ang / 2.0 - sqrt(s * (s - r) * (s - r) * (s - _d));

						switch(flag) {
							case 3:
								a += d * d - (w - px1) * (h - py2) / 2.0;
								break;
							case 1:
								a += (px1 - w + d + px2 - w + d) * d / 2.0;
								break;
							case 2:
								a += (py1 - h + d + py2 - h + d) * d / 2.0;
								break;
							case 0:
								a += fabs(px2 - (w-d)) * fabs(py1 - (h-d)) / 2.0;
								break;
						}
					}
				}
			}

			p = 1.0 - a / b;
		}
		fprintf(fp_w, "Case #%d: %lf\n", i+1, p);
	}

	fclose(fp_w);
	fclose(fp_r);

	return 0;
}