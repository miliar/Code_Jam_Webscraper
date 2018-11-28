#include <cstdio>

int a[10001];

int main ( )
{
	freopen ( "input.txt", "r", stdin );
	freopen ( "output.txt", "w", stdout );
	
	int T;
	
	scanf ( "%d", &T );
	for ( int o = 1; o <= T; ++o )
	{
		printf ( "Case #%d: ", o );
		
		int L, R, n;
		
		scanf ( "%d%d%d", &n, &L, &R );
		for ( int i = 1; i <= n; ++i )
			scanf ( "%d", &a[i] );
		
		int i;
		for ( i = L; i <= R; ++i )
		{
			int j;
			for ( j = 1; j <= n; ++j )
				if ( !( i % a[j] == 0 || a[j] % i == 0 ) )
					break;
			if ( j > n )
			{
				printf ( "%d\n", i );
				break;
			}
		}
		if ( i > R )
			printf ( "NO\n" );
	}
	return 0;
}
