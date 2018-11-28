#include <iostream>
#include <sstream>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()

typedef unsigned long long ull;
typedef long long lint;
typedef pair < int , int > pii;
typedef long double ld;

const int inf = 2000 * 1000 * 1000;
const lint linf = 2000000000000000000LL;
const double eps = 1e-9;

void prepare( )
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
#else
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}

vector < vector < int > > q;
vector < int > tmp;
vector < int > nn;
int a[2005];
int b[2005];
vector < int > g[2005];
int n,m;
int tt[2005];
int TIME;
int ans = -1;
vector < int > col;
int r[2005];

void rec( vector < int > t )
{
	TIME ++;
	vector < int > t1;
	vector < int > t2;
	for ( int i = 0; i < sz(t); i ++ )
		tt[t[i]] = TIME;
	int x,y;
	for ( int i = 0; i < sz(t); i ++ )
	{
		x = t[i];
		for ( int j = 0; j < sz(g[x]); j ++ )
		{
			y = g[x][j];
			if (t[(i+1)%sz(t)] != y && t[(i-1+sz(t))%sz(t)] != y)
			if (tt[y] == TIME)
			{
				int k;
				for ( k = i; t[k] != y; k = (k+1) % sz(t) )
				{
					t1.pb(t[k]);
				}
				t1.pb(y);

				for ( ; k != i; k = (k+1) % sz(t) )
				{
					t2.pb(t[k]);
				}
				t2.pb(x);
				rec(t1);
				rec(t2);
				return;
			}
		}
	}
	if (sz(t)>0)
		q.pb(t);
	return;
}

bool check( int x, int nc )
{
	for ( int i = 1; i <= nc; i ++ )
		tt[i] = 0;
	for ( int i = 0; i < sz(q[x]); i ++ )
	{
		tt[r[q[x][i]]] = 1;
	}
	for ( int i = 1; i <= nc; i ++ )
		if ( !tt[i] )
			return false;
	return true;
}

void go( int pos, int c )
{
	if ( c + n - pos <= ans ) return;
	if ( pos == n )
	{
		bool ok = true;
		for ( int i = 0; i < sz(q); i ++ )
		{
			ok &= check(i,c);
		}
		if (ok)
		{
			ans = c;
			for ( int i = 0; i < n; i ++ )
			{
				col[i] = r[i];
			}
		}
		return;
	}
	for ( int i = 1; i <= c; i ++ )
	{
		r[pos] = i;
		go(pos+1,c);
	}
	r[pos] = c + 1;
	go(pos+1,c+1);
}

bool solve( )
{
	_(tt,0);
	TIME = 0;
	q.clear();
	cin >> n >> m;
	col.clear();
	col.resize(n);
	for ( int i = 0; i < m; i ++ )
	{
		cin >> a[i];
		a[i]--;
	}
	for ( int i = 0; i < m; i ++ )
	{
		cin >> b[i];
		b[i]--;
	}
	tmp.clear();
	for ( int i = 0; i < n; i ++ )
	{
		tmp.pb(i);
		g[i].clear();
	}
	
	for ( int i = 0; i < m; i ++ )
	{
		if ( a[i] > b[i] )
			swap(a[i],b[i]);
		g[a[i]].pb(b[i]);
		g[b[i]].pb(a[i]);
	}
	rec(tmp);

	ans = -1;
	go(0,1);
	printf("%d\n",ans);
	for ( int i = 0; i < sz(col); i ++ )
	{
		if (i) printf(" ");
		printf("%d",col[i]);
	}
	printf("\n");

	return false;
}

int main()
{
	prepare( );
	int t;
	cin >> t;
	for ( int i = 0; i < t; i ++ )
	{
		printf("Case #%d: ",i+1);
		solve();
	}
	return 0;
}