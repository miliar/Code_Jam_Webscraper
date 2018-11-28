#include <math.h>
#include <stdio.h>

using namespace std;

const double PI = 3.1415926535897932384626433832795;

double racquetArea(double f, double R, double t, double r, double g);
double stringArea(double r, double x1, double x2);

int main()
{
	double f, R, t, r, g, probability;
	int numCases;
	
	scanf("%d\n", &numCases);
	for (int curCase = 1; curCase <= numCases; curCase++)
	{
		scanf("%lf %lf %lf %lf %lf\n", &f, &R, &t, &r, &g);
		probability = racquetArea(f, R, t, r, g) / (PI * R * R);
		printf("Case #%d: %lf\n", curCase, probability);
	}
	return 0;
}

double racquetArea(double f, double R, double t, double r, double g)
{
	double frameArea, area, x, y, x2, y2;
	double yofx, yofx2, xofy, xofy2;
	
	frameArea = PI * R * R;
	R -= t + f;
	g -= 2 * f;
	r += f;
	if (R <= 0 || g <= 0 || r > R)
	{
		return frameArea;
	}
	frameArea -= PI * R * R;

	// Vertical strings in quadrant 1
	area = stringArea(R, 0, r);
	for (x = 3 * r + g; x < R; x += g + 2 * r)
	{
		area += stringArea(R, x - 2 * r, x);
	}
	if (x - 2 * r < R)
	{
		area += stringArea(R, x - 2 * r, R);
	}

	// Horizontal strings in quadrant 1
	area *= 2;
	// Subtract intersection of strings
	x = 0;
	x2 = r;
	while (x2 < R)
	{
		y = 0;
		y2 = r;
		yofx = sqrt(R * R - x * x);
		yofx2 = sqrt(R * R - x2 * x2);
		while (y2 < yofx2)
		{
			area -= (x2 - x) * (y2 - y);
			y = y2 + g;
			y2 += g + 2 * r;
		}
		while (1)
		{
			if (y < yofx2)
			{
				if (y2 < yofx)
				{
					xofy2 = sqrt(R * R - y2 * y2);
					area -= stringArea(R, xofy2, x2) - (x2 - xofy2) * y;
					area -= (xofy2 - x) * (y2 - y);
				}
				else
				{
					area -= stringArea(R, x, x2) - (x2 - x) * y;
				}
			}
			else
			{
				xofy = sqrt(R * R - y * y);
				if (y2 < yofx)
				{
					xofy2 = sqrt(R * R - y2 * y2);
					area -= stringArea(R, xofy2, xofy) - (xofy - xofy2) * y;
					area -= (xofy2 - x) * (y2 - y);
				}
				else if (y < yofx)
				{
					area -= stringArea(R, x, xofy) - (xofy - x) * y;
				}
				else
				{
					break;
				}
			}
			y = y2 + g;
			y2 += g + 2 * r;
		}
		x = x2 + g;
		x2 += g + 2 * r;
	}
	if (x < R)
	{
		y = 0;
		y2 = r;
		yofx = sqrt(R * R - x * x);
		while (1)
		{
			xofy = sqrt(R * R - y * y);
			if (y2 < yofx)
			{
				xofy2 = sqrt(R * R - y2 * y2);
				area -= stringArea(R, xofy2, xofy) - (xofy - xofy2) * y;
				area -= (xofy2 - x) * (y2 - y);
			}
			else if (y < yofx)
			{
				area -= stringArea(R, x, xofy) - (xofy - x) * y;
			}
			else
			{
				break;
			}
			y = y2 + g;
			y2 += g + 2 * r;
		}
	}
	return 4 * area + frameArea;
}

double stringArea(double r, double x1, double x2)
{
	double r2 = r * r;
	return (0.5 * x2 * sqrt(r2 - x2 * x2) + 0.5 * r2 * asin(x2 / r)) -
	       (0.5 * x1 * sqrt(r2 - x1 * x1) + 0.5 * r2 * asin(x1 / r));
}
