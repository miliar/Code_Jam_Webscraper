#include <cstdio>

int abs ( int x )
{
	return x < 0 ? -x : x;
}

int main ( )
{
	freopen ( "input.txt", "r", stdin );
	freopen ( "output.txt", "w", stdout );
	
	int i, t, x, p1, p2, s1, s2, ans, n, T;
	char c;
	
	scanf ( "%d", &T );
	for ( int o = 1; o <= T; ++o )
	{
		scanf ( "%d%*c", &n );
		s1 = s2 = ans = 0; p1 = p2 = 1;
		for ( i = 1; i <= n; ++i )
		{
			scanf ( "%c%d%*c", &c, &x );
			if ( c == 'O' )
			{
				t = abs ( p1 - x ) + 1; p1 = x;
				if ( s1 >= t )
					++ans, ++s2;
				else ans += t - s1, s2 += t - s1;
				s1 = 0;
			}
			else
			{
				t = abs ( p2 - x ) + 1; p2 = x;
				if ( s2 >= t )
					++ans, ++s1;
				else ans += t - s2, s1 += t - s2;
				s2 = 0;
			}
		}
		printf ( "Case #%d: %d\n", o, ans );
	}
	return 0;
}
