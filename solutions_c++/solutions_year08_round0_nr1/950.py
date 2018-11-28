// test_C.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <math.h>
#include <vector>
#include <map>
#include <iostream>
#include <fstream>
#include <string>
#include <set>


void readString( std::ifstream& in, std::string& ss )
{
	while( true )
	{
		char c[ 2 ];
		c[ 0 ] = in.get( );
		c[ 1 ] = 0;

		if( isalpha( c[ 0 ] ) ||
			isdigit( c[ 0 ] ) ||
			c[ 0 ] == ' ' )
		{
			ss += std::string( c );
		}
		else
		{
			break;
		}
	}
}


int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream in;
	in.open( "A-large.in" );

	std::fstream out;
	out.open( "A-large.out", std::ios_base::out );

	size_t numCases = 0;
	in >> numCases;

	for( size_t c = 0; c < numCases; ++c )
	{
		size_t S;
		in >> S;

		std::vector< std::string > SS;
		while( SS.size( ) < S )
		{
			std::string ss;
			readString( in, ss );

			if( ss.length( ) )
				SS.push_back( ss );
		}

		size_t Q;
		in >> Q;

		std::vector< std::string > QQ;
		while( QQ.size( ) < Q )
		{
			std::string ss;
			readString( in, ss );

			if( ss.length( ) )
				QQ.push_back( ss );
		}

		std::vector< int > II;
		for( unsigned int i = 0; i < QQ.size( ); ++i )
		{
			int index = -1;
			for( unsigned int j = 0; j < SS.size( ); ++j )
				if( QQ[ i ] == SS[ j ] )
				{
					index = j;
					break;
				}

			II.push_back( index );
		}


		std::set< int > left;
		for( unsigned int i = 0; i < SS.size( ); ++i )
			left.insert( i );

		int N = 0;
		for( unsigned int i = 0; i < II.size( ); ++i )
		{
			if( II[ i ] == -1 )
				continue;

			left.erase( II[ i ] );
			if( left.empty( ) )
			{
				N += 1;

				for( unsigned int j = 0; j < SS.size( ); ++j )
					left.insert( j );
				left.erase( II[ i ] );
			}
		}

		out << "Case #";
		out << c + 1;
		out << ": ";
		out << N;
		out << "\n";
	}

	return 0;
}

