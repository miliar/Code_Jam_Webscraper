#include "stdafx.h"
#include <stdio.h>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <utility>
#include <iostream>
#include <sstream>
#include <math.h>
#include <iostream>

using namespace std;

int main()
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w+", stdout );

	int TC; scanf( "%d", &TC );
	for ( int _ = 0; _ < TC; _++ )
	{
		int N, S, P; scanf( "%d%d%d", &N, &S, &P );
		int a, res = 0;
		for ( int i = 0; i < N; i++ )
		{
			scanf( "%d", &a );
			//if (a >= ( 3*P-2 ) ) res++; else if ( a >= (3*P-4) && S ) res++, S--; continue;
			if ( a/3 >= P || !P ) res++;
			else if ( a >= P )
			{
				if ( abs( P - ( a - P ) / 2 ) < 2 ) res++;
				else if ( abs( P - ( a - P ) / 2 ) == 2 && S )
				{
					res++, S--;
				}
			}
		}
		printf( "Case #%d: %d\n", _+1, res );
	}

	return 0;
}
