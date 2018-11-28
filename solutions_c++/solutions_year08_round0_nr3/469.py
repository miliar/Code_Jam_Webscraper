#include <cstdio>
#include <math.h>

long double PI = 0;

inline long double dist(long double x, long double y)
{
	return sqrt(x*x+y*y);
}

inline long double mabs(long double a)
{
	if (a < 0.0)
		return -a;
	return a;
}

inline long double arcsin(long double d)
{
	return asin(d);
}

inline long double func(long double x1, long double x2, long double r)
{
	long double res1 = x1/2.0 * sqrt(r*r - x1*x1) + (r*r)/2.0 * arcsin(x1/r);
	long double res2 = x2/2.0 * sqrt(r*r - x2*x2) + (r*r)/2.0 * arcsin(x2/r);
	return mabs(res1-res2);
}
int main()
{
	freopen("c.txt", "w", stdout);
	//freopen("test.txt", "r", stdin);
	PI = acos(0.0)*2.0;
	int T;
	scanf("%d", &T);
	for (int tt=1; tt<=T; tt++)
	{
		double df, dR, dt, dr, dg;
		scanf("%lf%lf%lf%lf%lf",&df,&dR,&dt,&dr,&dg);
		long double f, R, t, r, g;
		f = df;
		R = dR;
		t = dt;
		r = dr;
		g = dg;
		long double res = 0;

		long double len = r+r+g;
		for (int i=0; i<3000; i++)
		{
			long double x = len*i;
			if (x > R)
				break;
			for (int j=0; j<3000; j++)
			{
				long double y = len*j;
				if (dist(x+r+f,y+r+f) >= R-t-f)
					break;
				long double nx = len*(i+1);
				long double ny = len*(j+1);
				if (dist(nx,ny) <= R)
				{
					res += (g-f-f)*(g-f-f);
				}
				else
				{
					int type = 0;
					long double x1 = x+r+f;
					long double y1 = y+r+f;
					long double x2 = x+len-r-f;
					long double y2 = y1;
					long double x3 = x1;
					long double y3 = y+len-r-f;

					long double y5 = y1;
					long double x5 = sqrt((R-t-f)*(R-t-f) - y5*y5);
					if (x5 > x2)
						type = 1;
					long double x7 = x2;
					long double y7 = 1e100;
					if (type == 1)
						y7 = sqrt((R-t-f)*(R-t-f) - x7*x7);

					long double x6 = x1;
					long double y6 = sqrt((R-t-f)*(R-t-f) - x6*x6);
					if (y6 > y3)
						type += 2;
					long double x8 = 1e100;
					long double y8 = y3;
					if (type >= 2)
						x8 = sqrt((R-t-f)*(R-t-f) - y8*y8);
					switch(type)
					{
					case 0:
						res += func(x1,x5,R-t-f);
						res -= mabs(x1-x5)*y1;
						break;
					case 1:
						res += func(x1,x2,R-t-f);
						res -= mabs(x1-x2)*y1;
						break;
					case 2:
						res += func(x8,x5,R-t-f);
						res -= mabs(x8-x5)*y1;
						res += mabs(x1-x8)*mabs(y1-y3);
						break;
					case 3:
						res += func(x8,x7, R-t-f);
						res -= mabs(x8-x7)*y1;
						res += mabs(x1-x8)*mabs(y1-y3);
						break;
					}
				}
			}
		}

		long double fullSQ = PI*R*R/4.0;
		res = res/fullSQ;
		res = 1.0 - res;
		printf("Case #%d: %.6lf\n", tt, (double)res);
	}
	return 0;
}