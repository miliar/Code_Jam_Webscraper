#include <cstdio>
#include <cstring>
#include <utility>
#include <algorithm>
#include <math.h>
#include <vector>
using namespace std;
const double PI = acos(-1.0);
int 	cas, T = 0;

double 	f, R, t, r, g;

double	lv, Rt;


double	DIS(double a, double b)
{return sqrt(a*a + b*b);}

double 	get_lv(double ff, double rr)
{
	double 	rnt;
	
//	if (ff >= rr)	
		rnt = ff;
//	else
//		rnt = sqrt(4*ff*rr) - rr;
	return rnt;	
}


double 	f1(double	x)
{	return x / 2.0 * sqrt(Rt*Rt - x*x) + Rt*Rt / 2.0 * asin(x / Rt);}

double	 Cal(double a, double b, double C)
{
	double	 rnt = 0.0;
	
	rnt = f1(b) - f1(a) - C*(b - a);
	return rnt;
}

double	Add(double x, double y)
{
	double	x0 = x + r + lv, x1 = x + r + g - lv;
	double	y0 = y + r + lv, y1 = y + r + g - lv;
	double	rnt = 0.0;
	
	double	nx0 = -1, nx1 = -1;
	double 	temp;
	
	
	if (sqrt(x0*x0 + y0*y0) > Rt)	return 0.0;
	
	
	if ((temp = Rt*Rt - y0*y0) > 0)
	{
		temp = sqrt(temp);
		if (temp>=x0 && temp <= x1)	nx1 = temp;
	}
	if ((temp = Rt*Rt - y1*y1) > 0)
	{
		temp = sqrt(temp);
		if (temp>=x0 && temp <= x1)	nx0 = temp;
	}
	
	if (DIS(x1, y1) < Rt)
		rnt = (x1 - x0) * (y1 - y0);
	else if (nx0 > 0 && nx1 < 0)
		rnt = (y1-y0) * (nx0-x0) + Cal(nx0, x1, y0);
	else if (nx0 > 0 && nx1 > 0)
		rnt = (y1-y0) * (nx0-x0) + Cal(nx0, nx1, y0);
	else if (nx0 < 0 && nx1 > 0)
		rnt = Cal(x0, nx1, y0);
	else if (nx0 < 0 && nx1 < 0)
		rnt = Cal(x0, x1, y0);
	
	return rnt;
}

int main()
{
	int 	i, j, k;
	
	freopen("C-small-attempt3.in", "r", stdin);
	freopen("C_small_out.txt", "w", stdout);	
		
	for (scanf("%d", &cas); cas; cas--)
	{
	
		scanf("%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);
		
		lv = get_lv(f, r);
		/*
		if (g - lv*2 < 0 || fabs(g - 2*lv) < 1e-7)
		{
			printf("Case #%d: %.6lf\n", ++T, 1.0);	
			continue;
		}
		*/
		
		Rt = R - t - f;
		double 	x, y;
		double 	delt = 2.0 * r + g;
		
		double	 area = 0.0;
		for (x=0.0; x<R; x+=delt)
		{
			for (y=0.0; y<R; y+=delt)	
			{
				double 	tp = Add(x, y);
				area += tp;
			//	printf("x,y, %lf %lf	add %lf\n", x, y,  Add(x, y));
			}
		}
	
		//printf("area %lf\n", area);
		double	tot = PI * R * R/4.0;
		double	p = 1.0 - area / tot;
		printf("Case #%d: %.6lf\n", ++T, p);	
	}
	return 0;
}
