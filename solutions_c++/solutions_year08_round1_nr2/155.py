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

#define MAXM 2010
#define MAXN 2010

vector<int> s[MAXM];
vector<int> t[MAXM];
int cnt[MAXM];
int p[MAXN];
int m, n;

void read_it()
{
	memset( p, 0, sizeof( p ) );
	scanf( "%d", &n );
	scanf( "%d", &m );
	int i, j;
	for( int i = 0; i < m; ++i )
	{
		scanf( "%d", &cnt[i] );
		int a, b;
		s[i].clear();
		t[i].clear();
		for( j = 0; j < cnt[i]; ++j )
		{
			scanf( "%d %d", &a, &b );
			s[i].push_back( a - 1 );
			t[i].push_back( b );
		}
	}
}

bool make_it()
{
	bool changed;
	int i, j;
	while( 1 )
	{
		changed = false;
		int pp = -1;
		for( i = 0; i < m; ++i )
		{
			for( j = 0; j < cnt[i]; ++j )
			{
				if( t[i][j] == 1 )
					pp = s[i][j];
				if( p[s[i][j]] == t[i][j] )
					break;
			}
			if( j >= cnt[i] )
			{
				if( pp == -1 )
					return false;
				if( p[pp] == 1 )
					return false;
				p[pp] = 1;
				changed = true;
				break;
			}
		}
		if( !changed )
			return true;
	}
	return true;
}

void get_result()
{
	for( int i = 0; i < n; ++i )
		printf( " %d", p[i] );
	printf( "\n" );
}

int main()
{
	freopen( "data4.in", "r", stdin );
	freopen( "data.out", "w", stdout );
	int c;
	scanf( "%d", &c );
	for( int i = 0; i < c; ++i )
	{
		printf( "Case #%d:", i + 1 );
		read_it();
		if( make_it() )
			get_result();
		else
			printf( " IMPOSSIBLE\n" );
	}
	return 0;
}