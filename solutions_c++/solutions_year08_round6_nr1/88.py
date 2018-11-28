#define _CRT_SECURE_NO_WARNINGS

#include<vector>
#include<map>
#include<string>
#include<cstdio>
#include<cstring>
#include<cstdlib>

using namespace std;

class Pos
{
public:
	int x, y, p;
};

Pos p[1010];
char buf[10000];
int n;

#define INF 1000000

int a1, a2, a3, a4;
int b1, b2, b3, b4;

void try_it()
{
}

void make_it()
{
	int i, j;
	scanf( "%d", &n );
	for( i = 0; i < n; ++i )
	{
		scanf( "%d %d", &p[i].x, &p[i].y );
		scanf( "%s", buf );
		if( buf[0] == 'B' )
			p[i].p = 1;
		else
		{
			p[i].p = 0;
			scanf( "%s", buf );
		}
	}

	a1 = -INF-1;
	a2 = INF+1;
	a3 = INF+1;
	a4 = -INF-1;
	b1 = INF;
	b2 = -INF;
	b3 = -INF;
	b4 = INF;

	for( i = 0; i < n; ++i )
		for( j = i + 1; j < n; ++j )
			if( p[j].p > p[i].p )
				swap( p[i], p[j] );
	for( i = 0; i < n && p[i].p == 1; ++i )
	{
		if( p[i].x > a1 )
			a1 = p[i].x;
		if( p[i].x < a3 )
			a3 = p[i].x;
		if( p[i].y > a4 )
			a4 = p[i].y;
		if( p[i].y < a2)
			a2 = p[i].y;
	}

	for( ; i < n && p[i].p == 0; ++i )
	{
		if( p[i].x > b3 && p[i].x < a3 && p[i].x < a1 && p[i].y >= a2 && p[i].y <= a4)
			b3 = p[i].x;
		if( p[i].x < b1 && p[i].x > a1 && p[i].x > a3 && p[i].y >= a2 && p[i].y <= a4 )
			b1 = p[i].x;
		if( p[i].y > b2 && p[i].y < a2 && p[i].y < a4 && p[i].x >= a3 && p[i].x <= a1 )
			b2 = p[i].y;
		if( p[i].y < b4 && p[i].y > a4 && p[i].y > a2 && p[i].x >= a3 && p[i].x <= a1 )
			b4 = p[i].y;
	}

	int m, x, y;
	scanf( "%d", &m );
	for( i = 0; i < m; ++i )
	{
		scanf( "%d %d", &x, &y );
		if( x <= a1 && x >= a3 && y >= a2 && y <= a4 )
			printf( "BIRD\n" );
		else if( p[0].p == 0 || ( x < b1 && x > b3 && y > b2 && y < b4 ) )
			printf( "UNKNOWN\n" );
		else
			printf( "NOT BIRD\n" );

	}
}

int main()
{
	freopen( "a1.in", "r", stdin );
	freopen( "out.out", "w", stdout );

	int test = 0;
	scanf( "%d", &test );
	for( int i = 1; i <= test; ++i )
	{
		printf( "Case #%d:\n", i );
		make_it();
	}
	return 0;
}
