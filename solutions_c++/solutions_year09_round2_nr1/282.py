#include <cstdio>
#include <cstdlib>
#include <set>
#include <vector>
#include <iostream>
#include <string>

using namespace std;
vector< string > vecs;
set< string > seth[ 105 ];
string st, acc, name[ 105 ];

int t, n, an, ac[ 105 ], poz;

string formatst( string a ) {
	string tr = "";
	int len = ( int )a.size();
	
	for( int i = 0; i < len; ++i ) {
		if( a[ i ] == '('  ||  a[ i ] == ')' ) tr += ' ';
		tr += a[ i ];
		if( a[ i ] == '('  ||  a[ i ] == ')' ) tr += ' ';
	}
	
	return( tr );
}

void extrst( string a ) {
	vecs.clear();
	
	int pozs, len = ( int )a.size();
	for( int i = 0; i < len; ++i ) {
		if( a[ i ] == ' ' ) continue;
		
		for( pozs = i; a[ i ] != ' '; ++i );
		vecs.push_back( a.substr( pozs, i - pozs ) );
	}
}

void solve( int uzima, int ind, double chance ) {
	double tr = 0;
	sscanf( vecs[ ++poz ].c_str(), "%lf", &tr );
	chance *= tr;
	
	if( vecs[ ++poz ] == ")" ) {
		if( uzima ) printf( "%.7lf\n", chance );
		return;
	}
	
	int prvi = ( seth[ ind ].find( vecs[ poz ] ) != seth[ ind ].end() );
	
	++poz;
	solve( uzima &  prvi, ind, chance ); ++poz;
	solve( uzima & !prvi, ind, chance ); ++poz;
}

int main( void ) {
	scanf( "%d", &t );
	for( int i = 0; i < t; ++i ) {
		scanf( "%d\n", &n ); acc = "";
		for( int j = 0; j < n; ++j ) {
			getline( cin, st );
			acc += ( " " + st );
		}
		
		extrst( formatst( acc ) );
		
		scanf( "%d", &an );
		for( int j = 0; j < an; ++j ) {
			seth[ j ].clear();
			cin >> name[ j ];
			
			scanf( "%d", &ac[ j ] );
			for( int k = 0; k < ac[ j ]; ++k ) {
				cin >> st; seth[ j ].insert( st );
			}
			
		}
		
		printf( "Case #%d:\n", i + 1 );
		for( int j = 0; j < an; ++j ) {
			poz = 0; solve( 1, j, 1.0 );
		}
	}
	return( 0 );
}
