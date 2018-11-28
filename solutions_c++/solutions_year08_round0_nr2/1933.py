#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cmath>
#include <cctype>
#include <vector>
#include <queue>
#include <list>
#include <map>
using namespace std;

#define FOR( i, a, b ) for( int i = a; i < b; ++i )
#define REP( i, n ) FOR( i, 0, n )
#define INF_LOOP( i ) for( int i = 0;; ++i )
#define FORE(it, x ) for( typeof( x.begin( ) ) it; it != x.end( ); ++it )
#define MIN( a, b ) ( a < b ) ? a : b
#define MAX( a, b ) ( a > b ) ? a : b

struct trip
{
	int start;
	int end;
};

int toMinutes( string time );
bool greater_trip( trip a, trip b );

int main( )
{
	ifstream ifs;
	ofstream ofs;

	ifs.open( "B-large.in" );
	ofs.open( "B-large.out" );

	int cases = 0;

	ifs >> cases;

	FOR( k, 1, cases + 1 )
	{
		string hour = "";
		int TurnAround = 0;
		int a_trains = 0;
		int b_trains = 0;
		vector<int> onA;
		vector<int> onB;
		vector<trip> a;
		vector<trip> b;
		int size = 0;

		ifs >> TurnAround;
		ifs >> size; a.resize( size );
		ifs >> size; b.resize( size );

		REP( i, a.size( ) )
		{
			ifs >> hour;
			a[ i ].start = toMinutes( hour );
			ifs >> hour;
			a[ i ].end = toMinutes( hour );
		}

		sort( a.begin( ), a.end( ), greater_trip );

		REP( i, b.size( ) )
		{
			ifs >> hour;
			b[ i ].start = toMinutes( hour );
			ifs >> hour;
			b[ i ].end = toMinutes( hour );
		}

		sort( b.begin( ), b.end( ), greater_trip );

		int sz = a.size( ) + b.size( );

		REP( i, sz )
		{
			trip t;
			bool from_a = false;

			if( !a.empty( ) && !b.empty( ) && greater_trip( a[ a.size( ) - 1 ], b[ b.size( ) - 1 ] ) )
			{
				t = b[ b.size( ) - 1 ];
				b.pop_back( );
				from_a = false;
			}
			else if( !b.empty( ) && !a.empty( ) )
			{
				t = a[ a.size( ) - 1 ];
				a.pop_back( );
				from_a = true;
			}
			else if( a.empty( ) )
			{
				t = b[ b.size( ) - 1 ];
				b.pop_back( );
				from_a = false;
			}
			else if( b.empty( ) )
			{
				t = a[ a.size( ) - 1 ];
				a.pop_back( );
				from_a = true;
			}


			if( from_a )
			{
				if( ! onA.empty( ) && onA[ onA.size( ) - 1 ] <= t.start )
				{
					onA.pop_back( );
					onB.push_back( t.end + TurnAround );
					sort( onB.begin( ), onB.end( ), greater<int>( ) );
				}
				else
				{
					++a_trains;
					onB.push_back( t.end + TurnAround );
					sort( onB.begin( ), onB.end( ), greater<int>( ) );

				}
			}
			else
			{
				if( ! onB.empty( ) && onB[ onB.size( ) - 1 ] <= t.start )
				{
					onB.pop_back( );
					onA.push_back( t.end + TurnAround );
					sort( onA.begin( ), onA.end( ), greater<int>( ) );
				}
				else
				{
					++b_trains;
					onA.push_back( t.end + TurnAround );
					sort( onA.begin( ), onA.end( ), greater<int>( ) );
				}
			}

		}

		ofs << "Case #" << k <<": " << a_trains <<" " << b_trains <<endl;

	}

		ifs.close( );
		ofs.close( );

}

int toMinutes( string time )
{
	int minutes = 0;

	FOR( i, 0, 2 )
	{
		minutes += ( time[ i ] - 48 ) * 60 * pow( 10.0, (double) 1 - i );
	}

	FOR( i, 3, 5 )
	{
		minutes += ( time[ i ] - 48 )* pow( 10.0, (double) 4 - i );
	}

	return minutes;
}

bool greater_trip( trip a, trip b )
{
	return a.start > b.start;
}