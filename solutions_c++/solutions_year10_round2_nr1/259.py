#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <string>
#include <map>
#include <set>
#include <algorithm>
using namespace std;
#define N 10000
int n, m, size;
set<string> que;

int main( )
{
	freopen( "A-small.in", "r", stdin );
	freopen( "A-small.out", "w", stdout );
	char str[200];
	string name, path;
	int t, ca, i, j, k, l, u, v;
	scanf( "%d", &ca );
	for ( t = 1; t <= ca; t++ )
	{
		scanf( "%d%d", &n, &m );
		que.clear( );
		for ( i = 0; i < n; i++ )
		{
			scanf( "%s", str );
			path.clear( );
			l = strlen( str );
			for ( j = 0; j < l; )
			{
				if ( str[j] == '/' )
				{
					j++;
					continue;
				}
				for ( k = j+1; k < l && str[k] != '/'; k++ );
				name.clear( );
				for ( u = j; u < k; u++ ) name.push_back( str[u] );
				path+=name;
				que.insert( path );
				j = k;
			}
		}
		v = que.size( );
		for ( i = 0; i < m; i++ )
		{
			scanf( "%s", str );
			path.clear( );
			l = strlen( str );
			for ( j = 0; j < l; )
			{
				if ( str[j] == '/' )
				{
					j++;
					continue;
				}
				for ( k = j+1; k < l && str[k] != '/'; k++ );
				name.clear( );
				for ( u = j; u < k; u++ ) name.push_back( str[u] );
				path+=name;
				que.insert( path );
				j = k;
			}
		}
		printf( "Case #%d: %d\n", t, que.size( )-v );
	}
}
