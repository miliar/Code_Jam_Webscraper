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

	unsigned int i, j, k;
	unsigned int N, L, H;
	unsigned int freq[100];
	for( i=1; i<=TOTAL; ++i )
	{
		fin >> N >> L >> H;
		for( j=0; j<N; ++j )
			fin >> freq[j];

		for( j=L; j<=H; ++j )
		{
			for( k=0; k<N; ++k )
			{
				if( j >= freq[k] )
				{
					if( j % freq[k] != 0 )break;
				}
				else
				{
					if( freq[k] % j != 0 )break;
				}
			}
			if( k == N )
			{
				cout << "Case #" << i << ": " << j << endl;
				break;
			}
		}
		if( j > H )
		{
			cout << "Case #" << i << ": NO\n";
		}

//		cout << "Case #" << i << ": " << << endl;
	}

	fin.close();

	return 0;
}



