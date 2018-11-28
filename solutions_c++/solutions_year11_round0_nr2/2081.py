#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <fstream>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> PI;
typedef vector<PI> VPI;
typedef unsigned long long ull;
typedef long long ll;

#define FOR(i, n) for(int i=0;i<(n);++i)
#define REP(i,s,n) for(int i=s;i<=n;++i)
#define SZ(x) ((int)(x).size())
#define LOOP(i,x) FOR(i,SZ(x))
#define IT(it,x) for(typeof((x).begin()) it = (x).begin();it!=(x).end();++it)
#define ALL(x) (x).begin(), (x).end()
#define ST first
#define ND second
#define MP make_pair
#define PB push_back

int case_number;
#define printg case_number++, printf("Case #%d: ",case_number), printf
#define gout case_number++, printf("Case #%d: ",case_number), cout

#define INF (1<<29)

void main2( void )
{
	int C, D, N;
	string ip = "";
	cin >> C;
	VS cb, cd;
	if( C > 0 ) FOR( i, C )
	{
		cin >> ip;
		cb.PB( ip );
		swap( ip[ 0 ], ip[ 1 ] );
		cb.PB( ip );
	}

	cin >> D;
	if( D > 0 ) FOR( i, D )
	{
		cin >> ip;
		cd.PB( ip );
		swap( ip[ 0 ], ip[ 1 ] );
		cd.PB( ip );
	}

	cin >> N >> ip;
	vector<char> s;
	FOR( i, N )
	{
		char c1, c2;
		if( !SZ( s ) )
		{
			s.PB( ip[ i ] );
			continue;
		}

		c1 = s[ SZ( s ) - 1 ]; c2 = ip[ i ];
		bool f = false;
		FOR( j, SZ( cb ) )
		{
			if( cb[ j ][ 0 ] == c1 && cb[ j ][ 1 ] == c2 )
			{
				s.pop_back();
				s.PB( cb[ j ][ 2 ] );
				f = true;
				break;
			}
		}
		if( !f ) s.PB( c2 );
		else continue;

		FOR( j, SZ( cd ) )
		{
			if( cd[ j ][ 0 ] == c2 )
			{
				bool f = true;
				c1 = cd[ j ][ 1 ];
				FOR( k, SZ( s ) )
				{
					if( s[ k ] == c1 )
					{
						f = false;
						while( SZ( s ) ) s.pop_back();
					}
				}
				if( !f ) break;
			}
		}
	}
	gout << "[";
	FOR( i, SZ( s ) - 1 ) cout << s[ i ] << ", ";
	if( SZ( s ) > 0 ) cout << s[ SZ( s ) - 1 ];
	cout << "]" << endl;
}

int main()
{
	freopen( "B-large.in", "r", stdin );
	freopen( "B-large.out", "w", stdout );
	int T;
	scanf( "%d", &T );
	FOR( i, T ) main2();
	return 0;
}
