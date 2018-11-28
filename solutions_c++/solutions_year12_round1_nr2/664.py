#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <cmath>
#include <set>
#include <map>

using namespace std;

#define FOR( i, a, b ) for( i = a; i < b; ++i )
#define FORN( i, a, b ) for( i = a; i <= b; ++i )

#define sint(x) scanf( "%d", &x )
#define sdouble(x) scanf( "%lf", &x )
#define sint64(x) scanf( "%I64d", &x )
#define pint(x) printf(  "%d ", x )
#define pintn(x) printf( "%d\n", x )

typedef long long ll;
typedef unsigned long long ull;

const int maxn = 2050;

int a[ maxn ];
int b[ maxn ];
bool ua[ maxn ];
bool ub[ maxn ];

void solve()
{
	int i, n;
	cin >> n;
	FOR( i, 0, n )
		cin >> a[ i ] >> b[ i ];
	memset( ua, 0, sizeof( ua ));
	memset( ub, 0, sizeof( ub ));
	int completed = 0;
	int raced = 0;
	int stars = 0;
	while( completed < n )
	{
		FOR( i, 0, n )
		if( stars >= b[ i ] && !ub[ i ] )
		{
			if( ua[ i ] )
				++stars;
			else
				stars += 2;
			ub[ i ] = 1;
			completed++;
			raced++;
			break;
		}
		if( i == n )
		{
			int mxv = -1;
			int mxi;
			FOR( i, 0, n )
				if( stars >= a[ i ] && !ua[ i ] && !ub[ i ] && b[ i ] > mxv )
				{
					mxv = b[ i ];
					mxi = i;
				}
			if( mxv == -1 )
			{
				cout << "Too Bad";
				return;
			}
			++stars;
			raced++;
			ua[ mxi ] = 1;
		}
	}
	cout << raced;
}

int main()
{
	freopen( "B-large.in", "r", stdin );
	freopen( "B-large.out", "w", stdout );
	int t;
	cin >> t;
	for( int i = 1; i <= t; ++i )
	{
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	return 0;
}

