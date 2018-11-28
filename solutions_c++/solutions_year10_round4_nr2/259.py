#pragma comment( linker, "/stack:128000000" )
#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>

void prepare( )
{
	freopen( "input.txt", "r", stdin );
#ifndef _DEBUG
	freopen( "output.txt", "w", stdout );
#endif
}

#include <cmath>
#include <cassert>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <sstream>
#include <iostream>
#include <deque>

using namespace std;

#define fo(a,b,c) for(a =(b);a<(c);++a)
#define fr(a,b) fo(a,0,(b))
#define fi(a) fr(i,(a))
#define fj(a) fr(j,(a))
#define fk(a) fr(k,(a))
#define all(a) (a).begin(),(a).end()
#define mp make_pair
#define pb push_back
#define sz(a) (int)(a).size()
#define _(a,b) memset((a),(b),sizeof(a))
#define __(a) _((a),0)

typedef long long lint;

const int MAXN = 12;
const int INF = 1000000000;

int n, m, n2;
int d[1 << MAXN][MAXN + 1];
int c[1 << MAXN];
int w[1 << MAXN];

int solve( int id, int h )
{
	if ( id >= n2 )
	{
		if ( n - h <= w[id - n2] )
			return 0;
		return INF;
	}
	int &res = d[id][h];
	if ( res >= 0 )
		return res;
	res = min( solve( id * 2, h + 1 ) + solve( id * 2 + 1, h + 1 ) + c[id], 
		solve( id * 2, h ) + solve( id * 2 + 1, h ) );
	if ( res > INF )
		res = INF;
	return res;
}

int main( )
{
	prepare( );
	int i, j, k;
	int t, tn;
	cin >> tn;
	fr( t, tn )
	{
		printf( "Case #%d: ", t + 1 );
		scanf( "%d", &n );
		n2 = 1 << n;
		fi( n2 ) fj( n + 1 )
		{
			d[i][j] = -1;
		}
		fi( n2 )
		{
			scanf( "%d", &w[i] );
		}
		for( i = n - 1; i >= 0; -- i )
		{
			fj( 1 << i )
			{
				scanf( "%d", &c[( 1 << i ) + j] );
			}
		}
		printf( "%d\n", solve( 1, 0 ) );
	}
	return 0;
}