#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

const int inf = 1000000000;
int n,w,h;
int a[256][256];
int c[256][256];

bool was[256][256];
int id;
int t[100000];

int f(int x,int y)
{
	if( was[x][y] ) return c[x][y];
	was[x][y] = true;
	
	int min = a[x][y];
	
	if( a[x-1][y] < min ) min = a[x-1][y];
	if( a[x][y-1] < min ) min = a[x][y-1];
	if( a[x][y+1] < min ) min = a[x][y+1];
	if( a[x+1][y] < min ) min = a[x+1][y];
	
	if( min == a[x][y] )
	{
		id++;
		c[x][y] = id;
	} else
	{
		if( a[x-1][y] == min ) c[x][y] = f(x-1,y); else
		if( a[x][y-1] == min ) c[x][y] = f(x,y-1); else
		if( a[x][y+1] == min ) c[x][y] = f(x,y+1); else
		if( a[x+1][y] == min ) c[x][y] = f(x+1,y);
	}
	
	return c[x][y];
}

int main()
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	
	scanf( "%d", &n );
	
	for( int i = 0; i < n; i++ )
	{
		scanf( "%d%d",&h,&w );
		
		memset( a, 0, sizeof a );
		for(int x = 0; x < 256; x++)
			for(int y = 0; y < 256; y++)
				a[x][y] = inf;
		
		for(int x = 1; x <= h; x++)
			for(int y = 1; y <= w; y++) scanf( "%d",&a[x][y] );
		
		
		memset( c, 0, sizeof c );
		memset( was, 0, sizeof was );
		id = 1;
		
		for(int x = 1; x <= h; x++)
			for(int y = 1; y <= w; y++)
			{
				c[x][y] = f(x,y);
			}
			
		int alp = 'a';
		
		memset( t, 0, sizeof t );
		
		printf("Case #%d:\n",i+1);
		
		for(int x = 1; x <= h; x++)
		{
			for(int y = 1; y <= w; y++)
			{
				if( t[ c[x][y] ] == 0 )
				{
					t[ c[x][y] ] = alp;
					alp++;
				}
				
				printf("%c ",t[ c[x][y] ]);
				
			}
			printf("\n");
		}
	}
	
	
	
	return 0;
}