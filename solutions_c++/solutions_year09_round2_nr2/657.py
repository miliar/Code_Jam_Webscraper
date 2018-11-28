#include "stdio.h"
#include <vector>
#include <set>
#include <strstream>
#include <string>
#include <algorithm>
using namespace std;


int main()
{
	freopen( "test.in", "r", stdin );
	freopen( "test.out", "w", stdout );

	int n;
	scanf( "%d", &n );
	for( int cn = 1; cn <= n; ++cn )
	{
		char w[1000];
		scanf( "%s", w );
		int l = strlen(w);
		int i;
		for( i = l-1; i>0; --i )
		{
			if( w[i] > w[i-1] )
				break;
		}
		printf( "Case #%d: ", cn );

		if( i > 0 )
		{
			int j;
			for( j=l-1; j>=0; --j )
				if( w[j] > w[i-1] )
					break;
			swap( w[i-1], w[j] );
			sort( w+i, w+l );
			printf( "%s\n", w );
		}
		else
		{
			sort( w, w+l );
			int i = 0;
			for( ; w[i] == '0'; ++i )
				;
			printf( "%c", w[i] );
			for( int j=0; j<=i; ++j )
			{
				printf( "0" );
			}
			printf( "%s\n", w+i+1 );
		}
	}
	return 0;

}