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

string current_engine;

string init_engine( map<string, vector< int > > mp );
bool switch_engine( vector<string> qs, int index , map< string, vector<int> > mp );

int main(int argc, char* argv[] )
{
	ifstream ifs;
	ofstream ofs;
	int n = 0;
	char t[ 110 ] = { 0 };

	ifs.open( "A-small1.in" );
	ofs.open( "A-small.out" );

	ifs >> n;

	FOR( k, 1, n + 1 )
	{
		map<string, vector< int > > mp;
		vector<string> engines;
		vector<string> queries;
		int nEngines = 0;
		int nQs = 0;
		int count = 0;

		ifs >> nEngines;
		ifs.getline( t, 110 );

		REP( i, nEngines )
		{
			ifs.getline(t, 110 );
			engines.push_back( t );
			mp[ t ].resize( 0 );
			
		}

		ifs >> nQs;
		ifs.getline( t, 110 );

		REP( i, nQs )
		{
			ifs.getline( t, 110 );
			queries.push_back( t );
			mp[ t ].push_back( i );
		}

		current_engine = init_engine( mp );
		
		REP( i, nQs )
		{
			if( switch_engine( queries, i, mp ) ) ++count;
		}
	
		ofs << "Case #" << k << ": " << count << endl;


	}

	ifs.close( );
	ofs.close( );
	return 0;
}

string init_engine( map<string, vector<int> > mp )
{
	int max = 0;
	string result;

	for( map<string, vector<int> >::iterator it = mp.begin( ); it != mp.end( ); ++it )
	{
		if( (*it).second.empty( ) ) return (*it).first;

		int inner_min = 101;
		REP( i, (*it).second.size( ) )
		{
			inner_min = MIN( inner_min, it->second[ i ] );
		}

		if( max < inner_min )
		{
			max = inner_min;
			result = (*it).first;
		}
	}

	return result;
}

bool switch_engine( vector<string> qs, int index , map< string, vector<int> > mp )
{
	int max = 0;
	int min = 101;

	bool flag_positive = false;
	string old_engine = current_engine;

	if( qs[ index ] != current_engine ) return false;

	for( map<string, vector<int> >::iterator it = mp.begin( ); it != mp.end( ); ++it )
	{
		flag_positive = false;
		min = 101;

		if( old_engine == (*it).first ) continue;

		if( (*it).second.empty( ) )
		{
			current_engine = (*it).first;
			return true;
		}
		else
		{
			REP( i, (*it).second.size( ) )
			{
				if( (*it).second[ i ] - index >= 0 ) flag_positive = true;

				if( (*it).second[ i ] - index > 0 )
				{
					min = MIN( min, (*it).second[ i ] - index );
				}
			}

			if( max < min )
			{
				max = min;
				current_engine = (*it).first;
			}

			if( ! flag_positive )
			{
				current_engine = (*it).first;
				return true;
			}
		}
	}

	return true;
}