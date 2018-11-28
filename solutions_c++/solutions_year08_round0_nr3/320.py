#include <stdio.h>
#include <math.h>

#define PI 3.14159265358979323846
#define SQRT1_2 0.707106781186547524401

int n;
double f, R, t, r, g;

double seg(double c) {
	return R * R * asin(c * 0.5 / R) - c * sqrt(R * R - c * c * 0.25) * 0.5;
}

int main() {
	FILE * fin = fopen("Fly Swatter.in", "r"), * fout = fopen("Fly Swatter.out", "w");
	int k, i, j;
	double p, a, x1, x2, x;
	fscanf(fin, "%d", &n);
	for (k = 1; k <= n; ++k) {
		fscanf(fin, "%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g);
		g -= f * 2;
		if (g > 0) {
			p = 0;
			a = PI * R * R * 0.125;
			r += f;
			R -= t + f;
			f = g + r * 2;
			t = R * SQRT1_2 - r - g;
			for (i = 0; i * f < t; ++i) {
				x1 = sqrt(R * R - (i * f + r) * (i * f + r));
				x2 = sqrt(R * R - (i * f + r + g) * (i * f + r + g));
				j = (int)((x2 + r) / f);
				p += (j - i - 1) * g * g;
				if (j * f + r >= x2) {
					if (j * f + r < x1) {
						x = sqrt(R * R - (j * f + r) * (j * f + r)) - i * f - r;
						x1 -= j * f + r;
						p += x * x1 * 0.5;
						p += seg(sqrt(x * x + x1 * x1));
					}
				} else {
					if (j * f + r + g >= x1) {
						p += g * ((x1 + x2) * 0.5 - j * f - r);
						p += seg(sqrt(g * g + (x1 - x2) * (x1 - x2)));
					} else {
						p += g * (x2 - j * f - r);
						x = sqrt(R * R - (j * f + r + g) * (j * f + r + g)) - i * f - r;
						p += (j * f + r + g - x2) * (x + g) * 0.5;
						p += seg(sqrt((g - x) * (g - x) + (j * f + r + g - x2) * (j * f + r + g - x2)));
						++j;
						if (j * f + r < x1) {
							x = sqrt(R * R - (j * f + r) * (j * f + r)) - i * f - r;
							x1 -= j * f + r;
							p += x * x1 * 0.5;
							p += seg(sqrt(x * x + x1 * x1));
						}
					}
				}
			}
			p += i * g * g * 0.5;
			t += g + r;
			if (i * f + r < t) {
				x1 = sqrt(R * R - (i * f + r) * (i * f + r));
				if (i * f + r + g >= x1) {
					p += (x1 - i * f - r) * (t - i * f - r) * 0.5;
					p += seg(sqrt((x1 - t) * (x1 - t) + (t - i * f - r) * (t - i * f - r)));
				} else {
					p += (t - i * f - r) * (t - i * f - r) * 0.5;
					x = sqrt(R * R - (i * f + r + g) * (i * f + r + g)) - i * f - r;
					p += (i * f + r + g - t) * (x + t - i * f - r) * 0.5;
					p += seg(sqrt((t - i * f - r - x) * (t - i * f - r - x) + (i * f + r + g - t) * (i * f + r + g - t)));
					j = i + 1;
					if (j * f + r < x1) {
						x = sqrt(R * R - (j * f + r) * (j * f + r)) - i * f - r;
						x1 -= j * f + r;
						p += x * x1 * 0.5;
						p += seg(sqrt(x * x + x1 * x1));
					}
				}
			}
			fprintf(fout, "Case #%d: %.6f\n", k, 1 - p / a);
		} else {
			fprintf(fout, "Case #%d: 1.000000\n", k);
		}
	}
	return 0;
}