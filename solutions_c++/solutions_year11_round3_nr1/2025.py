#include<cstdio>
#define MAX_R 50
#define MAX_C 50
using namespace std;
char grid[ MAX_R ][ MAX_C ];
int R, C;
bool fill_tile( int r, int c ){
	if( r+1< R && c+1 < C ){
		if( grid[ r ][ c ] == '#' && grid[ r ][ c+1 ] == '#'&&
		    	grid[ r+1 ][ c ] == '#' && grid[ r+1 ][ c+1 ] == '#'){
		   	
		 	grid[ r ][ c ] = '/';
		    	grid[ r ][ c+1 ] = '\\';
		    	grid[ r+1 ][ c ] = '\\';
			grid[ r+1 ][ c+1 ] = '/';
		    	return true;
		    }else{
		    	return false;
		    }
	}
	return false;
}
int main(){
	int T, _case = 0;
	scanf( "%d", &T );
	while( T -- ){
		bool possible = true;
		scanf( "%d %d", &R, &C );
		for( int i = 0; i < R; i ++ ){
			scanf( "%s", grid[ i ] );
		}
		
		for( int i = 0; i < R && possible ; i ++ ){
			for( int j = 0; j < C && possible ; j ++ ){
				if( grid[ i ][ j ] == '#' ){
					possible = fill_tile( i , j );
				}
			}
		}
		printf( "Case #%d:\n", ++_case );
		if( possible ){
			for( int i = 0; i < R; i ++ ){
				for( int j = 0; j < C; j ++ ){
					printf("%c",grid[ i ][ j ] );
				}
				printf( "\n" );
			}
		
		}else{
			printf("Impossible\n");
		}
	}
	return 0;
}
