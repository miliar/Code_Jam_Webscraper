// test_A.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"
#include <string>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <fstream>


int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream in;
	in.open( "A-small-attempt0.in" );

	std::fstream out;
	out.open( "A-small.out", std::ios_base::out );

	int L = 0;
	in >> L;

	int D = 0;
	in >> D;

	int N = 0;
	in >> N;

	std::vector< std::map< char, std::set< int > > > dictionary( L );
	for( int i = 0; i < D; ++i )
	{
		std::string s;
		in >> s;

		for( unsigned int j = 0; j < s.length( ); ++j )
		{
			char c = s[ j ];

			std::pair< std::map< char, std::set< int > >::iterator, bool > p;
			p = dictionary[ j ].insert( std::pair< char, std::set< int > >( c, std::set< int >( ) ) );
			(*p.first).second.insert( i );
		}
	}

	for( int i = 0; i < N; ++i )
	{
		std::vector< std::set< int > > possibilities( L );

		std::string s;
		in >> s;

		unsigned int j = 0;
		unsigned int k = 0;
		std::set< int > v;
		bool isInside = false;
		while( j < s.length( ) )
		{
			char c = s[ j ];
			if( c != '(' &&
				c != ')' )
			{
				std::map< char, std::set< int > >::iterator it = dictionary[ k ].find( c );
				if( it != dictionary[ k ].end( ) )
				{
					for( std::set< int >::iterator itt = (*it).second.begin( ); itt != (*it).second.end( ); ++itt )
						v.insert( (*itt) );
				}

				if( isInside )
				{
				}
				else
				{
					possibilities[ k ] = v;
					k += 1;
					v.clear( );
				}
			}
			else if( c == '(' )
			{
				isInside = true;
			}
			else if( c == ')' )
			{
				isInside = false;

				possibilities[ k ] = v;
				k += 1;
				v.clear( );
			}

			j += 1;
		}

		int R = 0;
		for( std::set< int >::iterator it = possibilities[ 0 ].begin( ); it != possibilities[ 0 ].end( ); ++it )
		{
			int t = (*it);

			bool good = true;
			for( unsigned int j = 0; j < possibilities.size( ); ++j )
			{
				if( possibilities[ j ].find( t ) == possibilities[ j ].end( ) )
				{
					good = false;
					break;
				}
			}

			if( good )
				R += 1;
		}

		out << "Case #" << i + 1 << ": ";
		out << R;
		out << "\n";
	}

	out.flush( );
	out.close( );

	return 0;

/*	for( int i = 0; i < N; ++i )
	{
		std::vector< int > posibilities( L );

		std::string s;
		in >> s;

		unsigned int j = 0;
		unsigned int k = 0;
		unsigned int n = 0;
		bool isInside = false;
		while( j < s.length( ) )
		{
			char c = s[ j ];
			if( c != '(' &&
				c != ')' )
			{
				bool isValid = (dictionary[ k ].find( c ) != dictionary[ k ].end( ));
				if( isValid )
					n += 1;

				if( isInside )
				{
				}
				else
				{
					posibilities[ k ] = n;
					k += 1;
					n = 0;
				}
			}
			else if( c == '(' )
			{
				isInside = true;
			}
			else if( c == ')' )
			{
				isInside = false;

				posibilities[ k ] = n;
				k += 1;
				n = 0;
			}

			j += 1;
		}

		int P = 1;
		for( unsigned int j = 0; j < posibilities.size( ); ++j )
			P *= posibilities[ j ];

		out << "Case #" << i << ": ";
		out << P;
		out << "\n";
	}
*/
}

/*
#include "stdafx.h"
#include <vector>
#include <map>
#include <iostream>
#include <fstream>


bool testWhiteSpaces( char c )
{
	if( c == ' ' || c == '\t' || c == '\n' || c == '\r' )
		return true;
	return false;
}


void readChars( std::ifstream& in, std::vector< char >& buffer )
{
	char c;
	c = in.get( );

	while( testWhiteSpaces( c ) )
		c = in.get( );
	while( !testWhiteSpaces( c ) )
	{
		buffer.push_back( c );
		c = in.get( );
	}
}


size_t toDecimal( const std::vector< char >& value, std::map< char, size_t >& alphabet )
{
	size_t v = 0;
	size_t n = alphabet.size( );
	for( size_t i = 0; i < value.size( ); ++i )
		v = v * n + alphabet.find( value[ i ] )->second;
	return v;
}


void fromDecimal( size_t v, const std::map< size_t, char >& alphabet, std::vector< char >& value )
{
	size_t n = alphabet.size( );
	while( v )
	{
		size_t i = v % n;
		v = (v - i) / n;

		value.push_back( alphabet.find( i )->second );
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

	for( size_t i = 0; i < numCases; ++i )
	{
		std::vector< char > valueIn;
		readChars( in, valueIn );

		std::map< char, size_t > alphabetIn;
		{
			std::vector< char > v;
			readChars( in, v );
			for( size_t i = 0; i < v.size( ); ++i )
				alphabetIn.insert( std::pair< char, size_t >( v[ i ], i ) );
		}

		std::map< size_t, char > alphabetOut;
		{
			std::vector< char > v;
			readChars( in, v );
			for( size_t i = 0; i < v.size( ); ++i )
				alphabetOut.insert( std::pair< size_t, char >( i, v[ i ] ) );
		}

		size_t decimal = toDecimal( valueIn, alphabetIn );

		std::vector< char > valueOut;
		fromDecimal( decimal, alphabetOut, valueOut );

		out << "Case #";
		out << i + 1;
		out << ": ";
		for( size_t j = 0; j < valueOut.size( ); ++j )
			out << valueOut[ valueOut.size( ) - j - 1 ];
		out << "\n";
	}

	return 0;
}
*/
