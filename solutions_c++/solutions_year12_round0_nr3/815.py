#include "stdafx.h"
//#include <stdio.h>
//#include <cstring>
//#include <string>
//#include <vector>
//#include <map>
//#include <algorithm>
#include <utility>
//#include <iostream>
//#include <sstream>
//#include <math.h>

using namespace std;

int main()
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w+", stdout );

	int TC; scanf( "%d", &TC );
	for ( int _ = 0; _ < TC; _++ )
	{
		int A, B; scanf( "%d%d", &A, &B );
		long long res = 0LL;
		int l=0, a=A, deg[ 10 ];
		for ( deg[0]=1; a; l++, a/=10, deg[l] = deg[l-1]*10 ){ ; }
		for ( int i = A; A > 9 && i <= B; i++ )
		{
			int xx[ 10 ], nn=0;
			for ( int j = 0; j < l-1; j++ )
			{
				int x = i % deg[j+1];
				x = deg[l-1-j]*x + ( i/deg[j+1] );
				bool yes = false;
				for ( int k = 0; !yes && k < nn; k++ )
					yes = ( xx[ k ] == x );
				xx[ nn++ ] = x;
				res += ( !yes && i < x && x <= B );
			}
		}
		printf( "Case #%d: %lld\n", _+1, res );
	}

	return 0;
}
