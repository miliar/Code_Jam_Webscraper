/*
	Author: Ali-Amir Aldan
	Problem: Watersheds
	Contest: Google Code Jam Q.Round
*/
#include <cstdio>
#include <iostream>

int n, m, T, a[ 101 ][ 101 ];
char c, res[ 101 ][ 101 ];
using std::min;

int minimal( int x1,int y1,int x2,int y2,int x3,int y3,int x4,int y4 )
{
	int res=1000000000;
	if( x1<n )
		res=min( res,a[ x1 ][ y1 ] );
	if( y2<m )
		res=min( res,a[ x2 ][ y2 ] );
	if( x3>=0 )
		res=min( res,a[ x3 ][ y3 ] );
	if( y4>=0 )
		res=min( res,a[ x4 ][ y4 ] );
	return res;
}

char dfs( int x,int y )
{
	if( res[ x ][ y ]!=' ' )
		return res[ x ][ y ];
	int val=minimal( x+1, y, x, y+1, x-1, y, x, y-1 );
	if( val>=a[ x ][ y ] )
		res[ x ][ y ]=c++;
	else
	if( x>0 && a[ x-1 ][ y ]==val )
		res[ x ][ y ]=dfs( x-1, y );
	else
	if( y>0 && a[ x ][ y-1 ]==val )
		res[ x ][ y ]=dfs( x, y-1 );
	else
	if( y+1<m &&a[ x ][ y+1 ]==val )
		res[ x ][ y ]=dfs( x, y+1 );
	else
	if( x+1<n && a[ x+1 ][ y ]==val )
		res[ x ][ y ]=dfs( x+1, y );
	return res[ x ][ y ];
}

int main()
{
	freopen( "input.txt","r",stdin );
	freopen( "output.txt","w",stdout );
	scanf( "%d",&T );
	for( int sw=0;sw<T;sw++ )
	{
		scanf( "%d%d",&n,&m );
		c='a';
		for( int i=0;i<n;i++ )
			for( int j=0;j<m;j++ )
				scanf( "%d",&a[ i ][ j ] );
		for( int i=0;i<n;i++ )
			for( int j=0;j<m;j++ )
				res[ i ][ j ]=' ';
		for( int i=0;i<n;i++ )
			for( int j=0;j<m;j++ )
				dfs( i,j );
		printf( "Case #%d: \n",sw+1 );
		for( int i=0;i<n;i++ )
		{
			for( int j=0;j<m;j++ )
				printf( "%c ",res[ i ][ j ] );
			printf( "\n" );
		}
	}
	return 0;
}
