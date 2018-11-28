#include <cstdio>
#include <iostream>
#include <cmath>
#include <cassert>
using namespace std;
const double PI = 2.0 * acos(0.0);
double sq(double x) { return x * x; }
double f(double t) { return 0.5 * t * sqrt(1-sq(t)) + 0.5 * asin(t); }
double solve(double f, double R, double t, double r, double g)
{
	if (2 * f >= g)
		return 1.0;
	double A = R * R * PI;
	double radius = R - t - f;
	if (radius <= 0.0)
		return 1.0;
	double sum = 0.0;
	for (int i=0; ; i++)
	{
		double x0 = r + i * (g + 2 * r) + f;
		if (x0 > radius)
			break;
		double h0 = radius * sqrt(1-sq(x0/radius));
		double x1 = x0 + g - 2 * f;
		if (x1 > radius)
			x1 = radius;
		double h1 = radius * sqrt(1-sq(x1/radius));
		for (int j=0; ; j++)
		{
			double y0 = r + j * (g + 2 * r) + f;
			if (y0 > h0)
				break;
			double y1 = y0 + g - 2 * f;
			if (y1 > radius)
				y1 = radius;
			if (h0 >= y1 && h1 >= y1)
			{
				sum += (x1 - x0) * (g - 2 * f);
			}
			else 
			{
				double x = x0;
				if (h0 >= y1) // XXX
				{
					x = sqrt(sq(radius) - sq(y1));
					if (x < x0)
						x = x0;
					sum += (x - x0) * (g - 2 * f);
				}
				double xx = x1;
				if (h1 < y0)
				{
					xx = sqrt(sq(radius) - sq(y0));
					if (xx > x1)
						xx = x1;
				}
				double I = ::f(xx/radius) - ::f(x/radius);
				sum += I * radius * radius - (xx - x) * y0;
			}
		}
	}
	return (A - 4 * sum) / A;
}
int main()
{
	int N;
	cin >> N;
	for (int i=0; i<N; i++)
	{
		double f, R, t, r, g;
		cin >> f >> R >> t >> r >> g;
		printf("Case #%d: %.6lf\n", i+1, solve(f, R, t, r, g));
	}
	return 0;
}
