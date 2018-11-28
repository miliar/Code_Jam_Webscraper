// MinimumScalrProduct.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include "stdafx.h"

#include <fstream>
#include <string>
#include <vector>
#include <algorithm>


int getMinimum( int* v1, int* v2, int n ) {
	std::vector< int > vv1;
	std::vector< int > vv2;

	for( int i = 0; i < n; i++ ) {
		vv1.push_back( v1[ i ] );
		vv2.push_back( v2[ i ] );
	}

	std::sort( vv1.begin(), vv1.end() );
	std::sort( vv2.begin(), vv2.end() );

	int p = 0; 
	for( int i = 0; i < n; i++ ) {
		p += vv1[ i ] * vv2[ n - 1 - i ];
	}

	return p;
}

int main(int argc, char** argv ) {
	// buffer
	char buff[ 4096 ];

	// file path
	std::string inPath = argv[ 1 ];
	std::string outPath = inPath + ".out";

	// open the file
	std::ifstream ifs( inPath.c_str() );
	std::ofstream ofs( outPath.c_str() );

	int step = 0;
	int c = 1;
	int n = int();
	int* v1 = NULL;
	int* v2 = NULL;

	while( !ifs.eof() ) {
		// read line
		ifs.getline( buff, 4096 );

		// solve
		if( step == 0 ) {	// get the number of tests
			step = 1;
		}
		else if( step == 1 ) {	// n
			n = atoi( buff );
			v1 = NULL;
			v2 = NULL;
			step = 2;
		}
		else if( step == 2 ) {
			int* v = NULL;
			if( v1 == NULL ) {
				v1 = new int[ n ];
				v = v1;
			}
			else if( v2 == NULL ) {
				v2 = new int[ n ];
				v = v2;
			}

			char* tok = strtok( buff, " ,\t" );
			for( int i = 0; i < n; i++ ) {
				v[ i ] = atoi( tok );
				tok = strtok( NULL, " ,\t" );
			}

			if( v1 != NULL && v2 != NULL ) {
				int a = getMinimum( v1, v2, n );

				ofs << "Case #" << c << ": " << a << std::endl;

				delete[] v1;
				delete[] v2;
				v1 = NULL;
				v2 = NULL;
				step = 1;
				c++;
			}
		}
	}

	ifs.close();
	ofs.flush();
	ofs.close();

	return 0;
}

