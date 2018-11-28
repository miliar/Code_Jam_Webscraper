#include <stdio.h>
#include <set>
#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <math.h>
using namespace std;

struct point
{
	double x, y;
};

double cross_product(const point& a, const point& b)
{
	return a.x*b.y - b.x*a.y;
}

double inner_product(const point& a, const point& b)
{
	return a.x*b.x + a.y*b.y;
}

double area( double rr, double x, double y, double l )
{
	double xaxa = (x+l)*(x+l), yaya = (y+l)*(y+l);
	double xa = x+l, ya = y+l;
	if( xaxa + yaya <= rr )
		return l*l;

	double xx = x*x, yy = y*y;
	if( xx + yy >= rr )
		return 0;
	
	point p[6];
	point a, b;
	int pn = 0;
	if( xaxa + y*y <= rr )
	{
		double sy = sqrt( rr - xaxa );
		p[pn].x = xa;
		p[pn].y = sy;
		a = p[pn];
		++pn;
		p[pn].x = xa;
		p[pn++].y = y;
	}
	else
	{
		double sx = sqrt( rr - yy );
		p[pn].x = sx;
		p[pn].y = y;
		a = p[pn];
		++pn;
	}

	p[pn].x = x;
	p[pn++].y = y;

	if( xx + yaya <= rr )
	{
		double sx = sqrt( rr - yaya );
		p[pn].x = x;
		p[pn++].y = ya;
		p[pn].x = sx;
		p[pn].y = ya;
		b = p[pn];
		++pn;

	}
	else
	{
		double sy = sqrt( rr - xx );
		p[pn].x = x;
		p[pn].y = sy;
		b = p[pn];
		++pn;
	}

	double ans = 0;
	
	p[pn] = p[0];
	
	for( int i=0; i<pn; ++i )
	{
		ans += cross_product( p[i], p[i+1] );
	}

	if( ans  < 0 )
		ans = -ans;

	ans += acos( inner_product( a, b )/rr )*rr - fabs( cross_product( a, b ) );

	return ans / 2;

}

int main()
{
	int case_num, n, m;
	
	freopen( "D:\\output.txt", "w", stdout );

	scanf( "%d", &case_num );

	for( int k=1; k<=case_num; ++k )
	{
		double f, R, t, r, g;
		scanf( "%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g );

		double ans = 0;

		if( f*2 >= g || R<=t+f )
		{
			ans = 1.0;
			goto loop;
		}
		
		ans = R*R*acos(-1.0);
		R -= f + t;

		double temp = 0, rr = R*R;

		for( int i=0; (g+2*r)*i <= R; ++i )
		{
			for( int j=0; (g+2*r)*j <= R; ++j )
			{
				temp += area( rr, (g+2*r)*i+r+f,  (g+2*r)*j+r+f, g - f*2 );
			}
		}

		ans = 1 - temp*4/ans;
loop:
		printf( "Case #%d: %.6lf\n", k, ans );

	}

	return 0;
}
