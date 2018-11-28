#include "stdafx.h"

#include <string>
#include <fstream>
#include <list>
#include <vector>
#include <set>


void solve( int k, int n, int* qs, int* ans ) {
	int* order = new int[ k ];

	std::vector< int > indexies;
	indexies.resize( k );
	for( int i = 0; i < k; i++ ) {
		indexies[ i ] = i + 1;
	}

	std::set< int > orderSet;
	for( int i = 0; i < n; i++ ) {
		orderSet.insert( qs[ i ] );
	}

	int start = 0;
	for( int i = 1; i <= k && orderSet.size() > 0; i++ ) {
		int num = ( start + ( i - 1 ) ) % (int)indexies.size();
		start = num;
		int idx = indexies[ num ] ;
		indexies.erase( indexies.begin() + num );
		order[ idx - 1 ] = i;
		orderSet.erase( idx );		
	}

	for( int i = 0; i < n; i++ ) {
		ans[ i ] = order[ qs[ i ] - 1 ];
	}
}

void solve( char* path ) {
	// buffer
	char buff[ 0x10000 ];

	// file path
	std::string inPath = path;
	std::string outPath = inPath + ".out";

	// open the file
	std::ifstream ifs( inPath.c_str() );
	std::ofstream ofs( outPath.c_str() );

	int c = 1;
	int k = int();
	int step = 0;

	while( !ifs.eof() ) {
		// read line
		ifs.getline( buff, 0x10000 );

		// save the universe	
		if( step == 0 ) {	// get the number of tests
			step = 1;
		}
		else if( step == 1 ) {	// get the number of cards
			k = atoi( buff );
			step = 2;
		}
		else if( step == 2 ) {	// solve
			char* tok = strtok( buff, " \t," );
			int n = atoi( tok );
			int* qs = new int[ n ];
			for( int i = 0; i < n; i++ ) {
				tok = strtok( NULL, " \t," );
				qs[ i ] = atoi( tok );
			}

			int* ans = new int[ n ];

			printf( "Case %d\n", c );
			solve( k, n, qs, ans );
			ofs << "Case #" << c << ":";
			for( int i = 0; i < n; i++ ) {
				ofs << " " << ans[ i ];
			}
			ofs << std::endl;
			c++;

			delete[] qs;
			delete[] ans;
			step = 1;
		}
	}

	ifs.close();
	ofs.flush();
	ofs.close();
}

int main(int argc, char** argv ) {
	solve( argv[ 1 ] );
	return 0;
}
