#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//#define DEBUG


const int MAX_ALTITUDE = 10 - 1;
const int WALL = 0xffffff;


class matrix_2d
{
public:
	matrix_2d( int n, int m );
	~matrix_2d()
	{
		if( matrix != NULL )
		{
			delete [] matrix;
			matrix = NULL;
		}
	}
	
	int &operator()(int n, int m);
	
	int X(){
		return x;
	}

	int Y(){
		return y;
	}
	
	
private:
	int x;
	int y;
	int z;
	int *matrix;
};


matrix_2d::matrix_2d( int n, int m ) : matrix(NULL)
{
	x = n;
	y = m;
	
	matrix = new int[x*y];
	bzero( matrix, sizeof(int) * x * y );
}

int &matrix_2d::operator()(int n, int m)
{
	if( x * m + n > x * y )
	{
		puts("out of bound");
		return z;
	}
	
	return matrix[x * m + n];	
}





static void print_map( matrix_2d &map )
{
	int H = map.Y();
	int W = map.X();
	
	for( int y = 0; y < H; y++ )
	{
		for( int x = 0; x < W; x++ )
		{
			if( map(x,y) == WALL )
				printf("*");
			else if( 20000 <= map(x,y) && map(x,y) <= 20000 + 'z' )
				printf("%c", map(x,y) - 20000);
			else 
				printf("%d",map(x,y));
		}
		puts("");
	}
	puts("");
	puts("");
}


static void print_result( matrix_2d &map )
{
	int H = map.Y();
	int W = map.X();
	
	for( int y = 1; y < H - 1; y++ )
	{
		for( int x = 1; x < W - 1; x++ )
		{
			printf("%c ", map(x,y) );

		}
		puts("");
	}
}



static int determine_flow( matrix_2d &map, int x, int y )
{
	int current = map( x, y );
	int north = map( x, y - 1 );
	int west = map( x - 1, y );
	int east = map( x + 1, y );
	int south = map( x, y + 1 );


	// north
	if( north < current && north <= west && north <= east && north <= south )
		return determine_flow( map, x, y - 1 );
	
	// west
	if( west < current && west < north && west <= east && west <= south )
		return determine_flow( map, x - 1, y );

	// east
	if( east < current && east < west && east < north && east <= south )
		return determine_flow( map, x + 1, y );

	// south
	if( south < current && south < west && south < east && south < north )
		return determine_flow( map, x, y + 1 );
	
	// exit of recursive
	return x << 16 | y << 8;
}




static void each_map( FILE *in )
{
	char line[8192];
	int H, W;
	
	fgets( line, sizeof(line), in );
	sscanf( line, "%d %d", &H, &W );
	
#ifdef DEBUG
	printf( "H = %d, W = %d\n", H, W );
#endif

	matrix_2d map( W + 2, H + 2 );
	matrix_2d map2( W + 2, H + 2 );

	// surround the map( altitude = WALL(32767) )
	for( int y = 0; y < H + 2; y++ )
	{
		map(0, y) = WALL;
		map(W+2-1, y) = WALL;		
		map2(0, y) = WALL;
		map2(W+2-1, y) = WALL;		
	}
	
	for( int x = 0; x < W + 2; x++ )
	{
		map(x, 0) = WALL;
		map(x, H+2-1) = WALL;
		map2(x, 0) = WALL;
		map2(x, H+2-1) = WALL;		
	}
	
	// set the map
	for( int y = 1; y < H + 2 - 1; y++ )
	{
		fgets( line, sizeof(line), in );
		char *l = line;
		
		for( int x = 1; x < W + 2 - 1; x++ )
		{
			int altitude = 0;
			while( true )
			{
				char c = *l++;
				
				if( '0' <= c && c <= '9' )
				{
					altitude *= 10;
					altitude += c - '0';				
					map(x, y) = altitude;
				}
				
				// space
				if( c == ' ' || c == '\0' || c == 0x0a )
					break;				
			}
		}
	}

#ifdef DEBUG
	print_map(map);
#endif
	
	// find basins
	for( int x = 1; x < W + 2 - 1; x++ )
		for( int y = 1; y < H + 2 - 1; y++ )
		{
			int point = determine_flow( map, x, y );
			int p_y = (point >> 8) & 0xff;
			int p_x = point >> 16;

#ifdef DEBUG
			printf( "(%d,%d)->(%d,%d)\n", x, y, p_x, p_y );
#endif
			
			
			map2( x, y ) = point;
		}
	
	char label = 'a';
	for( int x = 1; x < W + 2 - 1; x++ )
	{
		for( int y = 1; y < H + 2 - 1; y++ )
		{
			int current = map2( x, y );
			if( 'z' < current )
			{
				map2( x, y ) = label;

				for( int X = 1; X < W + 2 - 1; X++ )
					for( int Y = 1; Y < H + 2 - 1; Y++ )
					{
						if( map2( X, Y ) == current )
							map2( X, Y ) = label;
					}
				label++;
			}
					
		}
	}
	
	print_result(map2);
	
}


int main()
{
	char line[8192];
	FILE *input = fopen("input.txt","rt");
	int T;
	
	if( input == NULL )
	{
		puts("File not found.");
		return EXIT_FAILURE;		
	}
	
	fgets( line, sizeof(line), input );
	sscanf( line, "%d", &T);
	
	printf("There are %d maps in the problem\n", T );
	
	for( int i = 0; i < T; i++ )
	{
		printf( "Case #%d:\n", i + 1 );
		each_map(input);
	}	
}