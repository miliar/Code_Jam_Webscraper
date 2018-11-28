#include <cstdio>
#include <cstring>
#include <cmath>

int x, y, z;
int vx, vy, vz;
int n;

double len(double x, double y, double z)
{
	return sqrt(x * x + y * y + z * z);
}

void gett(int x, int y, int z, int vx, int vy, int vz, double &t)
{
	double l = len(vx, vy, vz);
	double p = x / l * vx + y / l * vy + z / l * vz;
	t = p / l;
}

int main()
{
	int testnumber, testcount;
	int x0, y0, z0, vx0, vy0, vz0;
	double t, d;
	
	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);
	
	scanf("%d", &testnumber);
	for (testcount = 0; testcount < testnumber; testcount++)
	{
		scanf("%d", &n);
		x = y = z = vx = vy = vz = 0;
		for (int i = 0; i < n; i++)
		{
			scanf("%d %d %d %d %d %d", &x0, &y0, &z0, &vx0, &vy0, &vz0);
			x += x0;
			y += y0;
			z += z0;
			vx += vx0;
			vy += vy0;
			vz += vz0;
		}
		if (vx == 0 && vy == 0 && vz == 0)
		{
			t = 0;
		}
		else
		{
			gett(-x, -y, -z, vx, vy, vz, t);
			if (t <= 0) t = 0;
		}
		d = len(x + vx * t, y + vy * t, z + vz * t);
		printf("Case #%d: %.8lf %.8lf\n", testcount + 1, d / n, t);
	}
	
	return 0;
}
