
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
#include <cassert>
using namespace std;

#define FOR( i, a, b ) for( int i = a; i < b; ++i )
#define REP( i, n ) FOR( i, 0, n )
#define LOOP( i ) for( int i = 0;; ++i )
#define FORE(it, x ) for( typeof( x.begin( ) ) it; it != x.end( ); ++it )
#define MIN( a, b ) ( a < b ) ? a : b
#define MAX( a, b ) ( a > b ) ? a : b


int main(int argc, char* argv[ ] )
{

	ifstream ifs;
	ofstream ofs;
	int N = 0;

	ifs.open("A-large.in" );
	ofs.open("A-large.out" );

	ifs >> N;

	FOR( ca, 1, N + 1 )
	{
		int P = 0, K = 0, L = 0;

		ifs >> P >> K >> L;

		vector< int > alpha( L );

		REP( i, L )
		{
			ifs >> alpha[ i ];
		}

		sort( alpha.begin( ), alpha.end( ), greater< int >( ) );

		long long counter = 0;

		vector<int>::iterator it = alpha.begin( );

		bool flag = false;

		FOR( i, 1, P + 1 )
		{
			REP( j, K )
			{
				counter += (*it)*i;
				++it;

				if( it == alpha.end( ) ) 
				{
					flag = true;
					break;
				}
			}

			if( flag ) break;
		}

		ofs << "Case #" << ca << ": " << counter << endl;

	}

	return 0;
}

