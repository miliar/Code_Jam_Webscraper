#include <stdio.h>
#include <math.h>

#define pi 3.1415926535897932384626433832795

int N, n;
double f, R, t, r, g;
double emptySquare;
double fillSquare;
double X1, X2, Y1, Y2;
double h;

double Tsquare(double x1, double x2, double R)
{
  double v1 = 0.5 * (x1 * sqrt(R*R - x1*x1) + R*R * asin(x1 / R));
  double v2 = 0.5 * (x2 * sqrt(R*R - x2*x2) + R*R * asin(x2 / R));

  return v2 - v1;
}

int main() {

	//FILE *in = fopen("C-small.in", "rt");
	//FILE *out = fopen("C-small.out", "wt");

	FILE *in = fopen("C-large.in", "rt");
	FILE *out = fopen("C-large.out", "wt");

	fscanf(in, "%d", &N);

	for (n = 1; n <= N; n++) {
		fscanf(in, "%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);

		if (2*f >= g) {
			fprintf(out, "Case #%d: %lf\n", n, 1.0);
			continue;
		}

		fillSquare = pi * R * R / 4;
		
		R = R - t - f;
		r = r + f;
		g = g - 2.0 * f;

		emptySquare = 0;

		X1 = r;
		while (X1 < R) {
			X2 = X1 + g;
			Y1 = r;
			while (1) {
				if (X1 * X1 + Y1 * Y1 >= R * R) break;
				Y2 = Y1 + g;
				if (X2 * X2 + Y2 * Y2 <= R * R) {
					emptySquare += g*g;
				} else {
					if (R * R - X1 * X1 > Y2 * Y2) {
						if (R * R - Y1 * Y1 > X2 * X2) {
							double x_b = sqrt(R * R - Y2 * Y2);
							double x_e = X2;
							emptySquare += (x_b - X1) * g;
							emptySquare += (Tsquare(x_b, x_e, R) - Y1 * (x_e - x_b));
						} else {
							double x_b = sqrt(R * R - Y2 * Y2);
							double x_e = sqrt(R * R - Y1 * Y1);
							emptySquare += (x_b - X1) * g;
							emptySquare += (Tsquare(x_b, x_e, R) - Y1 * (x_e - x_b));
						}
					} else {
						if (R * R - Y1 * Y1 > X2*X2) {
							emptySquare += (Tsquare(X1, X2, R) - Y1 * g);
						} else {
							double x_b = X1;
							double x_e = sqrt(R*R - Y1*Y1);
							emptySquare += (Tsquare(x_b, x_e, R) - Y1 * (x_e - x_b));
						}
					}
				}
				Y1 = Y1 + g + 2 * r;
			}
			X1 = X1 + g + 2 * r;
		}

		fprintf(out, "Case #%d: %lf\n", n, 1.0 - emptySquare/fillSquare);
	}
	
	fclose(in);
	fclose(out);

	return 0;
}