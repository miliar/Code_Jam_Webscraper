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

const int MAXN = 150;

int a[ MAXN ];


void solve ()
{
	int N, L, H;
	int i;
	cin >> N >> L >> H;
	for( i = 0; i < N; ++i )
		cin >> a[ i ];

	int j;
	for( j = L; j <= H; ++j )
	{
		for( i = 0; i < N; ++i )
			if( ( a[ i ] > j && a[ i ] % j != 0 ) ||
				( a[ i ] <= j && j % a[ i ] != 0 ) )
				break;
		if( i == N )
		{
			cout << j << endl;
			return;
		}
	}
	cout << "NO\n";
}


int main ()
{
	freopen( "C-small.in","r",stdin);
	freopen( "C-small.out","w",stdout);
	int i, T;
	cin >> T;
	for( i = 1; i <= T; ++i )
	{
		cout << "Case #" << i << ": ";
		solve();
	}
}