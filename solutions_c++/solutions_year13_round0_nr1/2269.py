#include <cstdio>
#include <cstring>

FILE *fin = fopen( "Ain.txt", "r" );
FILE *fout = fopen( "Aout.txt", "w" ); 

using namespace std;

int T;

char grid[5][5];

inline bool empty(){
	for ( int i = 0; i < 4; ++i ){
		for ( int j = 0; j < 4; ++j ){
			if ( grid[i][j] == '.' ) return true;
		}
	}
	return false;
}

inline int victory(){ // 0 - fail; 1 - X; 2 - O

	for ( int i = 0; i < 4; ++i ){
		
		int x = 0, o = 0;
		bool t = false;
		
		for ( int j = 0; j < 4; ++j ){
			if ( grid[i][j] == 'X' ) ++x;
			if ( grid[i][j] == 'O' ) ++o;
			if ( grid[i][j] == 'T' ) t = true;
 		}
		
		if ( x == 4 || ( x == 3 && t ) ) return 1;
		if ( o == 4 || ( o == 3 && t ) ) return 2;
		
	}
	
	for ( int i = 0; i < 4; ++i ){
		
		int x = 0, o = 0;
		bool t = false;
		
		for ( int j = 0; j < 4; ++j ){
			if ( grid[j][i] == 'X' ) ++x;
			if ( grid[j][i] == 'O' ) ++o;
			if ( grid[j][i] == 'T' ) t = true;
 		}
		
		if ( x == 4 || ( x == 3 && t ) ) return 1;
		if ( o == 4 || ( o == 3 && t ) ) return 2;
		
	}
	
	int x = 0, o = 0;
	bool t = false;

	
	for ( int i = 0; i < 4; ++i ){
		
		if ( grid[i][i] == 'X' ) ++x;
		if ( grid[i][i] == 'O' ) ++o;
		if ( grid[i][i] == 'T' ) t = true;

		if ( x == 4 || ( x == 3 && t ) ) return 1;
		if ( o == 4 || ( o == 3 && t ) ) return 2;
		
	}
	
	x = 0, o = 0;
	t = false;

	
	for ( int i = 0; i < 4; ++i ){
		
		if ( grid[i][4 - i - 1] == 'X' ) ++x;
		if ( grid[i][4 - i - 1] == 'O' ) ++o;
		if ( grid[i][4 - i - 1] == 'T' ) t = true;

		if ( x == 4 || ( x == 3 && t ) ) return 1;
		if ( o == 4 || ( o == 3 && t ) ) return 2;
		
	}
	
	return 0;
	
} 

int main( void ){

	fscanf( fin, "%d", &T );
	
	for ( int i = 0; i < T; ++i ){

		printf( "Yay\n" );
	
		for ( int j = 0; j < 4; ++j ) fscanf( fin, "%s", grid[j] );
		int tmp = victory();
	
		if ( tmp == 1 ){ fprintf( fout, "Case #%d: X won\n", i + 1 ); continue; }
		if ( tmp == 2 ){ fprintf( fout, "Case #%d: O won\n", i + 1 ); continue; }
		if ( empty() ) fprintf( fout, "Case #%d: Game has not completed\n", i + 1 ); else fprintf( fout, "Case #%d: Draw\n", i + 1 );
	
	}
	
	return 0;

}
