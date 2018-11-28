#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;


#define MAXN 1010
struct VENDOR
{
	int num;
   	double pos, left, right;
	double spread;
	bool operator< ( const VENDOR &r ) const
	{
		return pos < r.pos;
	}
};

VENDOR vendor[ MAXN ];
int n, d;


double spread( int x )
{
	if ( x == 1 || !x )
		return 0;
	return (double)d / ( x & 1 ? 1 : 2 ) + spread( x >> 1 ) * 2;
}
	


int main()
{
	int t;
	freopen( "B.out", "w", stdout );
	scanf( "%d", &t );

	for ( int k = 1; k <= t; ++k )
	{
		scanf( "%d %d", &n, &d );

		for ( int i = 0; i < n; ++i )
			scanf( "%lf %d", &vendor[ i ].pos, &vendor[ i ].num ),
			vendor[ i ].left = vendor[ i ].right = vendor[ i ].pos;
		
		sort( vendor, vendor + n );

		double MIN = 1e9, MAX = -1e9, now = vendor[ 0 ].pos;
		
		for ( int i = 0; i < n; ++i )
		{
			if ( vendor[ i ].pos - now >= d )
				now = vendor[ i ].pos;
			
			for ( int j = 0; j < vendor[ i ].num; ++j )
			{
				if ( vendor[ i ].pos - now > MAX )
					MAX = vendor[ i ].pos - now;
				if ( vendor[ i ].pos - now < MIN )
					MIN = vendor[ i ].pos - now;
				now += d;
			}
		}

		if ( MIN + MAX )
			MAX -= ( MAX - MIN ) / 2;
		if ( MAX < 0 )
			MAX *= -1;
		printf( "Case #%d: %.10lf\n", k, MAX );
	}
	return 0;
}




			

