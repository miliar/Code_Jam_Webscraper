// test_A.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"
#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <iostream>
#include <fstream>


struct Letter
{
	Letter( int _l, int _pos ) :
		l( _l ),
		pos( _pos )
	{
	}

	int l;
	int pos;
};


int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream in;
	in.open( "C-small-attempt0.in" );

	std::fstream out;
	out.open( "C-small.out", std::ios_base::out );

	std::string welcomeString = "welcome to code jam";
	std::set< char > welcomeStringChars;
	for( unsigned int i = 0; i < welcomeString.length( ); ++i )
		welcomeStringChars.insert( welcomeString[ i ] );
	unsigned int welcomeStringLength = welcomeString.length( );

	int N = 0;
	in >> N;

	std::string dummyString;
	std::getline( in, dummyString );

	for( int caseIndex = 0; caseIndex < N; ++caseIndex )
	{
		std::string caseString;
		std::getline( in, caseString );

		std::string checkString;
		for( unsigned int i = 0; i < caseString.length( ); ++i )
		{
			char c = caseString[ i ];
			if( welcomeStringChars.find( c ) != welcomeStringChars.end( ) )
				checkString.push_back( c );
		}

		std::stack< Letter > lettersStack;

		for( unsigned int i = 0; i < checkString.length( ); ++i )
			if( checkString[ i ] == welcomeString[ 0 ] )
			{
				lettersStack.push( Letter( 0, i ) );
				break;
			}

		__int64 R = 0;

		while( !lettersStack.empty( ) )
		{
			Letter& l = lettersStack.top( );
			if( l.l != welcomeStringLength - 1 )
			{
				char c = welcomeString[ l.l + 1 ];

				bool find = false;
				for( unsigned int i = l.pos + 1; i < checkString.size( ); ++i )
				{
					if( c == checkString[ i ] )
					{
						find = true;
						lettersStack.push( Letter( l.l + 1, i) );
						break;
					}
				}

				if( !find )
				{
					while( !lettersStack.empty( ) )
					{
						int pos = lettersStack.top( ).pos;
						int ll = lettersStack.top( ).l;
						char cc = welcomeString[ ll ];
						lettersStack.pop( );

						bool find = false;
						for( unsigned int i = pos + 1; i < checkString.size( ); ++i )
						{
							if( cc == checkString[ i ] )
							{
								find = true;
								lettersStack.push( Letter( ll, i) );
								break;
							}
						}

						if( find )
							break;
					}
				}
			}
			else
			{
				R += 1;

				while( !lettersStack.empty( ) )
				{
					int pos = lettersStack.top( ).pos;
					int ll = lettersStack.top( ).l;
					char cc = welcomeString[ ll ];
					lettersStack.pop( );

					bool find = false;
					for( unsigned int i = pos + 1; i < checkString.size( ); ++i )
					{
						if( cc == checkString[ i ] )
						{
							find = true;
							lettersStack.push( Letter( ll, i) );
							break;
						}
					}

					if( find )
						break;
				}
			}
		}

		R = R % 10000;

		out << "Case #" << caseIndex + 1 << ": ";
		if( R <= 9 )
		{
			out << "0";
			out << "0";
			out << "0";
			out << R;
		}
		else if( R <= 99 )
		{
			out << "0";
			out << "0";
			out << R;
		}
		else if( R <= 999 )
		{
			out << "0";
			out << R;
		}
		else
		{
			out << R;
		}
		out << "\n";
		out.flush( );

		std::cout << "Case #" << caseIndex + 1 << "\n";
	}

	out.flush( );
	out.close( );

	return 0;
}


/*
int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream in;
	in.open( "A-large.in" );

	std::fstream out;
	out.open( "A-large.out", std::ios_base::out );

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
		out.flush( );

		std::cout << "Case #" << i + 1 << "\n";
	}

	out.close( );

	return 0;
}
*/

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
