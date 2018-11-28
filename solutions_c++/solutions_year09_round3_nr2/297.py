#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>

using namespace std;


int main()
{
	int t, ti;
	int n;
	int i;
	double ax, ay, az, avx, avy, avz;
	double x, y, z, vx, vy, vz;
	double a, b, c, d;
	double time;
	double tmp;

	freopen( "B.in", "r", stdin );
	freopen( "B.out", "w", stdout );

	for( scanf( "%d", &t ), ti = 1; ti <= t; ++ti )
		{
		scanf( "%d", &n );
		ax = ay = az = avx = avy = avz = 0;
		for( i = 0; i < n; ++i )
			{
			scanf( "%lf%lf%lf%lf%lf%lf", &x, &y, &z, &vx, &vy, &vz );
			ax += x;
			ay += y;
			az += z;
			avx += vx;
			avy += vy;
			avz += vz;
			}//end for
		x = ax / n;
		y = ay / n;
		z = az / n;
		vx = avx / n;
		vy = avy / n;
		vz = avz / n;
		a = vx * vx + vy * vy + vz * vz;
		b = 2 * ( x * vx + y * vy + z * vz );
		c = x * x + y * y + z * z;
		time = -b / (2 * a);
		if( time >= 0 )
			{
			tmp = c - b * b /( 4 * a);
			if( tmp < 0 )
				{
				tmp = 0;
				}//end if
			d = sqrt( tmp );
			}
		else{
			time = 0;
			d = sqrt( c );
			}//end if
		printf( "Case #%d: %.7lf %.7lf\n", ti, d, time );
		}//end for

	return 0;
}

