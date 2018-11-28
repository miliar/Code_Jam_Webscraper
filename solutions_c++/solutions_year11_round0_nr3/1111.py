/*
 * Author ahfyth
*/

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;


const unsigned int maxN = 1000;

int main( int argc, char *argv[] )
{
	if( argc < 2 )
	{
		cerr << "Usage : " << argv[0] << " <file>\n";
		cerr << "This program is designed to \n";
		exit( 1 );
	}
	ifstream fin;
	fin.open( argv[1], ios::in );
	if( fin.fail() )
	{
		cerr << "Error : open file failed!\n";
		return 2;
	}
	unsigned int TOTAL;
	fin >> TOTAL;

	unsigned int i, j, k, min;
	unsigned int N;
	unsigned int * candy = new unsigned int[ maxN ];
	for( i=1; i<=TOTAL; ++i )
	{
		fin >> N;
		for( j=0; j<N; ++j )
			fin >> candy[ j ];

		k = candy[ 0 ];
		for( j=1; j<N; ++j )
			k ^= candy[ j ];

		if( k != 0 )
			cout << "Case #" << i << ": NO\n";
		else
		{
			k = candy[0];
			min = candy[0];
			for( j=1; j<N; ++j )
			{
				k += candy[ j ];
				if( candy[j] < min )min = candy[j];
			}

			k -= min;
			cout << "Case #" << i << ": " << k << endl;
		}
	}

	fin.close();

	return 0;
}



