#include	<iostream>
#include	<fstream>
#include	<sstream>
using	namespace	std;

#include	<boost/tokenizer.hpp>
using	namespace	boost;

#include	<math.h>

#include	<JpMooParaiso/Saturn.h>
using	namespace	JpMooParaiso::Saturn;
using	namespace	JpMooParaiso::Saturn::G;

struct
Board
{	char	m[ 16 ];
	char&
	E( int pY, int pX )
	{	return m[ pY * 4 + pX ];
	}

	bool
	C( char p, int pY, int pX )
	{	char w = E( pY, pX );
		return w == p || w == 'T';
	}
	
	char
	DEqual1()
	{	char v = E( 0, 0 );
		switch ( v )
		{
		case '.':	return 0;
		case 'T':
			v = E( 1, 1 );
			return ( C( v, 2, 2 ) && C( v, 3, 3 ) ) ? v : 0;
		case 'X':
		case 'O':
			return ( C( v, 1, 1 ) && C( v, 2, 2 ) && C( v, 3, 3 ) ) ? v : 0;
		}
		assert( false );
	}
	char
	DEqual2()
	{	char v = E( 3, 0 );
		switch ( v )
		{
		case '.':	return 0;
		case 'T':
			v = E( 2, 1 );
			return ( C( v, 1, 2 ) && C( v, 0, 3 ) ) ? v : 0;
		case 'X':
		case 'O':
			return ( C( v, 2, 1 ) && C( v, 1, 2 ) && C( v, 0, 3 ) ) ? v : 0;
		}
		assert( false );
	}
	char
	VEqual( int p )
	{	char v = E( 0, p );
		switch ( v )
		{
		case '.':	return 0;
		case 'T':
			v = E( 1, p );
			return ( C( v, 2, p ) && C( v, 3, p ) ) ? v : 0;
		case 'X':
		case 'O':
			return ( C( v, 1, p ) && C( v, 2, p ) && C( v, 3, p ) ) ? v : 0;
		}
		assert( false );
	}
	char
	HEqual( int p )
	{	char v = E( p, 0 );
		switch ( v )
		{
		case '.':	return 0;
		case 'T':
			v = E( p, 1 );
			return ( C( v, p, 2 ) && C( v, p, 3 ) ) ? v : 0;
		case 'X':
		case 'O':
			return ( C( v, p, 1 ) && C( v, p, 2 ) && C( v, p, 3 ) ) ? v : 0;
		}
		assert( false );
	}

	string
	WonString( char p )
	{
		char v[ 16 ];
		sprintf( v, "%c won", p );
		return v;
	}

	string
	Check()
	{
		char w;

		w = DEqual1();
		if ( w ) return WonString( w );

		w = DEqual2();
		if ( w ) return WonString( w );

		for ( int i = 0; i < 4; i++ )
		{
			w = HEqual( i );
			if ( w ) return WonString( w );
			w = VEqual( i );
			if ( w ) return WonString( w );
		}

		for ( int y = 0; y < 4; y++ )
		{	for ( int x = 0; x < 4; x++ )
			{	if ( E( y, x ) == '.' ) return "Game has not completed";
			}
		}
		return "Draw";
	}

	void
	Dump()
	{	for ( int y = 0; y < 4; y++ )
		{
			for ( int x = 0; x < 4; x++ )
			{
				cout << E( y, x );
			}
			cout << endl;
		}
	}
};

int
main( int argc, char* argv[] )
{
	cout << "I:" << argv[ 1 ] << endl;
	cout << "O:" << argv[ 2 ] << endl;

	ifstream wIFS( argv[ 1 ] );
	assert( wIFS.good() );
	ofstream wOFS( argv[ 2 ] );

	string	wLine;
	getline( wIFS, wLine );
	istringstream wISS( wLine );
	size_t	wT;
	wISS >> wT;

#if 1
	for ( size_t i = 0; i < wT; i++ )
	{
		Board	w;
		for ( int y = 0; y < 4; y++ )
		{
			wIFS >> wLine;
			for ( int x = 0; x < 4; x++ )
			{	w.E( y, x ) = wLine[ x ];
			}
		}
//		wIFS >> wLine;

		cout << i << endl;
		w.Dump();
		string v = w.Check();
		wOFS << "Case #" << ( i + 1 ) << ": " << v << endl;
		cout << "Case #" << ( i + 1 ) << ": " << v << endl;
	}

#else
	struct
	Pair
	{	size_t	mK;
		string	mV;
	};
	__block	List<Pair>	v;

	dispatch_queue_t		wQ = ::dispatch_get_global_queue( DISPATCH_QUEUE_PRIORITY_DEFAULT, 0 );
	dispatch_group_t		wG = ::dispatch_group_create();
	dispatch_semaphore_t	wS = ::dispatch_semaphore_create( 1 );

	for ( size_t i = 0; i < wT; i++ )
	{
		string	wS1;
		string	wS2;
		wIFS >> wS1;
		wIFS >> wS2;

		::dispatch_group_async
		(	wG
		,	wQ
		,	^{	Pair	w;
				w.mK = i;
				w.mV = Main( wS1, wS2 );
				::dispatch_semaphore_wait( wS, DISPATCH_TIME_FOREVER );
				v.Insert( w, [ & ]( Pair const& p ){ return w.mK > p.mK; } );
				::dispatch_semaphore_signal( wS );
			}
		);
	}

	::dispatch_group_wait( wG, DISPATCH_TIME_FOREVER );

	v.ForAll
	(	[ & ]( Pair const& p )
		{	wOFS << "Case #" << ( p.mK + 1 ) << ": " << p.mV << endl;
			cout << "Case #" << ( p.mK + 1 ) << ": " << p.mV << endl;
		}
	);
#endif
}
