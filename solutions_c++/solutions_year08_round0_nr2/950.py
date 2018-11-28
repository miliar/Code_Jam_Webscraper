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
#include <algorithm>


bool testWhiteSpaces( char c )
{
	if( c == ' ' || c == '\t' || c == '\n' || c == '\r' )
		return true;
	return false;
}


int readTime( std::ifstream& in )
{
	char c;
	c = in.get( );

	while( testWhiteSpaces( c ) )
		c = in.get( );

	char c1 = c;
	char c2 = in.get( );
	char dd = in.get( ); //:
	char c3 = in.get( );
	char c4 = in.get( );

	return (c1 * 10 + c2) * 60 + (c3 * 10 + c4);
}


struct L
{
	int t1;
	int t2;

	L( )
	{
		t1 = 0;
		t2 = 0;
	}

	L( int _t1, int _t2 )
	{
		t1 = _t1;
		t2 = _t2;
	}

	bool operator< ( const L& l )
	{
		if( t1 < l.t1 )
			return true;
		return false;
	}
};


int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream in;
	in.open( "B-large.in" );

	std::fstream out;
	out.open( "B-large.out", std::ios_base::out );

	size_t numCases = 0;
	in >> numCases;

	for( size_t c = 0; c < numCases; ++c )
	{
		int T;
		in >> T;

		size_t NA;
		in >> NA;

		size_t NB;
		in >> NB;

		std::vector< L > fromA;
		for( size_t i = 0; i < NA; ++i )
		{
			int t1 = readTime( in );
			int t2 = readTime( in ) + T;
			fromA.push_back( L( t1, t2 ) );
		}
		std::sort( fromA.begin( ), fromA.end( ) );

		std::vector< L > fromB;
		for( size_t i = 0; i < NB; ++i )
		{
			int t1 = readTime( in );
			int t2 = readTime( in ) + T;
			fromB.push_back( L( t1, t2 ) );
		}
		std::sort( fromB.begin( ), fromB.end( ) );


		size_t A = 0;
		size_t B = 0;

		while(	!fromA.empty( ) ||
				!fromB.empty( ) )
		{
			bool isFromA;
			L l;

			if( !fromA.empty( ) &&
				!fromB.empty( ) )
			{
				if( fromA.begin( )->t1 <= fromB.begin( )->t1 )
				{
					isFromA = true;
					l = *fromA.begin( );
					fromA.erase( fromA.begin( ) );

					A += 1;
				}
				else
				{
					isFromA = false;
					l = *fromB.begin( );
					fromB.erase( fromB.begin( ) );

					B += 1;
				}
			}
			else
			{
				if( !fromA.empty( ) )
				{
					isFromA = true;
					l = *fromA.begin( );
					fromA.erase( fromA.begin( ) );

					A += 1;
				}
				else
				{
					isFromA = false;
					l = *fromB.begin( );
					fromB.erase( fromB.begin( ) );

					B += 1;
				}
			}

			while( true )
			{
				if( isFromA )
				{
					std::vector< L >::iterator itt;
					for( itt = fromB.begin( ); itt != fromB.end( ); ++itt )
						if( l.t2 <= (*itt).t1 )
							break;
					if( itt != fromB.end( ) )
					{
						isFromA = false;
						l = *itt;
						fromB.erase( itt );
					}
					else
					{
						break;
					}
				}
				else
				{
					std::vector< L >::iterator itt;
					for( itt = fromA.begin( ); itt != fromA.end( ); ++itt )
						if( l.t2 <= (*itt).t1 )
							break;
					if( itt != fromA.end( ) )
					{
						isFromA = true;
						l = *itt;
						fromA.erase( itt );
					}
					else
					{
						break;
					}
				}
			}
		}

		out << "Case #";
		out << c + 1;
		out << ": ";
		out << A;
		out << " ";
		out << B;
		out << "\n";
	}

	return 0;
}

