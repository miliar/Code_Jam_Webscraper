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

const int MAXN = 100;


char a[ MAXN ][ MAXN ];
int n, m;


void solve ()
{
	int i, j;
	cin >> n >> m;
	for( i = 0; i < n; ++i )
		for( j = 0; j < m; ++j )
			cin >> a[ i ][ j ];

	bool can = true;

	int tmp;
	for( i = 0; i < n && can; ++i )
		for( j = 0; j < m && can; ++j )
			if( a[ i ][ j ] == '#' )
			{
				tmp = 0;
				for( ;  j < m && a[ i ][ j ] == '#'; ++j )
					++tmp;
				if( tmp % 2 == 1 )
					can = false;
			}

	
	for( j = 0; j < m && can; ++j )
		for( i = 0; i < n && can; ++i )
			if( a[ i ][ j ] == '#' )
			{
				tmp = 0;
				for( ;  i < n && a[ i ][ j ] == '#'; ++i )
					++tmp;
				if( tmp % 2 == 1 )
					can = false;
			}
	if( !can )
	{
		cout << "Impossible\n";
		return;
	}

	for( i = 0; i < n; ++i )
		for( j = 0; j < m; ++j )
			if( a[ i ][ j ] == '#' )
			{
				a[ i ][ j ] = a[ i + 1 ][ j + 1 ] = '/';
				a[ i ][ j + 1 ] = a[ i + 1 ][ j ] = '\\';
			}
	for( i = 0; i < n; ++i )
	{
		for( j = 0; j < m; ++j )
			cout << a[ i ][ j ];
		cout << endl;
	}
}

int main ()
{
	freopen( "A-large.in", "r", stdin );
	freopen( "A-large.out", "w", stdout );
	int T, i;
	cin >> T;
	for( i = 1; i <= T; ++i )
	{
		cout << "Case #" << i << ":\n";
		solve();
	}
	return 0;
}