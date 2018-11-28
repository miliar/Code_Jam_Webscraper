#include<iostream>
#include<cstdlib>
using namespace std;

int  T,H,W;
int  maps[ 101 ][ 101 ];
int  smap[ 101 ][ 101 ];
bool sign[ 101 ][ 101 ];
char oput[ 101 ][ 101 ];
int  d[ 4 ][ 2 ] = { -1,0 , 0,-1 , 0,1 , 1,0 };

int value( int x , int y )
{
	int min_x = x;
	int min_y = y;
	int min = maps[ x ][ y ];
	for ( int k = 0 ; k < 4 ; ++ k )
	{
		int xp = x + d[ k ][ 0 ];
		int yp = y + d[ k ][ 1 ];
		if ( xp >= 0 && xp < H && yp >= 0 && yp < W && maps[ xp ][ yp ] < min )
		{
			min = maps[ xp ][ yp ];
			min_x = xp;
			min_y = yp;
		}
	}
	if ( min_x == x && min_y == y )
		return smap[ x ][ y ];
	else
		return value( min_x, min_y );
}

void floodfill( int x , int y , char A )
{
	sign[ x ][ y ] = true;
	oput[ x ][ y ] = A;
	for ( int k = 0 ; k < 4 ; ++ k )
	{
		int px = x + d[ k ][ 0 ];
		int py = y + d[ k ][ 1 ];
		if ( px >= 0 && px < H && py >= 0 && py < W && 
				!sign[ px ][ py ] && smap[ px ][ py ] == smap[ x ][ y ] )
			floodfill( px , py , A );
	}
}

int main()
{
	FILE *fp = fopen( "Watersheds.out" , "w" );
	cin >> T;
	for ( int p = 1 ; p <= T ; ++ p )
	{
		cin >> H >> W;
		for ( int i = 0 ; i < H ; ++ i )
		for ( int j = 0 ; j < W ; ++ j )
			cin >> maps[ i ][ j ];
		for ( int i = 0 ; i < H ; ++ i )
		for ( int j = 0 ; j < W ; ++ j )
			smap[ i ][ j ] = 100*i+j;
		for ( int i = 0 ; i < H ; ++ i )
		for ( int j = 0 ; j < W ; ++ j )
			smap[ i ][ j ] = value( i , j );
			
		memset( sign , 0 , sizeof( sign ) );
		char ch = 'a';
		for ( int i = 0 ; i < H ; ++ i )
		for ( int j = 0 ; j < W ; ++ j )
			if ( !sign[ i ][ j ] ){
				floodfill( i , j , ch );
			++ ch;
		}
		fprintf(fp,"Case #%d:\n",p);
		for ( int i = 0 ; i < H ; ++ i )
		{
			for ( int j = 0 ; j < W-1 ; ++ j )	
				fprintf(fp,"%c ",oput[ i ][ j ]);
			fprintf(fp,"%c\n",oput[ i ][ W-1 ]);
		}
	}
}
