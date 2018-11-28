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

double minRoast( unsigned int l )
{
	if( l == 1 )return 0;
	if( l == 2 )return 2;
	if( l == 3 )return 3;
	if( l == 4 )return 61/15;
	
	cerr << "Error : " << l << "\n";
	return 0;
}

double solve( unsigned int *p, unsigned int n )
{
	unsigned int i, j, k, l;
/*
	cerr << "Input p :";
	for( j=1; j<=n; ++j )
		cerr << p[j] << " ";
	cerr << "\n";
*/
	unsigned int *q = new unsigned int[ n+1 ];

	double time = 0;
	unsigned int m = n;
	while( m > 0 )
	{
		// calc q
		for( j=1; j<=n; ++j )
		{
			k = 0;
			l = p[ j ];
			while( 1 )
			{
				if( l == j )break;
				l = p[l];
				++ k;
			}
			q[ j ] = k;
		}

		l = 100000;
		for( j=1; j<=n; ++j )
		{
			if( q[j] != 0 && q[j] < l )
			  l = q[j];
		}
		if( l==100000 )break;
		for( j=1; j<=n; ++j )
			if( q[j] == l )break;
//		cerr << "Smallest Circle : " << l << " : from " << j << "\n";

		//time += l * 2;
		//time += minRoast( l+1 );
		time += l+1;

		m -= l + 1;

		l = p[ j ];
		while( 1 )
		{
			if( l == j )break;
			k = p[l];
			p[l] = l;
			l = k;
		}
		p[j] = j;
/*
		cerr << "Now p :";
		for( j=1; j<=n; ++j )
			cerr << p[j] << " ";
		cerr << "\n\n";
*/
	}
	delete [] q;
	return time;
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

	unsigned int i, j;
	unsigned int N;
	unsigned int *p = new unsigned int[ maxN+1 ];
	double time;
	for( i=1; i<=TOTAL; ++i )
	{
		fin >> N;
		for( j=1; j<=N; ++j )
		{
			fin >> p[j];
		}
		time = solve( p, N );

		printf( "Case #%d: %6f\n", i, time );
	//	cerr << "Case #" << i << ": " << time << endl;
	}

	fin.close();

	return 0;
}



