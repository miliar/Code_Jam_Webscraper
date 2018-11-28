
//----------------------------------------------------------------------------

#include <algorithm>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <vector>
#include <set>

//----------------------------------------------------------------------------

#define DBGOUT( x ) std::cout << #x << " == " << ( x ) << std::endl;

//----------------------------------------------------------------------------

typedef char							 char_type;
typedef size_t							 size_type;
typedef std::basic_ifstream< char_type > ifst_type;
typedef std::basic_ofstream< char_type > ofst_type;
typedef std::basic_string< char_type >	 bstr_type;
typedef std::vector< bstr_type >		 vstr_type;
typedef std::set< bstr_type >			 sstr_type;
typedef std::vector< size_type >		 vint_type;
typedef std::vector< vint_type >		 memo_type;

struct data_type
{
	vstr_type engine;
	vint_type query;
};
	
typedef std::vector< data_type > vdat_type;

//----------------------------------------------------------------------------

bool read_case( ifst_type & ifst, data_type & input )
{
	vstr_type & engine = input.engine; engine.clear( );
	vint_type & query = input.query; query.clear( ); 
	char_type temp[ 256 ];

	if( true == ifst.eof( ) )
		return false;

	size_type s = 0; ifst >> s; ifst.get( );
	for( size_type i = 0 ; i < s ; ++i )
	{
		if( true == ifst.eof( ) )
			return false;

		ifst.getline( temp, 256 );
		engine.push_back( temp );
	}

	if( true == ifst.eof( ) )
		return false;

	vstr_type::const_iterator ebeg = engine.begin( );
	vstr_type::const_iterator eend = engine.end( );

	size_type q = 0; ifst >> q; ifst.get( ); query.reserve( q + 1 ); query.push_back( -1 );
	for( size_type i = 0 ; i < q ; ++i )
	{
		if( true == ifst.eof( ) )
			return false;

		ifst.getline( temp, 256 );

		vstr_type::const_iterator etmp = ebeg;
		for( etmp ; etmp != eend ; ++etmp )
		{
			if( NULL != strstr( temp, etmp->c_str( ) ) )
			{
				//if( ( etmp - ebeg ) != query.back( ) )
					query.push_back( etmp - ebeg );
			}
		}
	}

	return true;
}
bool read_file( ifst_type & ifst, vdat_type & input )
{
	input.clear( ); 
	
	ifst.setf( ifst.skipws );
	if( false == ifst.good( ) )
		return false;

	size_type n = 0; ifst >> n; input.resize( n );
	for( size_type i = 0 ; i < n ; ++i )
		if( false == read_case( ifst, input[ i ] ) )
			return false;

	return true;
}
	
//----------------------------------------------------------------------------

size_type find_minimum_memo( memo_type const & memo,
							 size_type		   q,
							 size_type		   m = -1 )
{
	size_type msize = memo.size( );

	size_type answer = m == 0 ? 1000000 : memo[ 0 ][ q ];
	for( size_type i = 1 ; i < msize ; ++i )
		answer = std::min( answer, i == 0 ? 1000000 : memo[ i ][ q ] );

	return answer;
}
size_type find_optimum_change( vint_type const & query,
							   vstr_type const & engine )
{
	size_type esize = engine.size( );
	size_type qsize = query.size( );

	if( esize == 1 )
		return qsize;

	memo_type memo; memo.resize( esize );

	for( size_type i = 0 ; i < esize ; ++i )
	{
		memo[ i ].resize( qsize, -1 );
		//memo[ i ][ qsize - 1 ] = query[ qsize - 1 ] == i;
		memo[ i ][ 0 ] = query[ 0 ] == i;
	}

	for( size_type q = 1 ; q < qsize ; ++q )
	{
		for( size_type m = 0 ; m < esize ; ++m )
		{
			memo[ m ][ q ] = ( m == query[ q - 0 ] ? 1 + find_minimum_memo( memo, q - 1 ) :
							 ( m == query[ q - 1 ] ? 1 + find_minimum_memo( memo, q - 1, m ) : memo[ m ][ q - 1 ] ) );
		}
	}
	
	/*
	std::cout << "  ";
	for( size_type q = 1 ; q < qsize ; ++q )
		std::cout << query[ q ] << " ";
	std::cout << std::endl;

	for( size_type m = 0 ; m < esize ; ++m )
	{
		for( size_type q = 0 ; q < qsize ; ++q )
			std::cout << memo[ m ][ q ] << " ";
		std::cout << std::endl;
	}
	//*/

	return find_minimum_memo( memo, qsize - 1 );
}
	
//----------------------------------------------------------------------------

int main( int, char ** )
{
	ofst_type ofst( "output.txt" );
	ifst_type ifst( "input.txt" );
	vdat_type input;

	if( false == read_file( ifst, input ) )
	{	
		std::cerr << "error : can not open the input file !!!" << std::endl;
		return 0;
	}

	for( size_type i = 0 ; i < input.size( ) ; ++i )
	{
		vstr_type & engine = input[ i ].engine;
		vint_type & query  = input[ i ].query;

		DBGOUT( query.size( ) );

		//*
		int change = find_optimum_change( query, engine );
		ofst << "Case #" << ( i + 1 ) << ": " << change << std::endl; 
		std::cerr << "Case #" << ( i + 1 ) << ": " << change << std::endl;
		//*/
	}

	return 0;
}
	
//----------------------------------------------------------------------------