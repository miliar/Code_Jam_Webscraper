/*
	Author: Ali-Amir Aldan
	Problem: Bribe The Prisoners
	Contest: Google Code Jam Round 1
*/
#include <cstdio>
#include <iostream>
#include <algorithm>
#define INF 1000000000
using namespace std;

int res;
int val[ 2000 ];
int P, Q, T;
bool was[ 2000 ];

void init()
{
	memset( was, 0, sizeof( was ) );
	res=INF;
}

void dfs( int u, int sum )
{
	int r;
	if( u==Q )
	{
		res=min( res, sum );
		return;
	}
	for( int i=0;i<Q;i++ )
		if( !was[ val[ i ] ] )
		{
			was[ val[ i ] ]=1;
			r=0;
			for( int l=val[ i ]+1;!was[ l ] && l<=P;l++ )
				++r;
			for( int l=val[ i ]-1;!was[ l ] && l>0;l-- )
				++r;
			dfs( u+1, sum+r );
			was[ val[ i ] ]=0;
		}
}

int main()
{
	freopen( "input.txt","r",stdin );
	freopen( "output.txt","w",stdout );
	scanf( "%d", &T );
	for( int sw=0;sw<T;sw++ )
	{
		scanf( "%d%d", &P, &Q );
		init();
		for( int i=0;i<Q;i++ )
			scanf( "%d", &val[ i ] );
		val[ Q+1 ]=P+1;
		dfs( 0,0 );
		printf( "Case #%d: %d\n", sw+1, res );
	}
	return 0;
}
