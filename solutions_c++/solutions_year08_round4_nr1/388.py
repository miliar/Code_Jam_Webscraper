#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <sstream>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef long long lint;

#define mp make_pair
#define pb push_back
#define two(x) (1<<(x))
#define sq(a) (a)*(a)
#define all(c) (c).begin(),(c).end()
#define For(i,b,e) for(int i = b;i < e;i ++)
#define foreach(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
const double PI = acos(-1.0);
#define INF 1000000000

int typ[10010];
int chg[10010];
int minval[10010][2];
int visit[10010];
int c, n, n1;

void read_it()
{
	scanf( "%d %d", &n, &c );
	memset( minval, -1, sizeof( minval ) );
	memset( visit, 0, sizeof( visit ) );
	n1 = (n-1) / 2;
	int i;
	for( i = 1; i <= n1; ++i )
		scanf( "%d %d", &typ[i], &chg[i] );
	for( i = n1 + 1; i <= n; ++i )
	{
		scanf( "%d", &typ[i] );
		minval[i][typ[i]] = 0;
		visit[i] = 1;
	}
}

void get_minval( int p )
{
	if( visit[p] )
		return;
	int l = p * 2, r = p * 2 + 1;
	get_minval( l );
	get_minval( r );
	for( int i = 0; i <= 1; ++i )
		for( int j = 0; j <= 1; ++j )
			for( int k = 0; k <= 1; ++k )
				if( minval[l][j] != -1 && minval[r][k] != -1 )
				{
					if( typ[p] == 1 && (j&k)==i && (minval[l][j] + minval[r][k] < minval[p][i] || minval[p][i] == -1 ))
						minval[p][i] = minval[l][j] + minval[r][k];
					if( typ[p] == 0 && (j|k)==i && (minval[l][j] + minval[r][k] < minval[p][i] || minval[p][i] == -1 ))
						minval[p][i] = minval[l][j] + minval[r][k];
					if( chg[p] )
					{
						if( typ[p] == 1 && (j|k)==i && (minval[l][j] + minval[r][k] + 1 < minval[p][i] || minval[p][i] == -1 ))
							minval[p][i] = minval[l][j] + minval[r][k] + 1;
						if( typ[p] == 0 && (j&k)==i && (minval[l][j] + minval[r][k] + 1 < minval[p][i] || minval[p][i] == -1 ))
							minval[p][i] = minval[l][j] + minval[r][k] + 1;
					}
				}
}

void make_it()
{
	get_minval( 1 );
	if( minval[1][c] != -1 )
		printf( "%d\n", minval[1][c] );
	else
		printf( "IMPOSSIBLE\n" );
}

int main()
{
	freopen( "data2.in", "r", stdin );
	freopen( "data.out", "w", stdout );
	int c;
	scanf( "%d", &c );
	for( int i = 0; i < c; ++i )
	{
		printf( "Case #%d: ", i + 1 );
		read_it();
		make_it();
	}
	return 0;
}