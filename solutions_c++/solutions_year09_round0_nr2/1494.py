#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <queue>
using namespace std;

int attitude[ 101 ][ 101 ];
bool used[ 101 ][ 101 ];
char basins[ 101 ][ 101 ];

int moves[ 4 ][ 2 ] = { { -1, 0 }, { 0, -1 }, { 0, 1 }, { 1, 0 } };

int H, W;

bool valid( int r, int c )
{
	if( r < 0 || r >= H || c <0 || c >= W ) return false;
	return true;

}

bool HasTheSameBasin( pair<int,int> pa, pair<int,int> pb )
{
	if( attitude[ pa.first ][ pa.second ] < attitude[ pb.first ][ pb.second ] )
	{
		int lowestAttitude = attitude[ pb.first ][ pb.second ];
		int lowestIdx = -1;

		for( int i = 0; i < 4; ++i )
		{
			if( valid( pb.first + moves[ i ][ 0 ], pb.second + moves[ i ][ 1 ] ) )
			{
				if( attitude[ pb.first + moves[ i ][ 0 ]][ pb.second + moves[ i ][ 1 ] ] < lowestAttitude )
				{
					lowestIdx = i;
					lowestAttitude = attitude[ pb.first + moves[ i ][ 0 ]][ pb.second + moves[ i ][ 1 ] ];
				}
				//if( attitude[ pb.first + moves[ i ][ 0 ] ][ pb.second + moves[ i ][ 1 ] ] <
				//	attitude[ pb.first ][ pb.second ] )
				//{
				//	if( pa.first == pb.first + moves[ i ][ 0 ] && pa.second == pb.second + moves[ i ][1 ] )
				//	{
				//		return true;
				//	}
				//	else
				//	{
				//		return false;
				//	}
				//}
			}
		}

		if( lowestIdx == -1 ) return false;

		if( pa.first == pb.first + moves[ lowestIdx ][ 0 ] && pa.second == pb.second + moves[ lowestIdx ][ 1 ] )
		{
			return true;
		}
	}
	else if ( attitude[ pb.first ][ pb.second ] < attitude[ pa.first ][ pa.second ] )
	{
		int lowestAttitude = attitude[ pa.first ][ pa.second ];
		int lowestIdx = -1;

		for( int i = 0; i < 4; ++i )
		{
			if( valid( pa.first + moves[ i ][ 0 ], pa.second + moves[ i ][ 1 ] ) )
			{				
				if( attitude[ pa.first + moves[ i ][ 0 ] ][ pa.second + moves[ i ][ 1 ] ] < lowestAttitude )
				{
					lowestIdx = i;
					lowestAttitude = attitude[ pa.first + moves[ i ][ 0 ] ][ pa.second + moves[ i ][ 1 ] ];
				}
				
				//if( attitude[ pa.first + moves[ i ][ 0 ] ][ pa.second + moves[ i ][ 1 ] ] <
				//	attitude[ pa.first ][ pa.second ] )
				//{
				//	if( pb.first == pa.first + moves[ i ][ 0 ] && pb.second == pa.second + moves[ i ][1 ] )
				//	{
				//		return true;
				//	}
				//	else
				//	{
				//		return false;
				//	}
				//}
			}
		}

		if( lowestIdx == -1 ) return false;

		if( pb.first == pa.first + moves[ lowestIdx ][ 0 ] && pb.second == pa.second + moves[ lowestIdx ][ 1 ] )
		{
			return true;
		}

	}

	return false;
}

int main( )
{
	freopen( "input.txt", "rt", stdin );
	freopen( "output.out", "wt", stdout );

	int T = 0;

	cin >> T;

	for( int ct = 1; ct <= T; ++ct )
	{
		memset( attitude, -1, sizeof( attitude ) );
		memset( used, false, sizeof( used ) );
		memset( basins, -1, sizeof( basins ) );
	
		cin >> H >> W;

		int cellsCount = H*W;

		set< pair<int,int > > sortedCells;

		for( int i = 0; i < H; ++i )
		{
			for( int j = 0; j < W; ++j )
			{
				cin >> attitude[ i ][ j ];
				sortedCells.insert( make_pair( i, j ) );
			}
		}

		char basin = 'a';

		while( cellsCount > 0 )
		{
			//find start pair
			pair<int,int> start = make_pair( -1, -1 );

			for( set< pair<int,int > >::iterator  hui = sortedCells.begin( );
				 hui != sortedCells.end( ); ++hui )
			{
				if( ! used[ hui->first ][ hui->second ] )
				{
					start = make_pair( hui->first , hui->second );

					break;

					//obey your master!
				}
			}

			queue<pair<int,int> > Q;

			Q.push( start );
			basins[ start.first ][ start.second ] = basin;
			used[ start.first ][ start.second ] = true;
			cellsCount--;

			while( ! Q.empty( ) )
			{
				pair<int,int> cur = Q.front( );
				Q.pop( );

				for( int i = 0; i < 4; ++i )
				{
					pair<int,int> pelem = make_pair( cur.first + moves[ i ][ 0 ], cur.second + moves[ i ][ 1 ] );

					if( valid( pelem.first, pelem.second ) &&
						! used[ pelem.first ][ pelem.second ] &&
						HasTheSameBasin( cur, pelem ) )
					{
						Q.push( pelem );
						basins[ pelem.first ][ pelem.second ] = basin;
						used[ pelem.first ][ pelem.second ] = true;
						cellsCount--;
					}										   	
				}
			}

			++basin;
		}

		cout << "Case #" << ct << ": " << endl;

		for( int i = 0; i < H; ++i )
		{
			cout << basins[ i ][ 0 ];

			for( int j = 1; j < W; ++j )
			{
				cout << " " << basins[ i ][ j ];
			}

			cout << endl;
		}
	}
}