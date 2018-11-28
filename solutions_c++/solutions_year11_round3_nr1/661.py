#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;
typedef long long ll;

char ma[ 100 ][ 100 ];
int r, c;

int main(){
	int casos;
	scanf( "%d", &casos );
	for( int k = 1; k <= casos; ++k ){
		memset( ma, '\0', sizeof( ma ) );
		scanf( "%d %d", &r, &c );
		for( int i = 0; i < r; ++i ){
			for( int j = 0; j < c; ++j )
				cin >> ma[ i ][ j ];
		}

			
		for( int i = 0; i < r; ++i ){
			for( int j = 0; j < c; ++j ){
				if( ma[ i ][ j ] == '#' && ma[ i ][ j + 1 ] == '#' && ma[ i + 1 ][ j ] == '#' && ma[ i + 1 ][ j + 1 ] == '#' ){
					 ma[ i ][ j ] = '/';
					 ma[ i ][ j + 1 ] = '\\';
					 
					 ma[ i + 1 ][ j ] = '\\';
					 ma[ i + 1 ][ j + 1 ] = '/';
				}
			}
		}
		
		bool dm = false;
		for( int i = 0; i < r; ++i ){
			for( int j = 0; j < c; ++j ){
				if( ma[ i ][ j ] == '#' )
					dm = true;
			}
		}
		printf( "Case #%d:\n", k );
		if( dm )
			printf( "Impossible\n" );
		else{
			for( int i = 0; i < r; ++i ){
				for( int j = 0; j < c; ++j )
					printf( "%c", ma[i][j] );
				printf( "\n" );				
			}
		}

	}
	

}

