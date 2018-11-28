////////////////////////////////////////////////////////////////////////////////
//
// Google Codejam '2009
// Qualificatino Round - B. 
//
// Author : Kang, Jin-Kook, 2009.09.03
//
// * 
//

#include <stdio.h>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <list>
#include <queue>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

////////////////////////////////////////////////////////////////////////////////
//
/*
Input 
   
5
3 3
9 6 3
5 9 6
3 5 9
1 10
0 1 2 3 4 5 6 7 8 7
2 3
7 6 7
7 6 7
5 5
1 2 3 4 5
2 9 3 9 6
3 3 0 8 7
4 9 8 9 8
5 6 7 8 9
2 13
8 8 8 8 8 8 8 8 8 8 8 8 8
8 8 8 8 8 8 8 8 8 8 8 8 8 

*/

//#include <iostream>
//#include <sstream>
//#include <fstream>
//ifstream fin("input.txt");
//#define cin fin

#define MAX_HEIGHT		100
#define MAX_WIDTH		100
#define DIR_COUNT		4

// North, West, East, South
const int searchOrderRow[ DIR_COUNT ] = { -1, 0, 0, 1 };
const int searchOrderCol[ DIR_COUNT ] = { 0, -1, 1, 0 };

struct Cell
{
	Cell() : alt_( -1 ), id_( -1 ), linked_( 0 ) { }

	void link( Cell* cell )
	{
		if ( cell == this ) return;
		if ( linked_ ) linked_->link( cell );
		else linked_ = cell;
	}

	int getID()
	{
		return ( linked_ ) ? linked_->getID() : id_;
	}

	int		alt_;
	int		id_;
	Cell*	linked_;
};

typedef Cell MapInfo[ MAX_HEIGHT ][ MAX_WIDTH ];

void findDrainageBasins( const int h, const int w, MapInfo& source )
{
	for ( int row = 0; row < h; ++row ) {
		for ( int col = 0; col < w; ++col ) {
			Cell* curCell = &source[ row ][ col ];
			Cell* minCell = 0;
			int minAlt = curCell->alt_, minDir = -1;

			for ( int dir = 0; dir < DIR_COUNT; ++dir ) {
				int targetRow = row + searchOrderRow[ dir ];
				int targetCol = col + searchOrderCol[ dir ];
				if ( targetRow < 0 || targetRow >= h
					|| targetCol < 0 || targetCol >= w )
					continue;

				Cell* cell = &source[ targetRow ][ targetCol ];
				int targetAlt = cell->alt_;
				if ( targetAlt < minAlt ) {
					minAlt = targetAlt;
					minDir = dir;
					minCell = cell;
				}
			}

			if ( minCell ) {
				if ( minDir < 2 ) {			// North, West (Higher priority)
					curCell->link( minCell );
				}
				else {						// South, East (Lower priority)
					minCell->link( curCell );
				}
			}
		}
	}
}

int main( int argc, char *argv[] )
{
	int count;
	cin >> count;

	for ( int i = 1; i <= count; ++i ) {
		int h, w;
		cin >> h >> w;

		// load map
		MapInfo source;
		int alt, id = 0;
		for ( int row = 0; row < h; ++row ) {
			for ( int col = 0; col < w; ++col ) {
				cin >> alt;
				source[ row ][ col ].alt_ = alt;
				source[ row ][ col ].id_ = id++;
			}
		}

		/*
		for ( int row = 0; row < h; ++row ) {
			for ( int col = 0; col < w; ++col ) {
				printf( "%d(%d)  ", source[ row ][ col ].alt_, source[ row ][ col ].id_.val_ );
			}
			printf( "\n" );
		}
		*/

		MapInfo result;
		findDrainageBasins( h, w, source );

		cout << "Case #" << i << ":" << endl;

		map< int, char > basinsMap;
		char basinAllocator = 'a';
		for ( int row = 0; row < h; ++row ) {
			for ( int col = 0; col < w; ++col ) {
				int id = source[ row ][ col ].getID();
				char basin = 0;
				if ( basinsMap.find( id ) != basinsMap.end() ) {
					basin = basinsMap[ id ];
				}
				else {
					basin = basinAllocator++;
					basinsMap[ id ] = basin;
				}

				if ( col > 0 ) cout << ' ';
				cout << basin;
			}
			cout << endl;
		}
	}

	return 0;
}
