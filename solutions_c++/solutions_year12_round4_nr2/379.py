#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#define MAXN 20000
using namespace std;

typedef struct CIRCLE
{
	int r;
	int index;
	int x, y;
};
CIRCLE cir[ MAXN ];

bool cmp( CIRCLE a, CIRCLE b )
{
	return a.r > b.r;
}


bool cmp2( CIRCLE a, CIRCLE b )
{
	return a.index < b.index;
}

int N, W, L;

int main()
{
	freopen( "B-large.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int datacase, t = 0;
	scanf( "%d", &datacase );
	while( datacase-- )
	{
		scanf( "%d%d%d", &N, &W, &L );
		for( int i = 0; i < N; i++ )
		{
			scanf( "%d", &cir[ i ].r );
			cir[ i ].index = i;
		}
		sort( cir, cir+N, cmp );
		int nowx = 0, nowy = 0, y = 0;
		for( int i = 0; i < N; i++ )
		{
			if( nowx == 0 )
			{
				cir[ i ].x = 0;
				cir[ i ].y = 0;
				y = nowx = cir[ i ].r;
			}
			else if( nowx + cir[ i ].r <= W )
			{
				cir[ i ].x = nowx + cir[ i ].r;
				cir[ i ].y = nowy;
				nowx += cir[ i ].r*2;
			}
			else
			{
				nowy += y + cir[ i ].r;
				cir[ i ].x = 0;
				cir[ i ].y = nowy;
				nowx = cir[ i ].r;
			}
		
		}
		sort( cir, cir+N, cmp2 );
		
		printf ( "Case #%d:", ++t );
		
		for ( int i = 0; i < N; i++ ) 
		{
			printf ( " %d.0 %d.0", cir[ i ].x, cir[ i ].y ) ;
		}
		printf ( "\n" ) ;			
		
		
		
	}
	
	return 0;
}
