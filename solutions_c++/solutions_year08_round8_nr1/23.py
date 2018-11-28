#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cmath>
using namespace std;

const long double eps = 1e-10;

long double x[6], y[6];
	long double bx, by;

void Load()
{
	int i;
	for (i = 0; i < 6; i++)
	{
		cin >> x[i] >> y[i];
	}
	bx = x[0];
	by = y[0];
	for (i = 0; i < 6; i++)
	{
		x[i] -= bx;
		y[i] -= by;
	}
}

long double vx[4], vy[4];

void Solve()
{
	vx[0] = x[1] - x[0];
	vy[0] = y[1] - y[0];
	vx[1] = x[2] - x[0];
	vy[1] = y[2] - y[0];
	vx[2] = x[4] - x[3];
	vy[2] = y[4] - y[3];
	vx[3] = x[5] - x[3];
	vy[3] = y[5] - y[3];
	long double a1, b1, c1, a2, b2, c2;
	a1 = (vx[0] - vx[2]);
	b1 = (vx[1] - vx[3]);
	c1 = x[3];
	a2 = (vy[0] - vy[2]);
	b2 = (vy[1] - vy[3]);
	c2 = y[3];
	long double d = a1 * b2 - b1 * a2;
	if (fabs(d) < eps)
	{
		if ((fabs(c1) < eps) && (fabs(c2) < eps))
		{
			printf("%.10lf %.10lf", (double)bx, (double)by);
		}
		else
		{
			printf("No solution");
		}
	}
	else
	{
		long double xx, yy;
		xx = (c1 * b2 - b1 * c2) / d;
		yy = (a1 * c2 - c1 * a2) / d;
		printf("%.10lf %.10lf", (double)(xx * vx[0] + yy * vx[1] + bx), (double)(xx * vy[0] + yy * vy[1] + by));
	}
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int nt, it;
	scanf("%d", &nt);
	for (it = 0; it < nt; it++)
	{
		printf("Case #%d: ", it + 1);
		Load();
		Solve();
		printf("\n");
	}
	return 0;
}