#include <cstdio>
#include <cstring>
#include <algorithm>
#include <functional>
using namespace std;

typedef pair<long long,long long> pii;

long long n, w, l;
pii r[100020];

long long x[100020], y[100020];

void put( long long p, long long xx, long long yy )
{
	x[p] = xx;
	y[p] = yy;
}

int main()
{
	long long t, T;
	long long i;
	long long cx, cy;
	long long ny;
	
	scanf( "%lld", &T );
	for ( t = 1; t <= T; t++ )
	{
		scanf( "%lld %lld %lld", &n, &w, &l );
		for ( i = 1; i <= n; i++ )
		{
			scanf( "%lld", &r[i].first );
			r[i].second = i;
		}
		
		memset( x, -1, sizeof( x ) );
		memset( y, -1, sizeof( y ) );
		
		sort( r + 1, r + n + 1, greater<pii>() );
		
		printf( "Case #%lld: ", t );
		
		cx = cy = 0;
		put( r[1].second, cx, cy );
		ny = r[1].first;
		cy = cy + r[1].first;
		//fprintf( stderr, "CASE %lld\n", r[1].first );
		for ( i = 2; i <= n; i++ )
		{
			//fprintf( stderr, "%lld\n", r[i].first );
			if ( cx >= w ) while ( 1 );
			if ( cy + r[i].first <= l )
			{
				cy = cy + r[i].first;
				put( r[i].second, cx, cy );
				cy = cy + r[i].first;
			}
			else
			{
				cx = ny + r[i].first;
				if ( cx >= w ) while ( 1 );
				cy = 0;
				put( r[i].second, cx, cy );
				ny = cx + r[i].first;
				cy = cy + r[i].first;
			}
		}
		
		for ( i = 1; i < n; i++ )
		{
//			fprintf( stderr, "%lld %lld %lld __ %lld %lld\n", i, x[i], y[i], w, l );
			if ( x[i] > w || y[i] > l || x[i] < 0 || y[i] < 0 ) while ( 1 );
			printf( "%lld.0 %lld.0 ", x[i], y[i] );
		}
		i = n;
		if ( x[i] > w || y[i] > l || x[i] < 0 || y[i] < 0 ) while ( 1 );
		printf( "%lld.0 %lld.0\n", x[n], y[n] );
	}
	return 0;
}
