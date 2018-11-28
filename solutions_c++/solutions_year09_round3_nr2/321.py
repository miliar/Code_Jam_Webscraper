#include <stdio.h>
#include <math.h>

double x, y, z, vx, vy, vz;
double xx, yy, zz, tx, ty, tz;
double a, b, t, d;
int cs, ct, n;

double sqr(double x)
{
	return x * x;
}

int main()
{
	int i;
	scanf("%d", &cs);
	for (ct = 1; ct <= cs; ct++) {
		scanf("%d", &n);
		xx = yy = zz = tx = ty = tz = 0;
		for (i = 0; i < n; i++) {
			scanf("%lf%lf%lf%lf%lf%lf", &x, &y, &z, &vx, &vy, &vz);
			xx += x;
			yy += y;
			zz += z;
			tx += vx;
			ty += vy;
			tz += vz;
		}
		xx /= n; yy /= n; zz /= n;
		tx /= n; ty /= n; tz /= n;

		a = 2 * (tx * tx + ty * ty + tz * tz);
		b = 2 * (xx * tx + yy * ty + zz * tz);

		t = -b / a;
		if (a == 0 || t < 0) t = 0;
		d = sqrt(sqr(xx + t * tx) + sqr(yy + t * ty) + sqr(zz + t * tz));
		printf("Case #%d: %.8lf %.8lf\n", ct, d, t);



	}	
	return 0;
}
