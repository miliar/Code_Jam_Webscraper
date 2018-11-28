#include <cstdio>

int main ( )
{
	freopen ( "input.txt", "r", stdin );
	freopen ( "output.txt", "w", stdout );
	
	int t, x, p, s, n, T;
	
	scanf ( "%d", &T );
	for ( int o = 1; o <= T; ++o )
	{
		printf ( "Case #%d: ", o);
		scanf ( "%d%d", &n, &x );
		p = s = x;
		for ( int i = 1; i < n; ++i )
			scanf ( "%d", &t ), x <?= t, p ^= t, s += t;
		if ( p )
			printf ( "NO\n" );
		else printf ( "%d\n", s - x );
	}
	return 0;
}
