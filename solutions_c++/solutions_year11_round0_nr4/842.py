#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int main()
{
	freopen( "D.out", "w", stdout );
	int test;
	scanf( "%d", &test );

	for ( int t = 0; t < test; ++t )
	{
		int n;
		scanf( "%d", &n );
		
		int cnt = 0, x;
		for ( int i = 0; i < n; ++i )
		{
			scanf( "%d", &x );
			if ( x - 1 != i )
				++cnt;
		}

		printf( "Case #%d: %d.000000\n", t + 1, cnt );
	}
	return 0;
}


