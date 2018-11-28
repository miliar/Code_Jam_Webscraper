#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>
using namespace std;

const double PI = 2*acos(0.0);

int tc, ntc;
double f, R, t, r, g;
double d;

double isinside(double y, double x, double R)
{
	return y*y + x*x <= R*R;
}

double area1(double y, double x, double R)
{
	double py = sqrt(R*R - x*x);
	double teta = atan(x/py);
	//printf("y=%lf, x=%lf, py=%lf, teta = %lf\n",y,x,py,teta);
	return (py-y)*x + teta/2*R*R - 0.5*x*py;
}

double intersect(double y1, double x1, double y2, double x2, double R)
{
	//printf("%.2lf %.2lf, %.2lf %.2lf\n",y1,x1,y2,x2);
	
	if (y1 < x1) 
	{
		swap(x1,y1);
		swap(x2,y2);
	}
	
	if (!isinside(y1,x1,R)) 
	{
		//printf("0\n"); 
		return 0;
	}
	if (isinside(y2,x2,R)) 
	{
		//printf("%.2lf\n",(y2-y1)*(x2-x1)); 
		return (y2-y1)*(x2-x1);
	}
	if (!isinside(y1,x2,R))
	{
		double px = sqrt( R*R - y1*y1 );
		double res = area1(y1,px,R) - area1(y1,x1,R);
		//printf("masuk1: %lf\n",res);
		return res;
	}
	else if (!isinside(y2,x1,R))
	{
		double py = sqrt( R*R - x2*x2 );
		double res = area1(py,x2,R) - area1(py,x1,R) + (py-y1)*(x2-x1);
		//printf("masuk2: %lf\n",res);
		return res;
	}
	
	double py2 = sqrt(R*R - x2*x2);
	double py1 = sqrt(R*R - x1*x1);
	double px1 = sqrt(R*R - y2*y2);

	double res = area1(py2,x2,R) - area1(py2,x1,R) - area1(y2,px1,R) + area1(y2,x1,R) + (py2-y1)*(x2-x1);	
	return res;
}

double calc1(double y, double x)
{
	//if (isinside(y+d-r, x+d-r, R-t)) return (g-f-f)*(g-f-f);
	return intersect(y+r+f, x+r+f, y+r+g-f, x+r+g-f, R-t-f);
}

double calc()
{
	if (f+f >= g) return 1;
	
	int i, j;
	double x, y;
	double res = 0;
	d = g+r+r;
	for (i=0;;i++)
	{
		y = i*d;
		//printf("y=%lf\n",y);
		if (y >= R) break;
		for (j=0;;j++)
		{
			x = j*d;
			//printf("x=%lf\n",x);
			if (x >= R) break;
			
			res += calc1(y, x);
		}
	}
	
	//printf("res = %lf\n",res);
	double area = PI*R*R / 4;
	//printf("area = %lf\n",area);
	double pfree = res / area;
	return 1 - pfree;
}

int main()
{
	scanf("%d",&ntc);
	double res;
	for (tc=1; tc<=ntc; tc++)
	{
		scanf("%lf %lf %lf %lf %lf",&f,&R,&t,&r,&g);
		res = calc();
		printf("Case #%d: %.10lf\n",tc,res);
	}
}