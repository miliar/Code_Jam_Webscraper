#include <iostream>
#include <cmath>
#include <vector>
#include <cstring>
using namespace std;


#define MAXN 1010

int sgn( double x )
{
	return fabs( x ) < 1e-9 ? 0 : x > 0 ? 1 : -1;
}

struct WAY
{
	int x1, x2, v;
	WAY( int _x1, int _x2, int _v )
		: x1( _x1 ), x2( _x2 ), v( _v )
	{}
	bool operator< ( const WAY &r ) const
	{
		return x1 < r.x1;
	}
};

double d[ MAXN ];

int main()
{
	freopen( "A.out", "w", stdout );
	int test;
	scanf( "%d", &test );

	int x, s, r, t, n;
	for ( int k = 1; k <= test; ++k )
	{
		scanf( "%d %d %d %d %d", &x, &s, &r, &t, &n );

		memset( d, 0, sizeof( d ) );
		vector< WAY > way;
		for ( int i = 0; i < n; ++i )
		{
			int a, b, v;
			scanf( "%d %d %d", &a, &b, &v );
			way.push_back( WAY( a, b, v ) );
		}

		sort( way.begin(), way.end() );

		double dis = 0, now = 0;

		for ( int i = 0; i < way.size(); ++i )
		{
			dis += way[ i ].x1 - now;
			now = way[ i ].x2;
			d[ way[ i ].v ] += way[ i ].x2 - way[ i ].x1;
		}
		
		dis += x - now;

		d[ 0 ] += dis;

		double ret = 0, remain = t;

		for ( int i = 0; i < MAXN; ++i )
		{
			if ( !d[ i ] )
				continue;
			double a = i + r, b = i + s;

			if ( sgn( remain * a - d[ i ] ) >= 0 )
			{
				
				ret += d[ i ] / a;
				remain -= d[ i ]/ a;
			}
			else
			{
				d[ i ] = d[ i ] - remain * a;
				ret += remain + d[ i ] / b;
				remain = 0;
			}
		}
	
		printf( "Case #%d: %.7lf\n", k, ret );
	}
	return 0;
}





