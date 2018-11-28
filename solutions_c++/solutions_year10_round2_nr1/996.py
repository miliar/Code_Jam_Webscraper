// test_A.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <stack>
#include <iostream>
#include <fstream>


struct Gr
{
	Gr( unsigned int _n ) :
		n( _n ),
		c( 0 )
	{
	}

	Gr( unsigned int _n, unsigned int _c ) :
		n( _n ),
		c( _c )
	{
	}

	unsigned int n;
	unsigned int c;
};


int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream in;
	in.open( "A-large.in" );

	std::fstream out;
	out.open( "A-large.out", std::ios_base::out );

	int T = 0;
	in >> T;

	for( int caseIndex = 0; caseIndex < T; ++caseIndex )
	{
		unsigned int N = 0;
		in >> N;

		unsigned int M = 0;
		in >> M;

		std::string fakeString;
		std::getline( in, fakeString );

		std::set< std::string > dirsE;
		for( unsigned int i = 0; i < N; ++i )
		{
			std::string dir;
			std::getline( in, dir );
			dirsE.insert( dir );
		}

		std::vector< std::string > dirsN;
		for( unsigned int i = 0; i < M; ++i )
		{
			std::string dir;
			std::getline( in, dir );
			dirsN.push_back( dir );
		}

		unsigned int R = 0;
		for( unsigned int i = 0; i < M; ++i )
		{
			bool needCount = false;

			std::string dir;
			char * pc = strtok( (char *) dirsN[ i ].c_str( ) + 1, "/" );
			while( pc )
			{
				dir = dir + std::string( "/" ) + std::string( pc );
				pc = strtok( 0, "/" );

				if( !needCount )
				{
					if( dirsE.find( dir ) == dirsE.end( ) )
					{
						needCount = true;
						R += 1;
						dirsE.insert( dir );
					}
				}
				else
				{
					R += 1;
					dirsE.insert( dir );
				}
			}
		}

		out << "Case #" << caseIndex + 1 << ": ";
		out << R;
		out << "\n";
		out.flush( );
	}

	out.flush( );
	out.close( );

	return 0;
}