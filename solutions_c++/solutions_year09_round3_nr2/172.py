#include <cstdio>
#include <cmath>

int T;
int N;
double X, Y, Z, Vx, Vy, Vz;
int x, y, z, vx, vy, vz;
int main()
{
	scanf("%d", &T);
	for(int test = 0; test < T; test ++)
	{
		scanf("%d", &N);
		X = 0, Y = 0, Z = 0;
		Vx = 0, Vy = 0, Vz = 0;
		for(int i = 0; i < N; i ++)
		{
			scanf("%d %d %d %d %d %d", &x, &y, &z, &vx, &vy, &vz);
			X += x;			Y += y;			Z += z;
			Vx += vx;		Vy += vy;		Vz += vz;
		}
		double t = 0;
		double div = Vx * Vx + Vy * Vy + Vz * Vz;
		if(fabs(div) > 1e-7)
			t = - (X * Vx + Y * Vy + Z * Vz) / div;
		if(t < 0)	t = 0;
		double d = 0;
		d = X * X + Y * Y + Z * Z +
		2 * (X * Vx + Y * Vy + Z * Vz) * t +
		(Vx * Vx + Vy * Vy + Vz * Vz) * t * t;
		if(d < 0)	d = 0;
		d = sqrt(d);
		printf("Case #%d: %.9lf %.9lf\n", test + 1, d / N, t);
	}
    return 0;
}
