//============================================================================
// Name        : GCJ_10_R1C_A.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
using namespace std;

int w, h;
const int maxw = 512;
const int maxh = 512;

bool board[ maxw ][ maxh ];
bool cutout[ maxw ][ maxh ];

int char2int( char a ) {
	if( a >= '0' && a <= '9' ) {
		return a-'0';
	}
	if( a >= 'A' && a <= 'F' ) {
		return a+10-'A';
	}
	if( a >= 'a' && a <= 'f' ) {
		return a+10-'a';
	}
	cout << "!!!!";
	throw;
}

bool test_( int x, int y, int r ) {
	bool color = board[x][y];

	for( int i=0; i<r; i++ )  {
		for( int j=0; j<r; j++ ) {
			if( ( board[x+i][y+j] != color ) || cutout[x+i][y+j] ) {
				return false;
			}
		}
	}
	for( int i=0; i<r; i++ )  {
		for( int j=0; j<r; j++ ) {
			cutout[x+i][y+j] = true;
		}
	}

	//cout << "Found! " << r << " " << x << " " << y << "\n";
	return true;
}

bool test( int r ) {
	for( int y=0; y<=h-r; y++ ) {
		for( int x=0; x<=w-r; x++ ) {
			if( test_( x, y, r ) ) {
				return true;
			}
		}
	}
	return false;
}

int main() {
	long casecount;

	ifstream in( "C-small-attempt0.in" );
	ofstream out( "out.txt" );

	in >> casecount;

	for( long c=1; c <= casecount; c++) {
		in >> h >> w;
		//cout << h << " " << w;
		for( int i=0; i<h; i++ ) {
			for( int j=0; j<w/4; j++ ) {
				char foo;
				in >> foo;
				int bar = char2int( foo );
				//cout << bar << " ";
				board[j*4][i] = bar&8;
				board[j*4+1][i] = bar&4;
				board[j*4+2][i] = bar&2;
				board[j*4+3][i] = bar&1;
			}
			//cout << "\n";
		}

		for( int i=0; i<h; i++ ) {
			for( int j=0; j<w; j++ ) {
				cutout[j][i] = false;
				if( i&1 == 1 )
					board[j][i] = !board[j][i];
				if( j&1 == 1 )
					board[j][i] = !board[j][i];
			}
		}

		/*for( int i=0; i<h; i++ ) {
			for( int j=0; j<w; j++ ) {
				cout << (board[j][i] ? "T" : "F");
			}
			cout << "\n";
		}*/
		int foo = min(w,h);
		int sizes[foo];
		for( int i=0;i<foo; i++ )
			sizes[i] = 0;

		for( int i=foo-1; i >= 1; i-- ) {
			//cout << (i+1) << "\n";
			while( test( i+1 ) )
				sizes[i]++;
		}
		for( int i=0; i<h; i++ ) {
			for( int j=0; j<w; j++ ) {
				if( !cutout[j][i] )
					sizes[0]++;
			}
		}

		int taika=0;
		for( int i=0;i<foo; i++ ) {
			if( sizes[i] != 0 )
				taika++;
		}
		out << "Case #" << c << ": " << taika << "\n";
		for( int i=foo-1;i>=0; i-- ) {
			if( sizes[i] != 0 ) {
				out << (i+1) << " " << sizes[i] << "\n";
			}
		}
	}
}
