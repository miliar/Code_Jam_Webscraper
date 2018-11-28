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
	in.open( "C-large.in" );

	std::fstream out;
	out.open( "C-large.out", std::ios_base::out );

	int numCases = 0;
	in >> numCases;

	for( int caseIndex = 0; caseIndex < numCases; ++caseIndex )
	{
		unsigned int N = 0;
		in >> N;

		std::vector< unsigned int > C( N );
		for( unsigned int i = 0; i < N; ++i )
			in >> C[ i ];

		std::sort( C.begin( ), C.end( ) );

		unsigned int ALL = 0;
		for( unsigned int i = 0; i < N; ++i )
			ALL += C[ i ];

		std::vector< std::vector< char > > AA( N );
		for( unsigned int i = 0; i < N; ++i )
		{
			AA[ i ].resize( 32 );
			for( unsigned int j = 0; j < 32; ++j )
				AA[ i ][ j ] = (char) ((C[ i ] & (1 << j)) != 0);
		}

		std::vector< unsigned int > CC( 32 );
		for( unsigned int j = 0; j < 32; ++j )
			for( unsigned int i = 0; i < N; ++i )
				CC[ j ] += AA[ i ][ j ];

		bool canDo = true;
		for( unsigned int j = 0; j < 32; ++j )
			if( CC[ j ] % 2 != 0 )
			{
				canDo = false;
				break;
			}

		unsigned int R = 0;

		if( canDo )
		{
			for( unsigned int B = 1; B < N; ++B )
			{
				std::vector< unsigned int > CCC( 32 );
				for( unsigned int j = 0; j < 32; ++j )
					for( unsigned int i = 0; i < B; ++i )
						CCC[ j ] += AA[ i ][ j ];

				bool isCorrect = true;
				for( unsigned int j = 0; j < 32; ++j )
					if( (CCC[ j ] % 2) != ((CC[ j ] - CCC[ j ]) % 2) )
					{
						isCorrect = false;
						break;
					}

				if( isCorrect )
				{
					unsigned int S = 0;
					for( unsigned int i = 0; i < B; ++i )
						S += C[ i ];

					unsigned int SS = S;
					if( SS < (ALL - S) )
						SS = (ALL - S);
					if( R < SS )
						R = SS;
				}
			}
		}

		std::cout << "Case #" << caseIndex + 1 << ": Done" << std::endl;

		out << "Case #" << caseIndex + 1 << ": ";
		if( canDo )
			out << R;
		else
			out << "NO";
		out << "\n";
		out.flush( );
	}

	out.flush( );
	out.close( );

	return 0;
}


/*
struct Combine
{
	Combine( char _c1, char _c2 ) :
		c1( _c1 ),
		c2( _c2 )
	{
	}

	bool operator<( const Combine& c ) const
	{
		if( c1 < c.c1 )
			return true;
		if( c1 > c.c1 )
			return false;
		if( c2 < c.c2 )
			return true;
		return false;
	}

	char c1;
	char c2;
};


struct Opposed
{
	char c1;
	char c2;
};


int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream in;
	in.open( "B-large.in" );

	std::fstream out;
	out.open( "B-large.out", std::ios_base::out );

	int numCases = 0;
	in >> numCases;

	for( int caseIndex = 0; caseIndex < numCases; ++caseIndex )
	{
		unsigned int C = 0;
		in >> C;

		std::map< Combine, char > combine;
		for( unsigned int i = 0; i < C; ++i )
		{
			char c1 = 0;
			in >> c1;

			char c2 = 0;
			in >> c2;

			char c3 = 0;
			in >> c3;

			combine.insert( std::pair< Combine, char >( Combine( c1, c2 ), c3 ) );
		}

		unsigned int D = 0;
		in >> D;

		std::vector< Opposed > opposed( D );
		for( unsigned int i = 0 ;i < D; ++i )
		{
			in >> opposed[ i ].c1;
			in >> opposed[ i ].c2;
		}

		unsigned int N = 0;
		in >> N;

		std::vector< char > invoked( N );
		for( unsigned int i = 0; i < N; ++i )
			in >> invoked[ i ];

		std::map< char, char > O1;
		for( unsigned int i = 0; i < D; ++i )
			O1.insert( std::pair< char, char >( opposed[ i ].c1, opposed[ i ].c2 ) );
		std::map< char, char > O2;
		for( unsigned int i = 0; i < D; ++i )
			O1.insert( std::pair< char, char >( opposed[ i ].c2, opposed[ i ].c1 ) );

		std::vector< char > R;
		std::map< char, int > A;

		for( unsigned int i = 0; i < N; ++i )
		{
			std::queue< char > c;
			c.push( invoked[ i ] );

			while( !c.empty( ) )
			{
				char cc = c.front( );
				c.pop( );

				bool canCombine = false;
				if( !R.empty( ) )
				{
					char pc = R.back( );
					std::map< Combine, char >::iterator it = combine.find( Combine( pc, cc ) );
					if( it == combine.end( ) )
						it = combine.find( Combine( cc, pc ) );
					if( it != combine.end( ) )
					{
						R.pop_back( );
						A[ pc ] -= 1;

						c.push( (*it).second );
					
						canCombine = true;
					}
				}

				bool canClear = false;
				if( !canCombine )
				{
					bool isOc = false;
					char oc = 0;

					std::map< char, char >::iterator it = O1.find( cc );
					if( it != O1.end( ) )
					{
						isOc = true;
						oc = (*it).second;
					}
					else
					{
						std::map< char, char >::iterator it = O2.find( cc );
						if( it != O2.end( ) )
						{
							isOc = true;
							oc = (*it).second;
						}
					}

					if( isOc )
					{
						std::map< char, int >::iterator itt = A.find( oc );
						if( itt != A.end( ) )
						{
							if( (*itt).second > 0 )
							{
								R.clear( );
								A.clear( );

								canClear = true;
							}
						}
					}
				}

				if( !canCombine &&
					!canClear )
				{
					R.push_back( cc );

					std::pair< std::map< char, int >::iterator, bool > p = A.insert( std::pair< char, int >( cc, 0 ) );
					(*p.first).second += 1;
				}
			}
		}

		std::cout << "Case #" << caseIndex + 1 << ": Done" << std::endl;

		out << "Case #" << caseIndex + 1 << ": ";
		out << "[";
		unsigned int RS = R.size( );
		for( unsigned int i = 0; i + 1 < RS; ++i )
		{
			out << R[ i ];
			out << ", ";
		}
		if( RS )
			out << R[ RS - 1 ];
		out << "]";
		out << "\n";
		out.flush( );
	}

	out.flush( );
	out.close( );

	return 0;
}
*/


/*
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
*/