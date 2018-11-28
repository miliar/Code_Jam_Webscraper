/*
	Author: Ali-Amir Aldan
	Problem: Decision_tree
	Contest: Google Code Jam Round 1
*/
#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

char s[ 1000 ], x[ 1000 ];
int last;
int dl[ 1000 ];
char feature[ 1000 ][ 100 ], animals[ 100 ][ 100 ];
bool notleaf[ 1000 ];
double w[ 1000 ], res;
int L, T, y;

void init()
{
	memset( dl,0,sizeof( dl ) );
	y=0;
	memset( notleaf,0,sizeof( notleaf ) );
}

double convert()
{
	double x=0, st, y=0;
	int i;
	for( i=0; s[ i ]!='.' && i<last;i++ )
	{
	 	x*=10;
	 	x+=s[ i ]-'0';
	}
	st=1;
	for( i=i+1; i<last;i++ )
	{
		y*=10;
		y+=s[ i ]-'0';
		st*=10;
	}
	st=y/st;
	x=x+st;
/*	for( int i=0;i<last;i++ )
		printf( "%c",s[ i ] );
	printf( "\n" );*/
	return x;
}

void getstring( int root, int &L )
{
	char c;
	for( c=' ';c!='('; )
	{
		scanf( "%c",&c );
		if( c=='\n' )
			--L;
	}
	for( c=' '; c==' ' || c=='\n'; )
	{
		scanf( "%c",&c );
		if( c=='\n' )
			--L;
	}
	last=1;
	s[ 0 ]=c;
	for( c='.'; c!=' ' && c!='\n' && c!=')' ; )
	{
		scanf( "%c",&c );
		if( c=='\n' )
			--L;
		s[ last++ ]=c;
	}
	--last;
	double x=convert();
	w[ root ]=x;
	for( ; c==' ' || c=='\n'; )
	{
		scanf( "%c",&c );
		if( c=='\n' )
			--L;
	}
	if( c==')' )
		return;
	notleaf[ root ]=1;
	feature[ root ][ dl[ root ]++ ]=c;
	for( c='.'; c!=' ' && c!='\n'; )
	{
		scanf( "%c",&c );
		if( c=='\n' )
			--L;
		feature[ root ][ dl[ root ]++ ]=c;
	}
	--dl[ root ];
	getstring( root*2+1, L );
	getstring( root*2+2, L );
	for( c=' '; c!=')'; )
	{
		scanf( "%c",&c );
		if( c=='\n' )
			--L;
	}
}

void dfs( int root, double &v )
{
	bool b=0;
	v*=w[ root ];
//	printf( "here=%d\n",root );
//	printf( "w=%0.7lf\n",w[ root ] );
	if( notleaf[ root ] )
	{
		for( int i=0;i<y;i++ )
		{
			b=0;
			if( strlen( animals[ i ] )!=dl[ root ] )
				b=1;
			else
			for( int j=0;j<dl[ root ];j++ )
				if( animals[ i ][ j ]!=feature[ root ][ j ] )
				{
					b=1;
					break;
				}					
			if( !b )
				break;
		}
		if( !b && y>0 )
			dfs( root*2+1,v );
		else
			dfs( root*2+2,v );
	}
}

int main()
{
	freopen( "input.txt","r",stdin );
	freopen( "output.txt","w",stdout );
	scanf( "%d\n",&T );
	char c;
	for( int sw=0;sw<T;sw++ )
	{
		init();
		printf( "Case #%d:\n", sw+1 );
        	scanf( "%d\n",&L );
        	getstring( 0, L );
        	for( ;L>0;L-- )
        		scanf( "\n" );
		scanf( "%d\n",&L );
		for( int j=0;j<L;j++ )
		{
			scanf( "%s %d%c", x, &y, &c );
			for( int i=0;i<y;i++ )
				scanf( "%s%c", animals[ i ], &c );
			res=1.0;
			dfs( 0, res );
			printf( "%0.7lf\n", res );
		}
        }
	return 0;
}
