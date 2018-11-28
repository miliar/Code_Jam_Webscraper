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


void solve( long N, long PD, long PG, unsigned int time )
{
	if( PG==0 && PD==0 )
	{
				cout << "Case #" << time << ": Possible\n";
				return;
	}
	if( (PG==0&&PD!=0) || (PG==100 && PD!=100))
	{
		cout << "Case #" << time << ": Broken\n";
		cerr << "Case #" << time << ":" << N << " "<< PD << " " <<PG <<" : Broken\n";
		return;
	}
	unsigned long ss, tt;
//	cout << N << PD << PG << '\n';
//	if( N > PG ) N %= PG ;
//	if( N == 0 ) N = PG;
//	if( N == 0 )
//	{
//		cout << "Case #" << time << ": Possible\n";
//		return;
//	}
	for( unsigned long i=1; i<=N; ++i )
	{
		if( (i * PD) % 100 != 0 )continue;

		unsigned int j;
		j = i*(PD-PG)/PG;
		if(j<0) j=0;
		for( unsigned int k=0; k<100; ++k )
		{
			if( ( (i+j+k)*PG) %100 == 0 )
			{
				cout << "Case #" << time << ": Possible\n";
				cerr << "Case #" << time << ":" << N << " "<< PD << " " <<PG <<" : Possible "<< i << "," << j << "\n";
				return;
			}
		}
//		cerr << "\ntt=" << tt << '\n';
	}
	cout << "Case #" << time << ": Broken\n";
	cerr << "Case #" << time << ":" << N << " "<< PD << " " <<PG <<" : Broken\n";
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
	long N, PD, PG;
	for( i=1; i<=TOTAL; ++i )
	{
		fin >> N >> PD >> PG;
		if( N == 0 )
		{
			cerr << "what's happening ? \n";
		}
		//  cout << "Case #" << i << ": Broken" << endl;
		solve( N, PD, PG, i );
	}

	fin.close();

	return 0;
}



