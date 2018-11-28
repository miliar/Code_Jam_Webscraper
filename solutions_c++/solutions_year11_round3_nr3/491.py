#include <iostream>
#include <cstdio>
using namespace std;

int n, num[ 10010 ], l, h;

int sol()
{
	for ( int i = l; i <= h; ++i )
	{
		bool flag = 1;
		for ( int j = 0; j < n; ++j )
		{
			int MAX = max( i, num[ j ] );
			int MIN = min( i, num[ j ] );
			if ( MAX % MIN )
			{
				flag = 0;
				break;
			}

		
		}
		if ( flag )
			return i;
	}
	return -1;
}


int main()
{
	freopen( "C.out", "w", stdout );
	int t;
	scanf( "%d", &t );

	for ( int k = 1; k <= t; ++k )
	{
		scanf( "%d %d %d", &n, &l, &h );

		for ( int i = 0; i < n; ++i )
			scanf( "%d", &num[ i ] );

		int ret = sol();

		if ( ret != -1 )
			printf( "Case #%d: %d\n", k, ret );
		else
			printf( "Case #%d: NO\n", k );
	}
	return 0;
}






