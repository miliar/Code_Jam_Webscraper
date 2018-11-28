#include "stdafx.h"
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <utility>
#include <math.h>

using namespace std;

int n;
vector<int> G[ 1010 ];
bool used[1010];

bool dfs( int node )
{
	used[ node ] = true;
	bool res = false;
	for ( int i =0; !res && i < G[node].size(); i++ )
	{
		int to = G[node][i];
		if ( used[to] ) res = true;
		else res = dfs( to );
	}
	return res;
}

int main()
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w+", stdout );

	int tc; scanf( "%d", &tc );
	for ( int _=0; _<tc; _++ )
	{
		scanf( "%d", &n );

		for ( int i =0; i < n; i++ )
		{
			int m; scanf( "%d", &m );
			G[ i ].clear();
			for ( int j = 0; j < m; j++ )
			{
				int x; scanf( "%d", &x );
				G[ i ].push_back(--x);
			}
		}
		bool yes = false;
		for ( int i = 0; !yes && i < n; i++ )
		{
			memset( used, false, sizeof(used) );
			yes = dfs(i);
		}

		printf( "Case #%d: %s\n", _+1, yes?"Yes":"No" );
	}

	return 0;
}
