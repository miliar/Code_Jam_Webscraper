#include <cstdio>

int main ( )
{
	freopen ( "input.txt", "r", stdin );
	freopen ( "output.txt", "w", stdout );
	int T;
	
	scanf ( "%d", &T );
	for ( int o = 1; o <= T; ++o )
	{
		printf ( "Case #%d: ", o );
		
		int pd, pg;
		long long n;
		
		scanf ( "%I64d%d%d", &n, &pd, &pg );
		
		if ( ( pd != 100 && pg == 100 ) || ( pd != 0 && pg == 0 ) )
		{
			printf ( "Broken\n" );
			continue;
		}
		
		int x = 1;
		if ( pd % 4 == 0 ) x = 4;
		else if ( pd % 2 == 0 ) x = 2;
		if ( pd % 25 == 0 ) x *= 25;
		else if ( pd % 5 == 0 ) x *= 5;
		int d = 100 / x;
		
		if ( d > n )
			printf ( "Broken\n" );
		else printf ( "Possible\n" );
	}
	return 0;
}
