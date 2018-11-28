#include <cstdio>

char map[51][51];
char ans[51][51];

int main ( )
{
	freopen ( "input.txt", "r", stdin );
	freopen ( "output.txt", "w", stdout );
	
	int T;
	
	scanf ( "%d", &T );
	for ( int o = 1; o <= T; ++o )
	{
		printf ( "Case #%d:\n", o );
		
		int i, j, n, m;
		
		scanf ( "%d%d%*c", &n, &m );
		for ( i = 0; i < n; ++i )
			scanf ( "%s", map[i] );
		for ( i = 0; i < n; ++i )
			for ( j = 0; j <= m; ++j )
				ans[i][j] = '\0';
		
		int f = 1;
		for ( i = 0; f && i < n; ++i )
			for ( j = 0; f && j < m; ++j )
				if ( ans[i][j] == '/' || ans[i][j] == '\\' )
					continue;
				else if ( map[i][j] == '.' )
					ans[i][j] = '.';
				else if ( j == m - 1 || map[i][j + 1] == '.' ||
					      i == n - 1 || map[i+1][j] == '.' ||
						  map[i+1][j+1] == '.' )
					f = 0;
				else
				{
					ans[i][j] = '/';
					ans[i][j+1] = '\\';
					ans[i+1][j] = '\\';
					ans[i+1][j+1] = '/';
					++j;
				}
		
		if ( f )
			for ( i = 0; i < n; ++i )
				printf ( "%s\n", ans[i] );
		else printf ( "Impossible\n" );
	}
	return 0;
}
