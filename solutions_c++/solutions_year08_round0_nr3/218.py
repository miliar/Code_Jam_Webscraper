#include <stdio.h>
#include <math.h>
#define eps 0.0000001

double PI = 2*acos(0);

double dist(double x, double y)
{	return sqrt(x * x + y * y);	}
double areaTriangle(double x1, double y1, double x2, double y2)
{	return (x1 * y2 - y1 * x2) / 2;	}
double angle(double x1, double y1, double x2, double y2)
{
	//printf("tri: %.6lf\n", areaTriangle(x1, y1, x2, y2));
       return asin(2 * areaTriangle(x1, y1, x2, y2) / (dist(x1, y1) * dist(x2, y2)));  }
double areaSector(double x1, double y1, double x2, double y2, double r)
{	return angle(x1, y1, x2, y2) * r * r / 2;	}
int equals(double a, double b)
{	return (a - b < eps && a - b > -eps);	}

double x2, y2, px[10], py[10], rez, xi, yi, xj, yj;
int n, i, here;
double intersect(double r, double x1, double y1, double l)
{
	x2 = x1 + l;
	y2 = y1 + l;
	
	if (dist(x1, y1) >= r)
		return 0;
	if (dist(x2, y2) <= r)
		return l * l;

	//now definitely intersects
	xi = x2;
	yi = sqrt(r * r - xi * xi);

	if (yi < y1 || yi > y2)
	{
		yi = y1;
		xi = sqrt(r * r - yi * yi);
	}

	xj = x1;
	yj = sqrt(r * r - xj * xj);
	if (yj < y1 || yj > y2)
	{
		yj = y2;
		xj = sqrt(r * r - yj * yj);
	}

	//forming a polygon
	n = 1;
	px[0] = x1; py[0] = y1;
	if (!equals(y1, yi))
		px[n] = x2, py[n] = y1, n++;

	here = n;
	px[n] = xi, py[n] = yi, n++;
	px[n] = xj, py[n] = yj, n++;

	if (!equals(x1, xj))
		px[n] = x1, py[n] = y2, n++;

	/*printf("poly: ");
	for (i = 0; i < n; i++)
		printf("%.6lf %.6lf\n", px[i], py[i]);*/

	rez = 0;
	double reza = 0;

	for (i = 0; i < n; i++)
	{
		if (i != here)
			rez += areaTriangle(px[i], py[i], px[(i+1)%n], py[(i+1)%n]);
		else
			rez += areaSector(px[i], py[i], px[(i+1)%n], py[(i+1)%n], r);

		//printf("arie de : %.6lf\n", rez-reza);
		reza = rez;
	}
	//printf("returning: %.6lf", rez);
	return rez;
}

int N;
double f, R, t, r, g;

FILE *fin, *fout;

int main()
{
	int lim = 1005, ix, iy;
	double x, y, rez, lat;

	fin = fopen("input.txt", "rt");
	fout = fopen("output.txt", "wt");

	fscanf(fin, "%d", &N);
	for (int test = 1; test <= N; test++)
	{
		printf("test %d\n", test);
		fscanf(fin, "%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);
		rez = 0;

		lat = g - 2 * f;

		if (lat > 0)
		{
			for (ix = 0; ix < lim; ix++)
			for (iy = 0; iy < lim; iy++)
			{
				x = r + ix * (g + 2 * r) + f;
				y = r + iy * (g + 2 * r) + f;
				
				//printf("intersect(%.6lf, %.6lf, %.6lf, %.6lf) is %.6lf\n", R-t-f, x, y, lat,  intersect(R - t - f, x, y, lat));
				rez += intersect(R - t - f, x, y, lat);
			}
		}
		
		fprintf(fout, "Case #%d: %.6lf\n", test, 1 - 4 * rez / (PI * R * R));
	}	

	return 0;
}

