#include <stdio.h>
#include <iostream>
#include <string>
#include <map>
#include <list>

using namespace std;

////////////////////////////////////////////////////////////////////////////////////
//

#define MAX_S		100
#define INFINITE	100000000

int getMinSwitch( const int& s, const int& q, list< char >& queries )
{
	// dynamic programming
	int tab0[ MAX_S ], tab1[ MAX_S ];
	int *oldtab = tab0, *newtab = tab1, *tmp;
	int val;
	char query;

	if ( q == 0 ) return 0;

	query = queries.front();
	queries.pop_front();
	for ( int i = 0; i < s; ++i ) {
		oldtab[ i ] = ( query == i ) ? INFINITE : 0;
	}

	for ( int i, j, k = 1; k < q; ++k ) {
		query = queries.front();
		queries.pop_front();

		for ( i = 0; i < s; ++i ) {
			if ( query == i ) {
				newtab[ i ] = INFINITE;
				continue;
			}

			val = INFINITE;
			for ( j = 0; j < s; ++j ) {
				if ( i == j ) {
					if ( oldtab[ j ] < val ) val = oldtab[ j ];
				}
				else {
					if ( oldtab[ j ] + 1 < val ) val = oldtab[ j ] + 1;
				}
			}
			newtab[ i ] = val;
		}

		tmp = newtab;
		newtab = oldtab;
		oldtab = tmp;
	}

	val = INFINITE;
	for ( int i = 0; i < s; ++i ) {
		if ( oldtab[ i ] < val ) val = oldtab[ i ];
	}

	return val;
}

int _getMinSwitch( const int& s, const int& q, list< char >& queries )
{
	// greedy algorithm
	char tab[ MAX_S ], query;
	int count = 0, used = 0;

	if ( q == 0 ) return 0;

	query = queries.front();
	queries.pop_front();
	for ( int i = 0; i < s; ++i ) tab[ i ] = 0;

	for ( int i = 1; i < q; ++i ) {
		query = queries.front();
		queries.pop_front();

		if ( tab[ query ] ) continue;

		tab[ query ] = 1;
		used++;

		if ( used == s ) {
			count++;
			for ( int j = 0; j < s; ++j ) tab[ j ] = 0;
			used = 1;
			tab[ query ] = 1;
		}
	}

	return count;
}

int main( int argc, char *argv[] )
{
	char buf[ 101 ];

	int count;
	gets_s( buf, 100 );
	count = atoi( buf );

	for ( int i = 1; i <= count; ++i ) {
		map< string, char >	searchEngines;
		list< char > queries;
		int s, q;

		gets_s( buf, 100 );
		s = atoi( buf );

		for ( char j = 0; j < s; ++j ) {
			gets_s( buf, 100 );
			searchEngines[ buf ] = j;
		}

		gets_s( buf, 100 );
		q = atoi( buf );

		for ( int j = 0; j < q; ++j ) {
			gets_s( buf, 100 );
			queries.push_back( searchEngines[ buf ] );
		}

		int switchCount = getMinSwitch( s, q, queries );
		printf( "Case #%d: %d\n", i, switchCount );
	}

	return 0;
}
