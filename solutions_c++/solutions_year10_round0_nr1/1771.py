#include <stdio.h>
#include <string.h>

char ans[ 10 ];

unsigned mass[ 31 ];

void work()
{
	mass[ 1 ] = 1;
	for(int i = 2;i <= 30;++i)
	{
		mass[ i ] = 2 * mass[ i - 1 ] + 1;
	}
}

int main()
{
	freopen( "A-large.in" , "r" , stdin );
	freopen( "A-large.out" , "w" , stdout );
	
	work();

	int t , n , k;
	scanf( "%d" , &t );

	for(int test = 1;test <= t;++test)
	{
		scanf( "%d%d" , &n , &k );
	k %= (mass[ n ] + 1);
		if( k < mass[ n ] )
			strcpy( ans , "OFF" );
		else
		{
			if( k == mass[ n ] )
				strcpy( ans , "ON"  );
			else
			{
				k -= mass[ n ] + 1;
			}
		}
		printf( "Case #%d: %s\n" , test , ans );
	}


	return 0;
}