#include <stdio.h>
#include <math.h>

int w, l, u, g;
int xl[1000], yl[1000];
int xu[1000], yu[1000];

int x[2000], p;
double y[2000];

double solver (double a, double b, double c)
{
//	printf ("%lf %lf %lf\n", a, b, c);
	if (a < 1e-10 && a > -1e-10)
		return -c/b;
	if (a < 0)
		return (-b + sqrt(b*b-4*a*c)) / (2*a);
	else
		return (-b + sqrt(b*b-4*a*c)) / (2*a);
}

double ans (double area)
{
	for (int i = 0; i < p - 1; i ++)
	{
//		printf ("%lf %lf\n", area, (y[i] + y[i + 1]) * (x[i+1] - x[i]));
		if ((y[i] + y[i + 1]) * (x[i+1] - x[i]) / 2 <= area)
		{
			area -= (y[i] + y[i + 1]) * (x[i+1] - x[i]) / 2;
		}
		else
		{
			if (area < 1e-10)
				return x[i];
			double w;
			
			double dy = (y[i+1]-y[i]), dx = (x[i+1]-x[i]);
			
			w = solver (dy / dx / 2, y[i], -area);
			
			return x[i] + w;
		}
	}
	
	return w;
}

int main ()
{
	int t, ct = 0;
	
	for (scanf ("%d", &t); t > 0; t --)
	{
		scanf ("%d%d%d%d", &w, &l, &u, &g);
		
		for (int i = 0; i < l; i ++)
			scanf ("%d%d", xl + i, yl + i);
		
		for (int i = 0; i < u; i ++)
			scanf ("%d%d", xu + i, yu + i);
			
		double area = 0;
		for (int i = 1; i < u; i ++)
			area += (yu[i] + yu[i - 1]) * (xu[i] - xu[i - 1]) / 2.0;
		for (int i = 1; i < l; i ++)
			area -= (yl[i] + yl[i - 1]) * (xl[i] - xl[i - 1]) / 2.0;
		
		area /= g;
//		printf ("%lf\n", area);
		
		p = 0;
		{
			int i = 0, j = 0;
			
			while (i < l && j < u)
			{
				if (xl[i] == xu[j])
				{
					x[p] = xl[i];
					y[p] = yu[j] - yl[i];
					p ++;
					i ++;
					j ++;
				}
				else if (xl[i] < xu[j])
				{
					x[p] = xl[i];
					y[p] = yu[j - 1] + (yu[j] - yu[j - 1]) * (double)(xl[i] - xu[j - 1]) / (xu[j] - xu[j - 1]) - yl[i];
					p ++;
					i ++;
				}
				else
				{
					x[p] = xu[j];
					y[p] = yu[j] - yl[i - 1] - (yl[i] - yl[i - 1]) * (double)(xu[j] - xl[i - 1]) / (xl[i] - xl[i - 1]);
					p ++;
					j ++;
				}
			}
		}
		
//		for (int i =0 ; i < p; i ++)
//			printf ("%d %lf\n", x[i], y[i]);

		printf ("Case #%d:\n", ++ ct);
		for (int i = 1; i <= g - 1; i ++)
			printf ("%.6lf\n", ans (i * area));
	}
	
	return 0;
}
