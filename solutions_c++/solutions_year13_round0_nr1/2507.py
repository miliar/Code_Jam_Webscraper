#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <string>

using namespace std;

//#define DEV 1

pair< char, int > check( string s[], int x, int y, int i, int j ) {

	if( s[x][y] == '.' )
		return make_pair( 'A', 0 );

	if( (x == 3 && i == 1) || (y == 3 && j == 1) || (x == 0 && i == -1) || (y == 0 && j == -1) ) {
		if( s[x][y] == 'T' )
			return make_pair( s[ x ][ y ], 1 );
		else
			return make_pair( s[ x ][ y ], 0 );
	}
	
	pair< char, int > temp = check( s, x+i, y+j, i, j );
	if( temp.first == 'A' )
		return make_pair( 'A', 0 );

	if( ( s[ x ][ y ] == temp.first && temp.first != 'T' ) || ( s[ x ][ y ] == 'T' && temp.second == 0 ) || ( temp.first == 'T' && s[ x ][ y ] != 'T' ) ) {
		if( s[ x ][ y ] == 'T' )
			return make_pair( s[ x ][ y ], 1 );
		else
			return make_pair( s[ x ][ y ], temp.second );
	} else {
		return make_pair( 'A' , 0 );
	}
}

int main() {
	#ifndef DEV
		freopen( "A-small-attempt0.in", "r", stdin );
		freopen( "A-small-attempt0.out", "w+", stdout );
	#endif

	int n;
	cin>>n;
	
	for( int i = 0; i < n; ++i ) {
		string s[ 4 ];
		bool dot = false;

		cin>> s[ 0 ] >> s[ 1 ] >> s[ 2 ] >> s[ 3 ];

		for( int j = 0; j < 4; ++j )
			if( count( s[j].begin(), s[j].end(), '.' ) > 0 )
				dot = true;

		char w = 'A';
		for( int j = 0; j < 4; ++j ) {
			pair< char, int > temp = check( s, j, 0, 0, 1 );
			if( temp.first != 'A' ) {
				w = temp.first;
				break;
			}
		}

		for( int j = 0; j < 4; ++j ) {
			pair< char, int > temp = check( s, 0, j, 1, 0 );
			if( temp.first != 'A' ) {
				w = temp.first;
				break;
			}
		}

		pair< char, int > temp = check( s, 0, 0, 1, 1 );
		if( temp.first != 'A' ) {
			w = temp.first;
		}

		temp = check( s, 0, 3, 1, -1 );
		if( temp.first != 'A' ) {
			w = temp.first;
		}

		cout<< "Case #" << i+1 <<": ";
		if( w == 'A' ) {
			if( dot )
				cout<<"Game has not completed";
			else
				cout<<"Draw";
		} else {
			cout<<w<<" won";
		}

		cout<<endl;
	}

	#ifdef DEV
		system( "PAUSE" );
	#endif
	return 0;
}
