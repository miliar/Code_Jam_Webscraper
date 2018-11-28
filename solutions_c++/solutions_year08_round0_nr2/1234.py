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

#define MAXN 256

int n, na, nb;
int d;
int s[MAXN];
int t[MAXN];
int con[MAXN][MAXN];
int num[MAXN];
char st[64];

int pre[MAXN];
bool used[MAXN];

int get_it()
{
	scanf( "%s", &st );
	return ((st[0]-'0') * 10 + (st[1]-'0'))*60 + (st[3]-'0') * 10 + (st[4]-'0');
}

void read_it()
{
	scanf( "%d", &d );
	scanf( "%d %d", &na, &nb );
	n = na + nb;
	int i, j;
	for( i = 0; i < n; ++i )
	{
		s[i] = get_it();
		t[i] = get_it();
	}
	memset( num, 0, sizeof( num ) );
	for( i = 0; i < na; ++i )
		for( j = na; j < n; ++j )
		{
			if( t[i] + d <= s[j] )
			{
				con[i][num[i]] = j;
				++num[i];
			}
			if( t[j] + d <= s[i] )
			{
				con[j][num[j]] = i;
				++num[j];
			}
		}
}

bool search_it( int p )
{
	used[p] = true;
	for( int i = 0; i < num[p]; ++i )
	{
		int k = con[p][i];
		if( pre[k] == -1 || ( !used[ pre[k] ] && search_it( pre[k] ) ) )
		{
			pre[k] = p;
			return true;
		}
	}
	return false;
}

void make_it()
{
	memset( pre, -1, sizeof( pre ) );
	int i;
	for( i = 0; i < n; ++i )
	{
		memset( used, 0, sizeof( used ) );
		search_it( i );
	}
	int cnta = 0, cntb = 0;
	for( i = 0; i < na; ++i )
		if( pre[i] == -1 )
			++cnta;
	for( i = na; i < n; ++i )
		if( pre[i] == -1 )
			++cntb;
	printf( "%d %d\n", cnta, cntb );
}

int main()
{
	freopen( "datab3.in", "r", stdin );
	freopen( "data.out", "w", stdout );
	int p;
	scanf( "%d", &p );
	for( int i = 1; i <= p; ++i )
	{
		printf( "Case #%d: ", i );
		read_it();
		make_it();
	}
	return 0;
}