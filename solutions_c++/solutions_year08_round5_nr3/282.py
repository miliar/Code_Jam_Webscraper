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
#define mp make_pair
#define pb push_back
#define two(x) (1<<(x))
#define sq(a) (a)*(a)
#define all(c) (c).begin(),(c).end()
#define For(i,b,e) for(int i = b;i < e;i ++)
#define foreach(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
const double PI = acos(-1.0);
#define INF 1000000000

#define MAXN 12

int n, m;

char now[MAXN][MAXN];

int nowmax[MAXN][1<<MAXN];
int mask[MAXN];
int mycnt[1<<MAXN];

void read_it()
{
	scanf( "%d %d", &n, &m );
	memset( mask, 0, sizeof( mask ) );
	for( int i = 1; i <= n; ++i )
	{
		scanf( "%s", now[i] );
		for( int j = 0; j < m; ++j )
			if( now[i][j] == 'x' )
				mask[i] |= ( 1<< j );
	}
	memset( nowmax, 0, sizeof( nowmax ) );
}

bool can( int p )
{
	for( int i = 0; i < m - 1; ++i )
		if( p & ( 1 << i ) )
			if( p & ( 1 << (i+1) ) )
				return false;
	return true;
}

bool has( int p, int q )
{
	if( q < 0 )
		return false;
	if( q >= m )
		return false;
	return ( p & (1<<q ) ) != 0;
}

bool can_it( int k, int j )
{
	for( int i = 0; i < m; ++i )
		if( k & (1<<i) )
			if( has( j, i-1) || has(j, i+1) )
				return false;
	return true;
}

void make_it()
{
	for( int i = 1; i <= n; ++i )
		for( int j = 0; j < (1<<m); ++j )
		{
			nowmax[i][j] = -1;
			if( can( j ) && ((j&mask[i])==0) )
			{
				for( int k = 0; k < (1<<m); ++k )
					if( nowmax[i-1][k] != -1 && can_it( k, j ) )
						if( nowmax[i-1][k] + mycnt[j] > nowmax[i][j] )
							nowmax[i][j] = nowmax[i-1][k] + mycnt[j];
			}
		}
}

void get_result()
{
	int nowmax1 = 0;
	for( int i = 0; i < (1<<m); ++i )
		if( nowmax[n][i] > nowmax1 )
			nowmax1 = nowmax[n][i];
	printf( " %d\n", nowmax1 );
}


int cnt_it( int p )
{
	int cnt = 0;
	while( p )
	{
		if( p & 1 )
			++cnt;
		p >>= 1;
	}
	return cnt;
}

int main()
{
	for( int i = 0; i < (1<<MAXN); ++i )
		mycnt[i] = cnt_it( i );
	freopen( "data2.in", "r", stdin );
	freopen( "data.out", "w", stdout );
	int c;
	scanf( "%d", &c );
	for( int i = 0; i < c; ++i )
	{
		printf( "Case #%d:", i + 1 );
		read_it();
		make_it();
		get_result();
	}
	return 0;
}