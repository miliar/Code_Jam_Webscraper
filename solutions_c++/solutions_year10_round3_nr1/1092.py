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

		std::vector< unsigned int > A( N );
		std::vector< unsigned int > B( N );
		for( unsigned int i = 0; i < N; ++i )
		{
			in >> A[ i ];
			in >> B[ i ];
		}

		unsigned int R = 0;
		for( unsigned int i = 0; i < N; ++i )
		{
			unsigned int a1 = A[ i ];
			unsigned int b1 = B[ i ];
			for( unsigned int j = i + 1; j < N; ++j )
			{
				unsigned int a2 = A[ j ];
				unsigned int b2 = B[ j ];
				if( ((a1 < a2) && (b2 < b1)) ||
					((a2 < a1) && (b1 < b2)) )
				{
					R += 1;
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