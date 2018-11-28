#include <iostream>
using namespace std;

long long int st[ 100 ], v[ 100 ];
int n, tg, T, end, total;


int main()
{
	
	int i, j, k, t, test = 0;
	
	
	freopen( "B-large.in", "r", stdin );
	freopen( "B-out.txt", "w", stdout );
	
	scanf( "%d", &t );
	
	while ( t-- )
	{
		scanf( "%d %d %lld %d", &n, &tg, &end, &T );
		
		for ( i = 1; i <= n; ++i )
			scanf( "%lld", &st[ i ] );
		
		for ( i = 1; i <= n; ++i )
			scanf( "%lld", &v[ i ] );
		
		for ( i = 1; i <= n; ++i )
		{
			st[ i ] += v[ i ] * T;
		}
		
		total = 0;
		for ( i = n; i && tg; --i )
		{
			if ( st[ i ] >= end )
				--tg;
			else
			{
				for ( j = i - 1; j; --j )
				{
					if ( st[ j ] >= end )
					{
						--tg;
						total += i - j;
						swap( st[ i ], st[ j ] );
						break;
					}
				} 
			}
		}
		
		if ( !tg )
			printf( "Case #%d: %d\n", ++test, total );
		else
			printf( "Case #%d: IMPOSSIBLE\n", ++test );
	}
	
	return 0;
}
