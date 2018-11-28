#include <iostream>
using namespace std;

int n, k;


int main()
{
	
	int t = 0, x, test;
	
	freopen( "A-large.in", "r", stdin );
	freopen( "Aout.txt", "w", stdout );
	
	scanf( "%d", &test );
	
	while ( test-- )
	{
		
		scanf( "%d %d", &n, &k );
		
		x = 1 << n;
		
		if ( k % x != x - 1 )
			printf( "Case #%d: OFF\n", ++t );
		else
			printf( "Case #%d: ON\n", ++t );
	}
	return 0;
}
			
