#include "stdio.h"
#include <vector>
#include <set>
#include <strstream>
#include <string>
#include <algorithm>
#include <hash_map>
#include <hash_set>
#include <queue>
#include <math.h>
using namespace std;
using namespace stdext;


int a[1000][200];
bool w[110][110];
int x[100], y[100], r[100];

double get( int a, int b )
{
	return (r[a] + r[b] + sqrt( 1.0*(x[a]-x[b])*(x[a]-x[b]) + (y[a]-y[b])*(y[a]-y[b]) ))/2;
}

int main()
{
	freopen( "test.in", "r", stdin );
	freopen( "test.out", "w", stdout );

	int tn, m, n;
	scanf( "%d", &tn );
	for( int cn = 1; cn <= tn; ++cn )
	{
		scanf( "%d", &n );
		
		for( int i=0; i<n; ++i )
		{
			scanf( "%d%d%d", x+i, y+i, r+i );
		}

		double ans = 1e99;
		if( n == 1 )
		{
			ans = r[0];
		}
		else if( n == 2 )
		{
			ans = ( r[0] < r[1] ? r[1] : r[0] );
		}
		else
		{
			double s = 0;
			for( int i=0; i<3; ++i )
			{
				s = r[i];
				if( i == 0 )
				{
					if( s <  get( 1, 2 ) )
						s = get( 1, 2 );
				}
				if( i == 1 )
				{
					if( s <  get( 0, 2 ) )
						s = get( 0, 2 );
				}
				if( i == 2 )
				{
					if( s <  get( 1, 0 ) )
						s = get( 1, 0 );
				}

				if( s < ans )
					ans = s;
			}

		}


		printf( "Case #%d: %lf\n", cn, ans );
	}
	return 0;

}