#include <stdio.h>
#include <windows.h>

#include <set>
#include <string>
#include <vector>

int main( int argc, char** argv ) {
	// input
	FILE* in = fopen( argv[ 1 ], "r" );

	long l = long();
	long d = long();
	long n = long();

	fscanf( in, "%ld %ld %ld", &l, &d, &n );

	// words
	std::vector< std::string > words;
	char buff[ 256 ];
	for( long i = 0; i < d; i++ ) {		
		fscanf( in, "%s", buff );
		words.push_back( buff );
	}

	// output
	FILE* out = fopen( "output.txt", "w" );

	for( long i = 0; i < n; i++ ) {
		std::vector< std::set< char > > pattern;
		fscanf( in, "%s", buff );
		char* c = buff;
		bool inP = false;
		
		while( *c != '\0' ) {
			if( !inP ) {
				pattern.resize( pattern.size() + 1 );
			}

			if( *c == '(' ) {
				inP = true;
			}
			else if( *c == ')' ) {
				inP = false;
			}
			else {
				pattern.back().insert( *c );
			}

			c = c + 1;
		}

		int cnt = 0;
		for( long int j = 0; j < d; j++ ) {
			bool isMatched = true;
			for( long k = 0; k < l && isMatched; k++ ) {
				isMatched = ( k < (long)pattern.size() && pattern[ k ].find( words[ j ].at( k ) ) != pattern[ k ].end() );
			}
			if( isMatched ) {
				cnt++;
			}
		}

		fprintf( out, "Case #%d: %d\n", i + 1, cnt );
	}

	fclose( in );
	fflush( out );
	fclose( out );

	return 0;
}
