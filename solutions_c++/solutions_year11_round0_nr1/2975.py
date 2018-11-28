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


int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream in;
	in.open( "A-large.in" );

	std::fstream out;
	out.open( "A-large.out", std::ios_base::out );

	int numCases = 0;
	in >> numCases;

	for( int caseIndex = 0; caseIndex < numCases; ++caseIndex )
	{
		unsigned int N = 0;
		in >> N;

		std::vector< char > colors( N );
		std::vector< unsigned int > buttons( N );
		for( unsigned int i = 0; i < N; ++i )
		{
			in >> colors[ i ];
			in >> buttons[ i ];
		}

		unsigned int p1 = 1;
		unsigned int p2 = 1;

		unsigned int R = 0;
		for( int i = 0; i < (int) N; ++i )
		{
			if( colors[ i ] == 'O' )
			{
				unsigned int s = 0;
				if( buttons[ i ] > p1 )
					s = buttons[ i ] - p1 + 1;
				else
					s = p1 - buttons[ i ] + 1;
				R += s;
				p1 = buttons[ i ];

				int I = -1;
				for( int j = i + 1; j < (int) N; ++j )
					if( colors[ j ] == 'B' )
					{
						I = j;
						break;
					}

				if( I != -1 )
				{
					int s2 = (int) buttons[ I ] - (int) p2;
					if( abs( s2 ) < (int) s )
						p2 += s2;
					else
					{
						if( s2 < 0 )
							p2 -= s;
						else
							p2 += s;
					}
				}
			}
			else if( colors[ i ] == 'B' )
			{
				unsigned int s = 0;
				if( buttons[ i ] > p2 )
					s = buttons[ i ] - p2 + 1;
				else
					s = p2 - buttons[ i ] + 1;
				R += s;
				p2 = buttons[ i ];

				int I = -1;
				for( int j = i + 1; j < (int) N; ++j )
					if( colors[ j ] == 'O' )
					{
						I = j;
						break;
					}

				if( I != -1 )
				{
					int s2 = (int) buttons[ I ] - (int) p1;
					if( abs( s2 ) < (int) s )
						p1 += s2;
					else
					{
						if( s2 < 0 )
							p1 -= s;
						else
							p1 += s;
					}
				}
			}
		}

		std::cout << "Case #" << caseIndex + 1 << ": Done" << std::endl;

		out << "Case #" << caseIndex + 1 << ": ";
		out << R;
		out << "\n";
		out.flush( );
	}

	out.flush( );
	out.close( );

	return 0;
}