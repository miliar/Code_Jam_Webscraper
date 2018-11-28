// round1A_a.cpp : Defines the entry point for the console application.
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
	in.open( "A-small.in" );

	std::fstream out;
	out.open( "A-small.out", std::ios_base::out );

/*	std::ifstream in;
	in.open( "A-large.in" );

	std::fstream out;
	out.open( "A-large.out", std::ios_base::out );
*/


	size_t numCases = 0;
	in >> numCases;

	for( size_t curTest = 0; curTest < numCases; ++curTest )
	{
		__int64 n;
		in >> n;

		__int64 A;
		in >> A;
			
		__int64 B;
		in >> B;
		
		__int64 C;
		in >> C;
		
		__int64 D;
		in >> D;
		
		__int64 x0;
		in >> x0;
		
		__int64 y0;
		in >> y0;
		
		__int64 M;
		in >> M;

		std::vector< __int64 > tX;
		std::vector< __int64 > tY;

		__int64 X = x0;
		__int64 Y = y0;
		tX.push_back( X );
		tY.push_back( Y );
		for( __int64 i = 1; i < n; ++i )
		{
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
			tX.push_back( X );
			tY.push_back( Y );
		}

		__int64 minX = tX[ 0 ];
		__int64 maxX = tX[ 0 ];
		__int64 minY = tY[ 0 ];
		__int64 maxY = tY[ 0 ];
		for( size_t i = 0; i < tX.size( ); ++i )
		{
			__int64 x = tX[ i ];
			__int64 y = tX[ i ];
			if( x < minX )
				minX = x;
			if( x > maxX )
				maxX = x;
			if( y < minY )
				minY = y;
			if( y > maxY )
				maxY = y;
		}

		__int64 numT = 0;
		__int64 munTt = 0;

		size_t nn = tX.size( );
		for( size_t i1 = 0; i1 < nn; ++i1 )
		{
			for( size_t i2 = i1 + 1; i2 < nn; ++i2 )
			{
				for( size_t i3 = i2 + 1; i3 < nn; ++i3 )
				{
					if( (tX[ i1 ] + tX[ i2 ] + tX[ i3 ]) % 3 == 0 &&
						(tY[ i1 ] + tY[ i2 ] + tY[ i3 ]) % 3 == 0 )
					{
						numT += 1;
					}

					munTt += 1;
				}
			}
		}

		out << "Case #";
		out << curTest + 1;
		out << ": " << numT;
		out << "\n";

		printf( "case: %i\n", curTest + 1 );
	}

	return 0;
}