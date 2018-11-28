#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

double x, y, z, vx, vy, vz;
double a1, b1, a2, b2, a3, b3;
int N;

int main() {
	freopen("F:\\B-large.in", "r", stdin);
	freopen("F:\\B-large.out", "w", stdout);
	int T, i, cas = 0;
	double t, d;
	scanf("%d", &T);
	while (T--) {
		scanf("%d", &N);
		double a = 0, b = 0, c = 0;
		a1 = b1 = a2 = b2 = a3 = b3 = 0;
		for (i = 0; i < N; ++i) {
			scanf("%lf%lf%lf%lf%lf%lf", &x, &y, &z, &vx, &vy, &vz);
			//a += vx * vx + vy * vy + vz * vz;
			//b += 2 * x * vx + 2 * y * vy + 2 * z * vz;
			//c += x
			a1 += x;
			b1 += vx;
			a2 += y;
			b2 += vy;
			a3 += z;
			b3 += vz;
		}
		a1 /= N;
		b1 /= N;
		a2 /= N;
		b2 /= N;
		a3 /= N;
		b3 /= N;

		a += b1 * b1 + b2 * b2 + b3 * b3;
		b += 2 * a1 * b1 + 2 * a2 * b2 + 2 * a3 * b3;
		c += a1 * a1 + a2 * a2 + a3 * a3;

		if (a < 0) {
			a = -a;
			b = -b;
			c = -c;
		}

		if (fabs(a) < 1e-6) t = 0;
		else t = -b / (2 * a);

		if (t < 0) t = 0;
		d = a * t * t + b * t + c;

		if (d < 0) d = -d;
		//printf("d = %lf\n", d);
		printf("Case #%d: %.8lf %.8lf\n", ++cas, sqrt(d), t);
	}
	return 0;
}

