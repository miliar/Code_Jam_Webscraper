#include <iostream>
#include <cstdio>
using namespace std;


long long int gcd( long long int a, long int b )
{
	if ( !a || !b )
		return a ? a : b;
	while ( ( a %= b ) && ( b %= a ) )
		;
	return a + b;
}



int main()
{
	freopen( "A.out", "w", stdout );
	long long int t, n, d, g;
	scanf( "%lld", &t );

	for ( int k = 1; k <= t; ++k )
	{

		scanf( "%lld %lld %lld", &n, &d, &g );
		
		if ( (g == 100 && d != 100 ) || ( !g && d ) )
		{
			printf( "Case #%d: Broken\n", k );
			continue;
		}

		if ( g == 100 && !d )
		{
			printf( "Case #%d: Possible\n", k );
			continue;
		}

		int x = gcd( d, 100 );
		

		if ( n >= ( 100 / x ) )
			printf( "Case #%d: Possible\n", k );
		else
			printf( "Case #%d: Broken\n", k );

		
		/*
		bool flag = 0;
		for ( int i = 1; i <= n; ++i )
		{
			int temp = i * d;
			
			if ( !( temp % 100 ) )
			{
				flag = 1;
				break;
			}
		}



		if ( !flag )
			printf( "Case #%d: Broken\n", k );
		else 
			printf( "Case #%d: Possible\n", k );
			*/
	}
	return 0;
}



