#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;


int main()
{
	int test = 0;

	freopen( "A.out", "w", stdout );

	scanf( "%d", &test );

	for ( int t = 0; t < test; ++t )
	{
		int n;
		queue< pair< int, int > > B, O;

		scanf( "%d", &n );
		int x;
		char c;

		for ( int i = 0; i < n; ++i )
		{
			scanf( " %c %d", &c, &x );
			if ( c == 'B' )
				B.push( pair< int, int >( i, x ) );
			else
				O.push( pair< int, int >( i, x ) );
		}


		int cnt = 0, posB = 1, posO = 1;
		
		while ( !B.empty() || !O.empty() )
		{
			if ( ( !B.empty() && !O.empty() && O.front().first < B.front().first ) || B.empty() )
			{
				int step = abs( posO - O.front().second ) + 1;
				cnt += step;
				posO = O.front().second;
				O.pop();

				if ( !B.empty() )
				{
					if ( B.front().second < posB )
						posB = max( posB - step, B.front().second );
					else
						posB = min( posB + step, B.front().second );
				}
			}
			else if ( ( !B.empty() && !O.empty() && B.front().first < O.front().first ) || O.empty() )
			{
				int step = abs( posB - B.front().second ) + 1;
				cnt += step;

				posB = B.front().second;
				B.pop();
				if ( !O.empty() )
				{
					if ( O.front().second < posO )
						posO = max( posO - step, O.front().second );
					else
						posO = min( posO + step, O.front().second );
				}
			}
		}
				
		printf( "Case #%d: %d\n", t + 1, cnt );
		
	}
	return 0;
}
		





