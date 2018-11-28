#include <stdio.h>
#include <stdlib.h>

#include <vector>


// T : ( 1, 100 )
// C : ( 0, 1 ) / ( 0, 36 )
// D : ( 0, 1 ) / ( 0, 28 )
// N : ( 1, 10 ) / ( 1, 100 )


using namespace std;


vector< char > checkCombine( vector< char* > C, vector< char > input );
vector< char > checkOppose( vector< char* > D, vector< char > input );


void main(){


	// file open
	FILE *fp = fopen( "input.txt", "r" );
	FILE *fp2 = fopen( "output.txt", "w" );

	if( fp == NULL ){

		return;
	}

	//
	int T;

	vector< char* > C;
	vector< char* > D;
	vector< char > input;
	vector< char > output;


	int i, j, n;
	char s[ 150 ] = { 0 };
	char c = 0;

	char* t;

	// T
	fscanf( fp, "%d", &T );

	for( i= 0; i< T; i++ ){
		C.clear();
		D.clear();
		input.clear();
		output.clear();
		
		// C
		fscanf( fp, "%d", &n );
		for( j= 0; j< n; j++ ){

			fscanf( fp, "%s", s );

			t = ( char* )malloc( sizeof( s ) );
			
			memcpy( t, s, sizeof( s ) );

			C.push_back( t );
		}

		// D
		fscanf( fp, "%d", &n );
		for( j= 0; j< n; j++ ){

			fscanf( fp, "%s", s );

			t = ( char* )malloc( sizeof( s ) );
			memcpy( t, s, sizeof( s ) );
			D.push_back( t );
		}

		// input
		fscanf( fp, "%d", &n );

		if( n > 0 ){
			fscanf( fp, "%s", s );

			for( j= 0; j< n; j++ ){

				input.push_back( s[ j ] );
			}
		}


		for( j= 0; j< input.size(); j++ ){

			output.push_back( input[ j ] );
			output = checkCombine( C, output );
			output = checkOppose( D, output );
		}

		fprintf( fp2, "Case #%d: [", i+1 );
		for( j = 0; j< output.size(); j++ ){

			fprintf( fp2, "%c, ", output[ j ] );
		}
		fprintf( fp2, "]\n" );
	}
}



vector< char > checkCombine( vector< char* > C, vector< char > input ){

	if( input.size() < 2 ){

		return input;
	}

	int i;

	char ele1 = input[ input.size() -1 ];
	char ele2 = input[ input.size() -2 ];

	for( i= 0; i< C.size(); i++ ) {

		if( ( ele1 == C[ i ][ 0 ] && ele2 == C[ i ][ 1 ] ) ||
			( ele1 == C[ i ][ 1 ] && ele2 == C[ i ][ 0 ] ) ){

				input.pop_back();
				input.pop_back();
				input.push_back( C[ i ][ 2 ] );
		}
	}
	return input;
}

vector< char > checkOppose( vector< char* > D, vector< char > input ){

	if( input.size() < 2 ){

		return input;
	}

	int i, j;

	for( i= 0; i< D.size(); i++ ) {
		
		//
		if( input[ input.size() -1 ] == D[ i ][ 0 ] ){

			for( j= 0; j< input.size() -1; j++ ){

				if( input[ j ] == D[ i ][ 1 ] ){

					input.clear();
					return input;
				}
			}
		}
		else if( input[ input.size() -1 ] == D[ i ][ 1 ] ){

			for( j= 0; j< input.size() -1; j++ ){

				if( input[ j ] == D[ i ][ 0 ] ){

					input.clear();
					return input;
				}
			}
		}
	}
	return input;
}