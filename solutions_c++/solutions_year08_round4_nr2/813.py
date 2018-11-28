// test.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <map>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>


int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream in;
	in.open( "B-small.in" );

	std::fstream out;
	out.open( "B-small.out", std::ios_base::out );

	size_t numCases = 0;
	in >> numCases;

	for( size_t curCase = 0; curCase < numCases; ++curCase )
	{
		size_t N;
		in >> N;
		
		size_t M;
		in >> M;
		
		size_t A;
		in >> A;

		bool find = false;
		size_t x1;
		size_t y1;
		size_t x2;
		size_t y2;
		size_t x3;
		size_t y3;

		for( __int64 a1 = 0; a1 <= N; ++a1 )
		{
			for( __int64 a2 = 0; a2 <= N; ++a2 )
			{
				for( __int64 b1 = 0; b1 <= M; ++b1 )
				{
					for( __int64 b2 = 0; b2 <= M; ++b2 )
					{
						__int64 v = a1 * b2 - a2 * b1;
						if( v < 0 )
							v = -v;
						if( v == A )
						{
							find = true;
							x1 = 0;
							y1 = 0;
							x2 = a1;
							y2 = b1;
							x3 = a2;
							y3 = b2;
							goto label1;
						}
					}
				}
			}
		}

label1:

		out << "Case #";
		out << curCase + 1;
		out << ": ";
		if( !find )
			out << "IMPOSSIBLE";
		else
		{
			out << x1 << " ";
			out << y1 << " ";
			out << x2 << " ";
			out << y2 << " ";
			out << x3 << " ";
			out << y3;
		}
		out << "\n";

		printf( "case: %i\n", curCase + 1 );
	}

	return 0;
}
