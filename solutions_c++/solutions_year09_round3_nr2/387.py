#include <stdio.h>
#include <string.h>
#include <math.h>

#define EPS				1e-6

int main() 
{
	int T , caseT ; 
	int n , i ;
	double x , y , z , vx , vy , vz ;
	double sx , sy , sz , svx , svy , svz ;
	double a , b , c , t , d ;

	freopen( "B-large.in" , "r" , stdin ) ;
	freopen( "B-large.out" , "w" , stdout ) ;

	scanf( "%d" , &T ) ;
	for ( caseT=1 ; caseT<=T ; ++caseT ) 
	{
		scanf( "%d" , &n ) ;
		sx = sy = sz = 0.0 ;
		svx = svy = svz = 0.0 ;
		for ( i=0 ; i<n ; ++i ) 
		{
			scanf( "%lf%lf%lf%lf%lf%lf" , &x , &y , &z , &vx , &vy , &vz ) ;
			sx += x ; sy += y ; sz += z ;
			svx += vx ; svy += vy ; svz += vz ;
		}
		a = svx*svx + svy*svy + svz*svz ;
		c = sx*sx + sy*sy + sz*sz ;
		b = 2*( sx*svx + sy*svy + sz*svz ) ;
//		if ( caseT == 43 ) printf( "%f\n%f\n%f\n" , a , b , c ) ;
		if ( fabs(a)<EPS )
		{
			if ( fabs(b)<EPS ) 
			{
				t = 0 ;
				d = c ;
				goto end ;
			}
			else
			{
				if ( b<-EPS ) t = -c/b ;
				else t=0 ;
				d = b*t+c ;
				goto end ;
			}
		}
		else
		{
			if ( -b/(2*a) < -EPS )
			{
				if ( -(b*b)/(4*a)+c > -EPS ) 
				{
					t = 0 ;
					d = a*t*t+b*t+c ;
					goto end ;
				}
				else
				{
					t = ( -b+sqrt( b*b-4*a*c ) ) / (2*a) ;
					d = 0 ;
					goto end ;
				}
			}
			else
			{
				if ( -(b*b)/(4*a)+c > -EPS ) 
				{
					t = -b/(2*a) ;
					d = -(b*b)/(4*a)+c ;
					goto end ;
				}
				else
				{
					if ( ( -b-sqrt( b*b-4*a*c ) ) / (2*a) > -EPS )
					{
						t = ( -b-sqrt( b*b-4*a*c ) ) / (2*a) ;
						d = 0 ;
						goto end ;
					}
					else
					{
						t = ( -b+sqrt( b*b-4*a*c ) ) / (2*a) ;
						d = 0 ;
						goto end ;
					}
				}
			}
		}
end:
		d = sqrt( d ) / n ;
		printf( "Case #%d: %.8f %.8f\n" , caseT , d , t ) ;

	}

	return 0 ;
}