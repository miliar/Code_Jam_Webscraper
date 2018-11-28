// tic_tac_toe.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

enum state
{
	enf,
	ex,
	eo,
	ed,
};

struct look
{
	char a[ 4 ];
	size_t x;
	size_t o;
	size_t t;
	size_t not;
	size_t nf;

	look( )
		:x( 0 )
		,o( 0 )
		,t( 0 )
		,not( 0 )
		,nf( 0 )
	{ }

	state test( )
	{
		x= 0;
		o= 0;
		t= 0;
		for( size_t i= 0; i < 4; ++i )
		{
			if( a[ i ] == 'X' )
				++x;

			else if( a[ i ] == 'O' )
				++o;

			else if( a[ i ] == 'T' )
				++t;

			else if( a[ i ] == '.' )
				++not;

			else
				++nf;
		}
		if( x == 4 || x == 3 && t == 1 )
			return ex;

		if( o == 4 || o == 3 && t == 1 )
			return eo;

		if( not )
			return enf;

		return ed;
	}
};

typedef std::vector< char* > board;
typedef std::vector< state > states;


int _tmain(int argc, _TCHAR* argv[])
{
	std::fstream is( "input.txt", std::ios::in );
	size_t count;
	is >> count;
	std::fstream os( "out.txt", std::ios::ate | std::ios::out );

	for( size_t i= 0; i < count; ++i )
	{
		bool d= false;
		bool o= false;
		bool x= false;
		bool nf= false;
		board aboard;
		for( size_t rowc= 0; rowc < 4; ++rowc )
		{
			char* arow= new char[ 4 ];
			is >> arow[ 0 ] >> arow[ 1 ] >> arow[ 2 ] >> arow[ 3 ];
			aboard.push_back( arow );	
		}
		//rows
		for( size_t j= 0; j < 4; ++j )
		{
			look l;
			l.a[ 0 ]= aboard.at( j )[ 0 ];
			l.a[ 1 ]= aboard.at( j )[ 1 ];
			l.a[ 2 ]= aboard.at( j )[ 2 ];
			l.a[ 3 ]= aboard.at( j )[ 3 ];
			if( l.test( ) == ex )
			{
				x= true;
				break;
			}
			if( l.test( ) == eo )
			{
				o= true;
				break;
			}
			if( l.test( ) == enf )
				nf= true;
		}
		if( ! x && ! o )
		{
			//cols
			for( size_t j= 0; j < 4; ++j )
			{
				look l;
				l.a[ 0 ]= aboard.at( 0 )[ j ];
				l.a[ 1 ]= aboard.at( 1 )[ j ];
				l.a[ 2 ]= aboard.at( 2 )[ j ];
				l.a[ 3 ]= aboard.at( 3 )[ j ];
				if( l.test( ) == ex )
				{
					x= true;
					break;
				}
				if( l.test( ) == eo )
				{
					o= true;
					break;
				}
				if( l.test( ) == enf )
					nf= true;
			}
		}
		if( ! x && ! o  )
		{
			look l;
			l.a[ 0 ]= aboard.at( 0 )[ 0 ];
			l.a[ 1 ]= aboard.at( 1 )[ 1 ];
			l.a[ 2 ]= aboard.at( 2 )[ 2 ];
			l.a[ 3 ]= aboard.at( 3 )[ 3 ];

			if( l.test( ) == ex )
			{
				x= true;
			}
			if( l.test( ) == eo )
			{
				o= true;
			}
			l.a[ 0 ]= aboard.at( 0 )[ 3 ];
			l.a[ 1 ]= aboard.at( 1 )[ 2 ];
			l.a[ 2 ]= aboard.at( 2 )[ 1 ];
			l.a[ 3 ]= aboard.at( 3 )[ 0 ];

			if( l.test( ) == ex )
			{
				x= true;
			}
			if( l.test( ) == eo )
			{
				o= true;
			}
		}

		os << "Case #" << i + 1 << ": ";

		if( o )
			os << "O won" << std::endl;

		else if( x )
			os << "X won" << std::endl;

		else if( ! nf )
			os << "Draw" << std::endl;

		else
			os << "Game has not completed" << std::endl;
			
	}
	os.close( );

	return 0;
}

