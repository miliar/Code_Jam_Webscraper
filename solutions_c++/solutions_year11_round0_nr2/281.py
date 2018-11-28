#include <cstdio>
#include <cstring>

char a [ 27 ][ 27 ], ans [ 101 ];
bool b [ 27 ][ 27 ];

int main ( )
{
	freopen ( "input.txt", "r", stdin );
	freopen ( "output.txt", "w", stdout );
	
	int i, j, s, n, T;
	char x, y, z;
	
	scanf ( "%d", &T );
	for ( int o = 1; o <= T; ++o )
	{
		if ( o == 50 )
			o = 50;
		printf ( "Case #%d: ", o);
		memset ( a, 0, sizeof ( a ) );
		memset ( b, false, sizeof ( b ) );
		scanf ( "%d%*c", &n );
		for ( i = 0; i < n; ++i )
			scanf ( "%c%c%c%*c", &x, &y, &z ), a [ x-'A' ][ y-'A' ] =
											a [ y-'A' ][ x-'A' ] = z-'A';
		scanf ( "%d%*c", &n );
		for ( i = 0; i < n; ++i )
			scanf ( "%c%c%*c", &x, &y ), b [ x-'A' ][ y-'A' ] = 
									  b [ y-'A' ][ x-'A' ] = true;
		scanf ( "%d%*c", &n ); s = 0;
		for ( i = 0; i < n; ++i )
		{
			scanf ( "%c", &y );
			ans [ ++s ] = y;
			while ( s && a [ ans[s]-'A' ][ ans [s-1]-'A' ] )
				ans [ s-1 ] = a[ans[s]-'A'][ans [s-1]-'A']+'A', --s;
			for ( j = 1; j < s; ++j )
				if ( b [ ans[j]-'A' ][ ans[s]-'A' ] )
					s = 0;
		}
		printf ( "[" );
		for ( i = 1; i < s; ++i )
			printf ( "%c, ", ans [ i ] );
		if ( s ) printf ( "%c", ans [ s ] );
		printf ( "]\n" );
	}
	return 0;
}
