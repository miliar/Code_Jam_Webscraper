#include <cstdio>

int a [ 1001 ];
bool f [ 1001 ];

int main ( )
{
	freopen ( "input.txt", "r", stdin );
	freopen ( "output.txt", "w", stdout );
	
	int i, x, s, n, T, ans;
	
	scanf ( "%d", &T );
	for ( int o = 1; o <= T; ++o )
	{
		printf ( "Case #%d: ", o );
		
		scanf ( "%d", &n );
		for ( i = 1; i <= n; ++i )
			scanf ( "%d", &a[i] ), f[i] = true;
		
		ans = 0;
		for ( i = 1; i <= n; ++i )
			if ( f[i] )
			{
				x = a[i];
				if ( x != i ) ++ans;
				while ( x != i )
					++ans, f[x] = false, x = a[x];
			}
		printf ( "%d.000000\n", ans);
	}
	return 0;
}
