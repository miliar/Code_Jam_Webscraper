#include <cstdio>
#include <cmath>
#include <string>

void OpenFiles()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
}

struct point
{
	int x, y, z;

	point(int x = 0, int y = 0, int z = 0)
	{
		this->x = x;
		this->y = y;
		this->z = z;
	}

	void scan()
	{
		scanf("%d%d%d", &x, &y, &z);
	}

	point operator + (point rhs)
	{
		return point(x + rhs.x, y + rhs.y, z + rhs.z);
	}

	bool operator ==(point rhs)
	{
		return x == rhs.x && y == rhs.y && z == rhs.z;
	}
};

point c[1000];
point v[1000];
int n, t;

double dist(double x, double y, double z)
{
	double t = x*x+y*y+z*z;
	if (t < 0) t = 0;
	return sqrt(t);
}

int main()
{
	OpenFiles();
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		printf("Case #%d: ",i+1);
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
		{
			c[i].scan();
			v[i].scan();
		}

		point a;
		for (int i = 0; i < n; i++)
			a = a + c[i];
		point b = a;
		for (int i = 0; i < n; i++)
			b = b + v[i];
		if (a == b)
		{
			printf("%.9lf %.9lf\n", dist((double)a.x / n, (double)a.y / n, (double)a.z / n), 0);
		}
		else
		{
			double x1 = (double)a.x / n;
			double y1 = (double)a.y / n;
			double z1 = (double)a.z / n;

			double x2 = 0;
			double y2 = 0;
			double z2 = 0;

			double vx = (double)(b.x-a.x) / n;
			double vy = (double)(b.y-a.y) / n;
			double vz = (double)(b.z-a.z) / n;

			double A = (vx*vx + vy*vy + vz*vz);
			double B = 2*(vx*(x1-x2) + vy*(y1-y2) + vz*(z1-z2));
			double C = ((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) + (z1-z2)*(z1-z2));


			double t = -B/2/A;

			if (t < 0)
				t = 0;

			printf("%.9lf %.9lf\n", dist(x1 + t*vx, y1 + t*vy, z1 + t*vz), t);
		}
	}


	return 0;
}