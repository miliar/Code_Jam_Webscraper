// round1A_c.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <map>
#include <iostream>
#include <fstream>
#include <algorithm>


int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream in;
	in.open( "C-small.in" );

	std::fstream out;
	out.open( "C-small.out", std::ios_base::out );

/*	std::ifstream in;
	in.open( "C-large.in" );

	std::fstream out;
	out.open( "C-large.out", std::ios_base::out );
*/


	size_t numCases = 0;
	in >> numCases;

	for( size_t curTest = 0; curTest < numCases; ++curTest )
	{
		size_t K;
		in >> K;

		size_t n;
		in >> n;

		std::vector< size_t > D;
		for( size_t i = 0; i < n; ++i )
		{
			size_t d;
			in >> d;

			D.push_back( d );
		}

		std::vector< size_t > E;
		for( size_t i = 0; i < K; ++i )
			E.push_back( i );


		std::vector< size_t > PP;
		PP.resize( K );

		size_t KK = 0;
		for( size_t i = 1; i <= K; ++i )
		{
			size_t ii = (KK + i - 1) % E.size( );
			PP[ E[ ii ] ] = i;
			E.erase( E.begin( ) + ii );
			KK = ii;
		}

		out << "Case #";
		out << curTest + 1;
		out << ": ";
		for( size_t i = 0; i < D.size( ) - 1; ++i )
			out << PP[ D[ i ] - 1 ] << " ";
		out << PP[ D[ D.size( ) - 1 ] - 1 ];
		out << "\n";

		printf( "case: %i\n", curTest + 1 );
	}

	return 0;
}

