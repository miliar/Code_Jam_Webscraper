#include <windows.h>
#include <stdio.h>
#include <fstream>


long countWelcome( const char* s, long idx, char* line ) {
	if( s[ idx ] == '\0' ) {
		return 1;
	}

	long cnt = 0;
	char* tmp = line;
	while( *tmp != '\0' ) {
		if( s[ idx ] == *tmp ) {
			cnt = cnt + countWelcome( s, idx + 1, tmp + 1 );
		}
		tmp++;
	}

	return cnt;
}


int main( int argc, char** argv ) {
	// string 
	const char* s = "welcome to code jam";

	// open
	FILE* in = fopen( argv[ 1 ], "r" );
	FILE* out = fopen( "output.txt", "w" );

	char line[ 1024 ];
	fgets( line, 1024, in );
	long n = atol( line );

	// count
	for( long i = 0; i < n; i++ ) {
		fgets( line, 1024, in );
		printf( "%d: %s\n", i + 1, line );

		long cnt = countWelcome( s, 0, line );

		fprintf( out, "Case #%d: %04d\n", i + 1, cnt );
	}

	// close
	fclose( in );
	fflush( out );
	fclose( out );
}
