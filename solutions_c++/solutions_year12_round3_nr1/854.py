// GCJ.cpp : Defines the entry point for the console application.
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
#include <iostream>
#include <iomanip>


int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream in;
	in.open( "A-large.in" );

	std::fstream out;
	out.open( "A-large.out", std::ios_base::out );

	int numCases = 0;
	in >> numCases;

	std::cout << "Cases: " << numCases << std::endl;
	for( int caseIndex = 0; caseIndex < numCases; ++caseIndex )
	{
		int N = 0;
		in >> N;

		std::vector< std::vector< int > > inh( N );

		for( int i = 0; i < N; ++i )
		{
			int M = 0;
			in >> M;

			for( int j = 0; j < M; ++j )
			{
				int c = 0;
				in >> c;

				inh[ i ].push_back( c - 1 );
			}
		}

		bool hasDiamond = false;

		std::vector< int > C( N );
		for( int i = 0; i < N; ++i )
		{
			std::vector< int > S;
			S.insert( S.end( ), inh[ i ].begin( ), inh[ i ].end( ) );

			while( !S.empty( ) )
			{
				int h = S.back( );
				S.pop_back( );

				C[ h ] += 1;
				if( C[ h ] > 1 )
				{
					hasDiamond = true;
					break;
				}

				for( int j = 0; j < (int) inh[ h ].size( ); ++j )
					S.push_back( inh[ h ][ j ] );
			}

			if( hasDiamond )
				break;

			for( int j = 0; j < N; ++j )
				if( C[ j ] > 1 )
				{
					hasDiamond = true;
					break;
				}

			if( hasDiamond )
				break;

			for( int i = 0; i < N; ++i )
				C[ i ] = 0;
		}

		std::string caseResult = "No";
		if( hasDiamond )
			caseResult = "Yes";

		std::cout << "Case #" << caseIndex + 1 << ": ";
		std::cout << caseResult;
		std::cout << ", Done";
		std::cout << std::endl;

		out << "Case #" << caseIndex + 1 << ": ";
		out << caseResult;
		out << std::endl;
		out.flush( );
	}

	out.flush( );
	out.close( );

	return 0;
}

