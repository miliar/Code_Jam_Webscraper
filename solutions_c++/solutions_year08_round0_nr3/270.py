#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/stack:16000000")
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

int nn;
double f, R, t, r, g, sall, s;

bool inside(double x, double y)
{
	return x*x+y*y<=R*R;
}

double F(double x)
{
	return x/2.0*sqrt(R*R-x*x)+R*R/2.0*asin(x/R);
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	scanf("%d\n",&nn);
	for (int ii=1; ii<=nn; ++ii)
	{
		scanf("%lf%lf%lf%lf%lf\n", &f, &R, &t, &r, &g);
		s = 0; 
		sall = 3.1415926535897932384626433832795*R*R/4.0;
		R -= f;
		R -= t;
		r += f;
		g -= 2*f;
		if (g>0)
			for (int i=0; i<600; ++i)
				for (int j=0; j<600; ++j)
				{
					double x0 = r + i*(2*r+g),
						   y0 = r + j*(2*r+g),
						   x1 = r + i*(2*r+g) + g,
						   y1 = r + j*(2*r+g) + g;
					bool f1 = inside(x0, y0),
						 f2 = inside(x0, y1),
						 f3 = inside(x1, y0),
						 f4 = inside(x1, y1);
					if (f1)
					if (f4)
						s += g*g;
					else
					if (f1 && !f2 && f3)
						s += F(x1)-F(x0)-(x1-x0)*y0;
					else
					if (f1 && f2 && !f3)
						s += F(y1)-F(y0)-(y1-y0)*x0;
					else
					if (f1 && !f2 && !f3)
					{
						double xt = sqrt(R*R-y0*y0);
						s += F(xt)-F(x0)-(xt-x0)*y0;
					}
					else
					if (f1 && f2 && f3)
					{
						double xt = sqrt(R*R-y1*y1);
						s += g*g + F(x1)-F(xt)-(x1-xt)*y1;
					}
			}

		printf("Case #%d: %.6lf\n", ii, 1.0-s/sall);
	}
	return 0;
}
