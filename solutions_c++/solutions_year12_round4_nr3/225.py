#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <memory.h>
using namespace std;

#define fi first
#define sc second
#define mp make_pair
#define pb push_back
#define ALL(c) (c).begin(), (c).end()
#define RESET(a,b) memset( (a), b, sizeof(a) )
#define ren(a,b,c) for (int a=b; a<c; ++a)
#define red(a,b,c) for (int a=b; a>=c; --a)
#define repi(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)

const double eps = 1e-9;
typedef long long ll;
typedef pair <int,int> pii;

//lintaor1's template

int i[2048], m[2048], o[2048];

void solve( const int& );
int geth( int );

int main()
{
	freopen( "C-large.in", "r", stdin );
	freopen( "C-large.ou", "w", stdout );
	int T;
	cin >> T; ++T;
	ren (TT,1,T)
	{
		solve( TT );
	}
	return 0;
}

//-----
void solve( const int &T )
{
	int n;
	cin >> n;
	
	RESET( i,0 );
	RESET( m,-1 );
	RESET( o,-1 );
	ren (x,1,n) scanf("%d",&i[x]);

	bool impo = false;
	ren (x,1,n)
	{
		ren (y,x+1,i[x])
			if (i[y] > i[x])
			{
				impo = true;
				break;
			}
		if (impo) break;
	}
	
	if (impo) printf("Case #%d: Impossible\n", T); else
	{
		int h = 0;
		ren (x,1,n) if (m[x] == -1)
		{
			int cur = x;
			while (cur != n && m[cur] == -1)
			{
				m[cur] = h;
				cur = i[cur];
			}
			++h;
		}
		
		m[n] = 0;
		++n;
		printf("Case #%d:", T);
		ren (x,1,n)
		{
			if (o[x] == -1) o[x] = geth( x );
			printf(" %d", o[x]);
		}
		printf("\n");
		
		/*
		ren (x,1,n)
		{
			printf("%d %d %d\n", i[x], o[x], m[x]);
		}
		*/
		
	}
}


int geth( int x )
{
	if (o[x] != -1) return o[x];
	if (x==0) return o[x] = 100000000;
	return o[x] = geth( i[x] ) - (m[x] * (i[x]-x));
}
