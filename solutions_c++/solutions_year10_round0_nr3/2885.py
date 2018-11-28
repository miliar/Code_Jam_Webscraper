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


struct Gr
{
	Gr( unsigned int _n ) :
		n( _n ),
		c( 0 )
	{
	}

	Gr( unsigned int _n, unsigned int _c ) :
		n( _n ),
		c( _c )
	{
	}

	unsigned int n;
	unsigned int c;
};


int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream in;
	in.open( "C-small-attempt0.in" );

	std::fstream out;
	out.open( "C-small-attempt0.out", std::ios_base::out );

	int T = 0;
	in >> T;

	for( int caseIndex = 0; caseIndex < T; ++caseIndex )
	{
		unsigned int R = 0;
		in >> R;
		
		unsigned int K = 0;
		in >> K;

		unsigned int N = 0;
		in >> N;

		std::queue< Gr > G;
		for( unsigned int i = 0; i < N; ++i )
		{
			unsigned int g;
			in >> g;
			G.push( Gr( g ) );
		}

		unsigned int P = 0;
		unsigned int r = 0;

		unsigned int k = 0;
		std::vector< Gr > g;

		while( true )
		{
			if( G.empty( ) )
			{
				if( g.empty( ) )
				{
					break;
				}
				else
				{
					P += k;
					r += 1;
					if( r >= R )
						break;

					for( unsigned int i = 0; i < g.size( ); ++i )
						G.push( g[ i ] );
					k = 0;
					g.clear( );
				}
			}

			if( k + G.front( ).n <= K )
			{
				k += G.front( ).n;
				g.push_back( G.front( ) );
				G.pop( );
			}
			else
			{
				P += k;
				r += 1;
				if( r >= R )
					break;

				for( unsigned int i = 0; i < g.size( ); ++i )
					G.push( g[ i ] );
				k = 0;
				g.clear( );
			}
		}

		out << "Case #" << caseIndex + 1 << ": ";
		out << P;
		out << "\n";
		out.flush( );
	}

	out.flush( );
	out.close( );

	return 0;
}