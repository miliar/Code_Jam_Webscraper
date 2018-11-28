#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
#define N 100
int n, m, b, limit;
int pos[N], vol[N], mark[N];

bool valid( )
{
	int i, j, cnt = 0;
	memset( mark, 0, sizeof(mark) );
	for ( i = 0; i < n; i++ )
	{
		j = b-pos[i];
		if ( j%vol[i] == 0 ) j = j/vol[i];
		else j = j/vol[i]+1;
		if ( j <= limit )
		{
			mark[i] = 1;
			cnt++;
		}
	}
	return cnt >= m;
}

int solve( )
{
	int i, j, k = 0, pre = n, cnt = 0;
	for ( i = n-1; i >= 0; i-- )
	{
		if ( k == m ) break;
		if ( mark[i] )
			k++;
		else
			cnt += m-k;
	}
	return cnt;
}

int main( )
{
	int t, ca;
	freopen( "B-large.in", "r", stdin );
	freopen( "B-large.out", "w", stdout );
	scanf( "%d", &ca );
	for ( t = 1; t <= ca; t++ )
	{
		scanf( "%d%d%d%d", &n, &m, &b, &limit );
		for ( int i = 0; i < n; i++ ) scanf( "%d", pos+i );
		for ( int i = 0; i < n; i++ ) scanf( "%d", vol+i );
		if ( valid( ) == false )
		{
			printf( "Case #%d: IMPOSSIBLE\n", t );
			continue;
		}
		printf( "Case #%d: %d\n", t, solve( ) );
	}
}
