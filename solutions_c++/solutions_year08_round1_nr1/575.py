
//----------------------------------------------------------------------------

#define _USE_MATH_DEFINES
#include <math.h>

#include <functional>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <vector>
#include <queue>

//----------------------------------------------------------------------------

#define DBGOUT( ex ) std::cout << #ex << " == " << ( ex ) << std::endl
	
//----------------------------------------------------------------------------

template< typename I >
	bool put_stream( std::ostream & ostr, I beg, I end, char const * sep = " ", char const * suf = "\n" )
	{
		if( beg == end )
			return false;

		if( false == ostr.good( ) )
			return false;

		ostr << *beg;
		for( ++beg ; beg != end ; ++beg )
			ostr << sep << *beg;
		ostr << suf;

		return true;
	}
	
template< typename T >
	bool put_stream( std::ostream & ostr, std::vector< T > & vec, char const * sep = " ", char const * suf = "\n" )
	{
		return put_stream( ostr, vec.begin( ), vec.end( ), sep, suf );
	}
	
template< typename T >
	bool put_stream( std::ostream & ostr, std::vector< std::vector< T > > & vec, char const * sep = " ", char const * suf = "\n" )
	{
		for( size_t i = 0 ; i < vec.size( ) ; ++i )
		{
			if( false == put_stream( ostr, vec[ i ].begin( ), vec[ i ].end( ), sep, suf ) )
				return false;
		}

		return true;
	}
	
//----------------------------------------------------------------------------

template< typename T >
	bool get_stream( std::istream & istr, std::vector< T > & vec, int count = -1 )
	{
		vec.clear( );

		if( false == istr.good( ) )
			return false;

		T val;

		for( int i = 0 ; i != count ; ++i )
		{
			if( true == istr.eof( ) )
				return false;

			if( !( istr >> val ) )
				return false;

			vec.push_back( val );
		}

		return true;
	}
	
template< typename T >
	bool get_stream( std::istream & istr, std::vector< std::vector< std::vector< T > > > & vec )
	{
		if( false == istr.good( ) )
			return false;

		int n; if( ! ( istr >> n ) ) return false;
		
		vec.resize( n );
		for( int i = 0 ; i < n ; ++i )
		{
			int t; if( ! ( istr >> t ) ) return false;
			
			vec[ i ].resize( 2 );
			get_stream( istr, vec[ i ][ 0 ], t );
			get_stream( istr, vec[ i ][ 1 ], t );
		}

		return true;
	}
	
//----------------------------------------------------------------------------

template< typename T >
	void rearrange( std::vector< std::vector< T > > & vec )
	{
		std::sort( vec[ 0 ].begin( ), vec[ 0 ].end( ), std::greater< T >( ) );
		std::sort( vec[ 1 ].begin( ), vec[ 1 ].end( ), std::less< T >( ) );
	}
	
template< typename T >
	T calculate( std::vector< std::vector< T > > & vec )
	{
		size_t size = vec[ 0 ].size( );
		
		T product = 0;
		for( size_t i = 0 ; i < size ; ++i )
			product += vec[ 0 ][ i ] * vec[ 1 ][ i ];

		return product;
	}
	
//----------------------------------------------------------------------------

int main( int argc, char ** argv )
{
	std::vector< std::vector< std::vector< long long > > > input;

	if( false == get_stream( std::ifstream( "input.txt" ), input ) )
		return 0;

	std::ofstream ofst( "output.txt" );
	if( false == ofst.good( ) )
		return 0;

	for( size_t i = 0 ; i < input.size( ) ; ++i )
	{
		rearrange< long long >( input[ i ] );
		//put_stream< int >( std::cout, input[ i ] );
		//DBGOUT( calculate< int >( input[ i ] ) );

		ofst << "Case #" << ( i + 1 ) << ": " << calculate< long long >( input[ i ] ) << std::endl;
	}

	return 0;
}
	
//----------------------------------------------------------------------------