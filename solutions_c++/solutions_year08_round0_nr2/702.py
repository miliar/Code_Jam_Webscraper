
//----------------------------------------------------------------------------

#include <functional>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <vector>
#include <queue>

//----------------------------------------------------------------------------

#define DBGOUT( x ) std::cout << #x << " == " << ( x ) << std::endl;

//----------------------------------------------------------------------------

typedef char							 char_type;
typedef size_t							 size_type;
typedef std::vector< size_type >		 vint_type;
typedef std::basic_ifstream< char_type > ifst_type;
typedef std::basic_ofstream< char_type > ofst_type;

struct trip_type
{
	bool operator <= ( trip_type const & rhs ) const
	{
		return comp( rhs ) <= 0;
	}
	bool operator >= ( trip_type const & rhs ) const
	{
		return comp( rhs ) >= 0;
	}
	bool operator <  ( trip_type const & rhs ) const
	{
		return comp( rhs ) < 0;
	}
	bool operator >  ( trip_type const & rhs ) const
	{
		return comp( rhs ) > 0;
	}
	
	int comp( trip_type const & rhs ) const
	{
		return ( from < rhs.from ? -1 :
			   ( from > rhs.from ? +1 :
			   ( to   < rhs.to   ? -1 :
			   ( to   > rhs.to   ? +1 : 0 ) ) ) );
	}
	
	size_type from;
	size_type to;
};
	
typedef std::vector< trip_type > vtrp_type;

struct schd_type
{
	vtrp_type stta; // turning time
	vtrp_type sttb;	// station-A
	size_type turn;	// station-B
};
	
typedef std::vector< schd_type > vsch_type;

//----------------------------------------------------------------------------

bool read_trip( ifst_type & ifst, trip_type & input )
{
	char_type sign;
	
	input.from = 0;
	input.to   = 0;

	if( false == ifst.good( ) )
		return false;

	size_type hh1, mm1; ifst >> hh1 >> sign >> mm1;
	size_type hh2, mm2; ifst >> hh2 >> sign >> mm2;

	input.from = hh1 * 100 + mm1;
	input.to   = hh2 * 100 + mm2;

	return true;
}
bool read_case( ifst_type & ifst, schd_type & input )
{
	vtrp_type & stta = input.stta;
	vtrp_type & sttb = input.sttb;
	size_type & turn = input.turn;

	stta.clear( );
	sttb.clear( );
	if( false == ifst.good( ) )
		return false;

	size_type tt; ifst >> tt; turn = tt;
	size_type na; ifst >> na; stta.resize( na );
	size_type nb; ifst >> nb; sttb.resize( nb );

	for( size_type i = 0 ; i < na ; ++i )
		if( false == read_trip( ifst, stta[ i ] ) )
			return false;

	for( size_type i = 0 ; i < nb ; ++i )
		if( false == read_trip( ifst, sttb[ i ] ) )
			return false;

	std::stable_sort( stta.begin( ), stta.end( ) );
	std::stable_sort( sttb.begin( ), sttb.end( ) );
	return true;
}
bool read_file( ifst_type & ifst, vsch_type & input )
{
	input.clear( );
	if( false == ifst.good( ) )
		return false;

	size_type n; ifst >> n; input.resize( n );
	for( size_type i = 0 ; i < n ; ++i )
		if( false == read_case( ifst, input[ i ] ) )
			return false;

	return true;
}
	
//----------------------------------------------------------------------------

size_type advance_time( size_type t, size_type d )
{
	size_type mm = t % 100 + d;
	size_type hh = t / 100;

	if( mm >= 60 )
	{
		mm -= 60;
		hh += 1;

		//if( hh > 23 )
		//	hh = 0;
	}

	return hh * 100 + mm;
}
	
//----------------------------------------------------------------------------

void find_number_of_train( schd_type const & input, size_type & numa, size_type & numb )
{
	std::priority_queue< size_type, std::vector< size_type >, std::greater< size_type > > quea;
	std::priority_queue< size_type, std::vector< size_type >, std::greater< size_type > > queb;

	vtrp_type const & stta = input.stta;
	vtrp_type const & sttb = input.sttb;
	size_type const & turn = input.turn;

	size_type maxa = stta.size( );
	size_type maxb = sttb.size( );
	size_type runa = 0; numa = 0;
	size_type runb = 0; numb = 0;
	
	while( runa < maxa && runb < maxb )
	{
		if( stta[ runa ].from < sttb[ runb ].from )
		{
			int change = ( queb.empty( ) || queb.top( ) > stta[ runa ].from );
			if( change == 0 ) queb.pop( );
			numa += change;
			
			quea.push( advance_time( stta[ runa++ ].to, turn ) );
		}
		else
		{
			int change = ( quea.empty( ) || quea.top( ) > sttb[ runb ].from );
			if( change == 0 ) quea.pop( );			
			numb += change;
			
			queb.push( advance_time( sttb[ runb++ ].to, turn ) );
		}
	}

	for( runa ; runa < maxa ; ++runa )
	{
		int change = ( queb.empty( ) || queb.top( ) > stta[ runa ].from );
		if( change == 0 ) queb.pop( );
		numa += change;
	}

	for( runb ; runb < maxb ; ++runb )
	{
		int change = ( quea.empty( ) || quea.top( ) > sttb[ runb ].from );
		if( change == 0 ) quea.pop( );
		numb += change;
	}
}
	
//----------------------------------------------------------------------------

void print_schd( schd_type const & input )
{
	size_type const & turn = input.turn;
	std::cerr << "turn == " << turn << std::endl;
	
	vtrp_type const & stta = input.stta;
	std::cerr << "stta == " << std::setfill( '0' );
	for( size_type i = 0 ; i < stta.size( ) ; ++i )
		std::cerr << std::setw( 4 ) << stta[ i ].from << "-" << std::setw( 4 ) << stta[ i ].to << " ";
	std::cerr << std::endl;

	vtrp_type const & sttb = input.sttb;
	std::cerr << "sttb == " << std::setfill( '0' );
	for( size_type i = 0 ; i < sttb.size( ) ; ++i )
		std::cerr << std::setw( 4 ) << sttb[ i ].from << "-" << std::setw( 4 ) << sttb[ i ].to << " ";
	std::cerr << std::endl;

	std::cerr << std::endl;
}
	
//----------------------------------------------------------------------------

int main( int, char ** )
{
	ofst_type ofst( "output.txt" );
	ifst_type ifst( "input.txt" );
	vsch_type input;

	if( false == read_file( ifst, input ) )
	{	
		std::cerr << "error : can not open the input file !!!" << std::endl;
		return 0;
	}

	for( size_type i = 0 ; i < input.size( ) ; ++i )
	{
		schd_type & schd = input[ i ];
		size_type numa;
		size_type numb;

		find_number_of_train( input[ i ], numa, numb );
		
		ofst << "Case #" << ( i + 1 ) << ": " << numa << " " << numb << std::endl;

		print_schd( schd );
		std::cerr << "numa == " << numa << std::endl;
		std::cerr << "numb == " << numb << std::endl;
		std::cerr << std::endl;
	}

	return 0;
}
	
//----------------------------------------------------------------------------