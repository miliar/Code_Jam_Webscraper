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

const unsigned int MAXR = 50;
const unsigned int MAXC = 50;

void solve( char **map, unsigned int R, unsigned int C, unsigned int time )
{
	unsigned int i, j;
	for( i=0; i<R-1; ++i )
	{
		for( j=0; j<C-1; ++j )
		{
			if( map[i][j] == '#' )
			{
				if( map[i][j+1] == '#' && map[i+1][j] =='#' && map[i+1][j+1] == '#')
				{
					map[i][j] = '/';
					map[i][j+1] = '\\';
					map[i+1][j] = '\\';
					map[i+1][j+1] = '/';
				}
				else
				{
					cout << "Case #" << time << ":\nImpossible\n";
					return;
				}
			}
		}
	}
	for( i=0; i<R; ++i )
		for( j=0; j<C; ++j )
			if( map[i][j] == '#' )
			{
				cout << "Case #" << time << ":\nImpossible\n";
				return;
			}

	cout << "Case #" << time << ":\n";
	for( i=0; i<R; ++i )
	{
		for( j=0; j<C; ++j )
		  cout << map[i][j];

		cout << endl;
	}
}

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
	unsigned int R, C;
	char **map = new char *[ MAXR ];
	for( i=0; i<MAXR; ++i )
		map[i] = new char[ MAXC ];

	for( i=1; i<=TOTAL; ++i )
	{
		fin >> R >> C;
		for( j=0; j<R; ++j )
			for( k=0; k<C; ++k )
				fin >> map[j][k];

		solve( map, R, C, i );
//		cout << "Case #" << i << ": " << << endl;
	}

	fin.close();

	return 0;
}



