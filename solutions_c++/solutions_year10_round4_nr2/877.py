#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;
#define N 1024
int p, size, miss[N], pos[N];
int price[10][N];
int visit[10][N];
long long ans;
struct Node 
{
	int x, y;
	bool operator<( const Node &v ) const 
	{
		return price[x][y] < price[v.x][v.y];
	}
}node[N];

int cmp( int x, int y )
{
	return miss[x] < miss[y];
}

void solve( )
{
	int u, v;
	int i, j, k;
	ans = 0;
	memset( visit, 0, sizeof(visit) );
	for ( i = 0; i < (1<<p); i++ )
	{
		u = pos[i]/2;
		size = 0;
		for ( j = 0; j < p; j++ )
		{
			node[size].x = j;
			node[size].y = u;
			u >>= 1;
			size++;
		}
	//	sort( node, node+size );
	//	if ( size <= miss[pos[i]] ) continue;
		for ( j = 0, k = size-1; j < p-miss[pos[i]] && k >= 0; j++, k-- )
			visit[node[k].x][node[k].y] = 1;
	}
	for ( i = 0; i < p; i++ )
	{
		for ( j = 0; j < (1<<(p-1-i)); j++ )
			if ( visit[i][j] ) 
				ans += price[i][j];
	}
}

int main( )
{
	int ca, t;
	int i, j, k;
	freopen( "B-small.in", "r", stdin );
	freopen( "B-small.out", "w", stdout );
	scanf( "%d", &ca );
	for ( t = 1; t <= ca; t++ )
	{
		scanf( "%d", &p );
		for ( i = 0; i < (1<<p); i++ ) scanf( "%d", miss+i );
		//for ( i = 0; i < (1<<p); i++ ) miss[i] = p-miss[i];
		for ( i = 0; i < (1<<p); i++ ) pos[i] = i;
		for ( i = 0; i < p; i++ )
			for ( j = 0; j < (1<<(p-1-i)); j++ ) 
				scanf( "%d", &price[i][j] );
		sort( pos, pos+(1<<p), cmp );
		solve( );
		printf( "Case #%d: %lld\n", t, ans );
	}
}
