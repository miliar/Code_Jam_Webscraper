#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <string>
#include <math.h>

using namespace std;

long double R, t;
long double r, g, f;
long double pi;

inline long double rad(long double x, long double y)
{
	return sqrtl(x * x + y * y);
}

inline long double wyc(long double x1, long double y1, long double x2, long double y2)
{
	long double dl = rad(x1-x2, y1-y2);
	long double kat;
	long double q;
	dl /= (long double) 2.0;
	kat = dl/t;
	kat = asinl(kat);
	kat /= pi;
	kat *= pi * t * t;
	q = sqrtl(t*t - dl*dl);
	q *= dl;
	q = kat - q;
	long double x,y;
	if (x1 <= x2) x = x2-x1;
	else x = x1-x2;
	if (y1 <= y2) y = y2-y1;
	else y = y1-y2;
	x *= y;
	x /= (long double) 2.0;
	return q + x;
}

long double znajdz(long double x)
{
	return sqrtl(t*t - x*x);
}

long double pole(long double x, long double y)
{
	long double a,b, ret=0.0;
	long double c;
	if (x<y)
	{
		c = x;
		x = y;
		y = c;
	}
	if (rad(x+g, y+g) <= t) return (g+g)*(g+g);
	if (rad(x+g, y-g) <= t)
	{
		a = znajdz(x+g);
		b = znajdz(y+g);
		ret = wyc(x+g,a,b,y+g);
		ret += (x+g-b) * (a+g-y);
		ret += (g+g) * (b+g-x);
		return ret;
	}
	if (rad(x-g, y+g) <= t)
	{
		a = znajdz(y-g);
		b = znajdz(y+g);
		ret = wyc(a,y-g,b,y+g);
		if (b>a) b=a;
		ret += (g+g) * (b+g-x);
		return ret;
	}
	if (rad(x-g, y-g) <= t)
	{
		a = znajdz(x-g);
		b = znajdz(y-g);
		return wyc(x-g,a,b,y-g);
	}
	return (long double) 0.0;
}

long double licz(void)
{
	scanf("%llf%llf%llf%llf%llf", &f, &R, &t, &r, &g);
	t = R-t-f;
	r += f;
	g -= f+f;
	g /= (long double) 2.0;
	if (g<=((long double)0)) return (long double) 1.0;
	long double ret = pi * R * R;
	long double og1 = R / (g + g + r + r);
	int ogr = og1;
	ogr += 100;
	long double x,y;
	x = r + g;
	for(int i = 0; i <= ogr; i++)
	{
		y = r + g;
		for(int j = 0; j <= ogr; j++)
		{
			ret -= pole(x,y) * ((long double) 4.0);
			y += g + g + r + r;
		}
		x += g + g + r + r;
	}
	ret /= (pi * R * R);
	return ret;
}

int main(void)
{
	pi = acosl((long double) -1.0);
	int dd;
	scanf("%d",&dd);
	for(int yy=1; yy<=dd; yy++) printf("Case #%d: %llf\n",yy, licz());
	return 0;
}
