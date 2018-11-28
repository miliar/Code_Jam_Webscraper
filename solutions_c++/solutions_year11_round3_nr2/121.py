#include <algorithm>
#include <iostream>
#include <cassert>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <map>

using namespace std;

const int MAXN = 2000000;

typedef long long ll;

ll a[ MAXN ];
ll dist[ MAXN ];
ll reach[ MAXN ];
ll win[ MAXN ];



void solve ()
{
	int L, N, C;
	ll t;
	cin >> L >> t >> N >> C;
	//t *= 2LL;
	int i, j;
	for( i = 0; i < C; ++i )
		cin >> dist[ i ];
	for( i = C; i < N; ++i )
		dist[ i ] = dist[ i - C ];

	reach[ 0 ] = 0;
	ll ans = 0;
	for( i = 1; i <= N; ++i )
		reach[ i ] = reach[ i - 1 ] + dist[ i - 1 ] * 2LL;

	ans = reach[ N ];

	for( i = 0; i < N; ++i )
		if( reach[ i ] > t )
			break;
	--i;
	int lt = i;
	win[ i ] = dist[ i ] - ( t - reach[ i ] ) / 2;
	for( ++i; i < N; ++i )
		win[ i ] = dist[ i ];
	sort( win + lt, win + N );
	ll sum = 0;
	for( i = 0; i < L && N - i - 1 >= lt; ++i )
		sum += win[ N - i - 1 ];
	ans -= sum;
	cout << ans << endl;
	

	
}


int main ()
{
	freopen( "B-large.in", "r", stdin );
	freopen( "B-large.out", "w", stdout );
	int i, T;
	cin >> T;
	for( i = 1; i <= T; ++i )
	{
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}