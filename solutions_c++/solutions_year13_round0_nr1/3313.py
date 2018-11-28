#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cfloat>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <numeric>
#include <iterator>

using namespace std;

typedef unsigned int UI;
typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;
typedef istringstream ISS;
typedef ostringstream OSS;

#define REP( i, m, n ) for ( int i = (int)( m ); i < (int)( n ); ++i )
#define FOR( v, c ) for ( auto &v : c )

#define EACH( it, c ) for ( auto it = c.begin(); it != c.end(); ++it )
#define ALL( c ) (c).begin(), (c).end()

#define PB( n ) push_back( n )
#define MP( a, b ) make_pair( ( a ), ( b ) )
#define EXIST( c, e ) ( (c).find( e ) != (c).end() )

#define fst first
#define snd second

#define DUMP( x ) cerr << #x << " = " << ( x ) << endl
#define DEBUG( x ) cerr << __FILE__ << ":" << __LINE__ << ": " << #x << " = " << ( x ) << endl

bool win( const VS &board, char p )
{
	// horizontal
	FOR( line, board )
	{
		int tmp = 0;
		FOR( c, line )
		{
			if ( c == p )
			{
				tmp += 2;
			}
			if ( c == 'T' )
			{
				tmp += 1;
			}
		}
		if ( 7 <= tmp )
		{
			return true;
		}
	}

	// vertical
	REP( ix, 0, 4 )
	{
		int tmp = 0;
		REP( iy, 0, 4 )
		{
			if ( board[ iy ][ ix ] == p )
			{
				tmp += 2;
			}
			if ( board[ iy ][ ix ] == 'T' )
			{
				tmp += 1;
			}
		}
		if ( 7 <= tmp )
		{
			return true;
		}
	}

	{ // right down
		int tmp = 0;
		REP( i, 0, 4 )
		{
			if ( board[i][i] == p )
			{
				tmp += 2;
			}
			if ( board[i][i] == 'T' )
			{
				tmp += 1;
			}
		}
		if ( 7 <= tmp )
		{
			return true;
		}
	}

	{ // right up
		int tmp = 0;
		REP( i, 0, 4 )
		{
			if ( board[ 3 - i ][i] == p )
			{
				tmp += 2;
			}
			if ( board[ 3 - i ][i] == 'T' )
			{
				tmp += 1;
			}
		}
		if ( 7 <= tmp )
		{
			return true;
		}
	}

	return false;
}
			
string solve()
{
	VS board( 4 );
	FOR( line, board )
	{
		cin >> line;
	}

	if ( win( board, 'X' ) )
	{
		return "X won";
	}
	if ( win( board, 'O' ) )
	{
		return "O won";
	}

	int cnt = 0;
	FOR( line, board )
	{
		cnt += count( ALL( line ), '.' );
	}
	return cnt == 0 ? "Draw" : "Game has not completed";
}

int main()
{
	cin.tie( 0 );
	ios::sync_with_stdio( false );

	int t;
	cin >> t;
	REP( ti, 0, t )
	{
		cout << "Case #" << ti + 1 << ": " << solve() << endl;
	}

	return 0;
}
