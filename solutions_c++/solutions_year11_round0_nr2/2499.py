#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <string>
#include <map>
#include <algorithm>
using namespace std;


int main( )
{
	freopen( "input.txt", "rt", stdin );
	freopen( "output.txt", "wt", stdout );	

	int T = 0;
	cin >> T;

	for( int ct = 0; ct < T; ++ct )
	{
		vector< string > combines;
		vector< string > clears;
		int C = 0;

		cin >> C;

		for( int i = 0; i < C; ++i )
		{
			string t;
			cin >> t;
			combines.push_back( t );
		}

		int D = 0;
		cin >> D;

		for( int i = 0; i < D; ++i )
		{
			string t;
			cin >> t;
			clears.push_back( t );
		}

		int N = 0;
		cin >> N;

		string invokes;
		cin >> invokes;

		map< char, int > used;
		vector< char > result;

		for( int i = 0; i < N; ++i )
		{
			result.push_back( invokes[ i ] );
			++used[ invokes[ i ] ];

			bool bCombined = false;

			if( result.size( ) > 1 )
			{
				char elem1 = result[ result.size( ) -1 ];
				char elem2 = result[ result.size( ) - 2 ];
				for( int j = 0; j < combines.size( ); ++j )
				{
					if( ( elem1 == combines[ j ][ 0 ] && elem2 == combines[ j ][ 1 ] ) ||
						( elem2 == combines[ j ][ 0 ] && elem1 == combines[ j ][ 1 ] ) )
					{
						result.pop_back( );
						result.pop_back( );
						--used[ elem1 ];
						--used[ elem2 ];
						result.push_back( combines[ j ][ 2 ] );
						++used[ combines[ j ][ 2 ] ];
						bCombined = true;
						break;
					}
				}

				if( ! bCombined )
				{
					for ( int j = 0; j < clears.size( ); ++j )
					{
						if( used[ clears[ j ][ 0 ]  ] > 0 && 
							used[ clears[ j ][ 1 ] ] > 0 )
						{
							result.clear( );
							used.clear( );
							break;
						}
					}
				}
			}
		}

		cout << "Case #" << ct + 1 << ": " << "[";

		for( int i = 0; i < (int)result.size( ) - 1; ++i )
		{
			cout << result[ i ] << ", ";
		}

		if( result.size( ) > 0 )
		{
			cout << result[ result.size( ) - 1 ];
		}

		cout << "]" << endl;
	}
}