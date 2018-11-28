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

const unsigned int MAXN = 100;

void solve( unsigned int N, char ** compete, unsigned int time )
{
	double WP[ MAXN ];
	double OWP[ MAXN ];
	double OOWP[ MAXN ];
	unsigned int i, j;
	unsigned int count;

	unsigned int played[ MAXN ];
	// WP
	for( i=0; i<N; ++i )
	{
		WP[i] = 0;
		played[i] = 0;
		for( j=0; j<N; ++j )
		{
			if( compete[i][j] == '.' )continue;
			played[i] ++;
			if( compete[i][j] == '1' )WP[i] ++;
		}
		WP[ i ] /= played[i];
	}

	//OWP
	for( i=0; i<N; ++i )
	{
		OWP[i] = 0;

		for( j=0; j<N; ++j )
		{
			if( compete[i][j] != '.' )
			{
				if( compete[i][j] == '1' )
				{
					OWP[i] += WP[j] * played[j] / ( played[j] -1 );
				}
				else
				{
					OWP[i] += (WP[j] * played[j] - 1 ) / ( played[j] -1 );
				}
			}
		}
		OWP[i] /= played[i];
	}
	//OOWP
	for( i=0; i<N; ++i )
	{
		OOWP[i] = 0;
		for( j=0; j<N; ++j )
		{
			if( compete[i][j] != '.' )
			{
				OOWP[i] += OWP[j];
			}
		}
		OOWP[i] /= played[i];
	}

	// score
	double s;
	cout << "Case #" << time << ":\n";
	for( i=0; i<N; ++i )
	{
		s = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];
		printf( "%.7f\n", s );
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

	char **compete = new char * [MAXN];

	unsigned int N;
	unsigned int i, j, k;
	for( i=0; i<MAXN; ++i )
		compete[i] = new char[ MAXN ];

	for( i=1; i<=TOTAL; ++i )
	{
		fin >> N;
		for( j=0; j<N; ++j )
			for( k=0; k<N; ++k )
				fin >> compete[j][k];

		solve( N, compete, i );

//		cout << "Case #" << i << ": " << << endl;
	}

	fin.close();

	return 0;
}



