//AlexFetisov
//Accepted
//I'm Feeling Lucky!

#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:128000000")

#include <iostream>

void initf()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
}

#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
#include <string>
#include <sstream>

using namespace std;

#define fr(i,a,b) for ( int i = ( a ); i <= ( b ); ++i)
#define fi(a) for ( int i = 0; i < ( a ); ++i)
#define fj(a) for ( int j = 0; j < ( a ); ++j)
#define fk(a) for ( int k = 0; k < ( a ); ++k)
#define CLR(a, b) memset( ( a ), ( b ), sizeof( ( a ) ) )
#define clr(a) CLR( ( a ), 0 )
#define pb push_back
#define mp make_pair
#define all( v ) ( v ).begin(),( v ).end()

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef vector < int > vi;
typedef pair < int, int > pii;

const int inf = 1 << 30;

int p[100*101];
int rank[100*101];

void makeset( int x )
{
	p[x] = x;
	rank[x] = 0;
}

int findset( int x )
{
	if ( x != p[x] ) p[x] = findset( p[x] );
	return ( p[x] );
}

void unionset( int x, int y )
{
	x = findset( x );
	y = findset( y );
	if ( x == y ) return;
	if ( rank[y] > rank[x] )
	{
		p[x] = y;
	}
	else
	{
		p[y] = x;
		if ( rank[x] == rank[y] ) ++rank[x];
	}
}

int n, m;

bool valid( int x, int y )
{
	return ( x >= 0 && y >= 0 && x < n && y < m );
}

int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};

int wh[101][101];
int f[101][101];

void choose( int x, int y )
{
	int mi = inf;
	wh[x][y] = -1;
	fi( 4 )
	{
		int nx = x + dx[i], ny = y + dy[i];
		if ( !valid( nx, ny ) ) continue;
		mi = min( mi, f[nx][ny] );
	}
	if ( mi >= f[x][y] ) return;
	fi( 4 )
	{
		int nx = x + dx[i], ny = y + dy[i];
		if ( !valid( nx, ny ) ) continue;
		if ( mi == f[nx][ny] )
		{
			wh[x][y] = i;
			return;
		}
	}
}

int col[101][101];

void dfs( int x, int y, int c )
{
	if ( col[x][y] != -1 ) 
	{
		unionset( c, col[x][y] );
		return;
	}
	col[x][y] = c;
	if ( wh[x][y] == -1 ) return;
	dfs( x + dx[ wh[x][y] ], y + dy[ wh[x][y] ], c );
}

char g[30];
char nlet;

void solve()
{
	int tst;
	scanf("%d", &tst );
	fr(t,1,tst )
	{
		cout << "Case #" << t << ":\n";

		scanf("%d%d", &n, &m );
		CLR( col, -1 );
		fi( n ) fj( m ) scanf("%d", &f[i][j] );
		fi( n ) fj( m ) choose( i, j );
		int c = 0;
		int cnt = 0;
		fi( n ) fj( m )
			makeset( cnt++ );
		fi( n ) fj( m )
			if ( col[i][j] == -1 )
				dfs( i, j, c++);
		fi( 30 ) g[i] = ' ';
		nlet = 'a';
		fi( n ) fj( m )
			if ( g[findset(col[i][j])] == ' ' )
				g[findset(col[i][j])] = nlet++;
		fi( n ) 
		{
			fj( m )
				printf("%c ", g[findset(col[i][j])] );
			printf("\n" );
		}
	}
}

int main()
{
	initf();
	solve();
	return (0);
}