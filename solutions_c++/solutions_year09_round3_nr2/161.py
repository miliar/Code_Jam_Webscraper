#include <stdio.h>
#include <math.h>

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);

	int n, test, i, caz;
	double x, y, z, vx, vy, vz, xn, yn, zn, vxn, vyn, vzn;
	double t, d, a, b, c;

	scanf("%d", &caz);
	for(test = 1; test <= caz; ++test)
	{
		scanf("%d", &n);
		x = y = z = vx = vy = vz = 0;
		for(i = 1; i <= n; ++i)
		{
			scanf("%lf %lf %lf %lf %lf %lf", &xn, &yn, &zn, &vxn, &vyn, &vzn);
			x += xn;
			y += yn;
			z += zn;
			vx += vxn;
			vy += vyn;
			vz += vzn;
		}
		if(vx == 0 && vy == 0 && vz == 0)
		{
			t = 0;
		}
		else
		{
			t = -(x * vx + y * vy + z * vz) / (vx * vx + vy * vy + vz * vz);
			if(t < 0)
			{
				t = +0;
			}
		}
		a = (double) (x + t * vx) / n;
		b = (double) (y + t * vy) / n;
		c = (double) (z + t * vz) / n;
		d = sqrt(a * a + b * b + c * c);
		printf("Case #%d: %.8lf %.8lf\n", test, d, t);
	}

	return 0;
}
