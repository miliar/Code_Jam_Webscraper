// BribeThePrisoners.cpp : Defines the entry point for the console application.
//


#include <stdio.h>
#include <vector>


int count( int* arr, int num, int size ) {
	if( num == 0 ) {
		return 0;
	}
	if( num == 1 ) {
		return ( size - 1 );
	}


	int minGold = INT_MAX;
	for( int i = 0; i < num; i++ ) {
		int idx = arr[ i ];
		int tmpGold = count( arr, i, idx - 1 );
		std::vector< int > vec;
		for( int j = i + 1; j < num; j++ ) {
			vec.push_back( arr[ j ] - idx );			
		}
		tmpGold += count( vec.size() == 0 ? NULL : &( vec[ 0 ] ), (int)vec.size(), size - idx );

		if( tmpGold < minGold ) {
			minGold = tmpGold;
		}
	}

	minGold += ( size - 1 );

	return minGold;
}



int main( int argc, char** argv ) {
	// input
	char* path = argv[ 1 ];
	FILE* in = fopen( path, "r" );
	FILE* out = fopen( "output.txt", "w" );

	long num = int();
	fscanf( in, "%ld", &num );

	for( long i = 0; i < num; i++ ) {
		long p = long();
		long q = long();
		fscanf( in, "%ld %ld", &p, &q );

		std::vector< int > vec;
		for( int j = 0; j < q; j++ ) {
			long a = long();
			fscanf( in, "%ld", &a );
			vec.push_back( a );
		}

		int cnt = count( &( vec[ 0 ] ), (int)vec.size(), p );

		fprintf( out, "Case #%d: %d\n", i + 1, cnt );
	}

	fclose( in );
	fflush( out );
	fclose( out );

	return 0;
}
