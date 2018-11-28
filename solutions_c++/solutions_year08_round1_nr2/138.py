#include <stdio.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

int main()
{
	int casen, n, m, i, j;
	freopen( "d:\\temp\\out.txt", "w", stdout );
	freopen( "d:\\temp\\in.txt", "r", stdin );
	scanf( "%d", &casen );

	for( int k=1; k<=casen; ++k )
	{
		scanf( "%d", &n );
		scanf( "%d", &m );
		
		vector< map<int,bool> > request(m);
		vector<bool> sat(m, false);


		for( i=0; i<m; ++i )
		{
			int t;
			scanf( "%d", &t );
			for( j=0; j<t; ++j )
			{
				int a, b;
				scanf( "%d%d", &a, &b );
				request[i][a] = (bool)b;
			}
		}

		map<int,bool> ans;

		bool key = true;
		while(key)
		{
			for( i=0; i<m; ++i )
			{
				if( !sat[i] && request[i].size() == 1 )
				{
					break;
				}
			}

			if( i >= m )
			{
				break;
			}
		
			int milkshake = request[i].begin()->first;
			bool type = request[i].begin()->second;

			ans[milkshake] = type;

			for( i=0; i<m; ++i )
			{
				if( !sat[i] && request[i].find( milkshake ) != request[i].end() )
				{
					if( request[i][milkshake] == type )
					{
						sat[i] = true;
					}
					else
					{
						request[i].erase( milkshake );
						if( request[i].empty() )
						{
							key = false;
							break;
						}
					}
				}
			}//for
		}

		if( !key )
		{
			printf( "Case #%d: IMPOSSIBLE\n", k, ans );
		}
		else
		{
			printf( "Case #%d:", k );
			for( i=1; i<=n; ++i )
			{
				if( ans.find(i) != ans.end() )
				{
					printf( " %d", ans[i] );
				}
				else
				{
					printf( " 0" );
				}
			}
			printf( "\n" );
		}
	}

	return 0;

}