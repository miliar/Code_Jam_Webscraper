#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctype.h>
#include <bitset>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <queue>
#include <map>
#include <set>

using namespace std;

typedef long long ll;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef istringstream iss;
typedef ostringstream oss;

#define d2(x1, y1, x2, y2) (sqr((x1)-(x2)) + sqr((y1)-(y2)))
#define sqr(a) ((a)*(a))
#define ab(a) (((a)>0)?(a):(-(a))) 
#define cl(a, val) memset(a, val, sizeof(a))
#define deb(x) cout<<#x<<" = "<<(x)<<endl
#define FG(a, b) for((a) = (b); (a) >= 0; (a)--)
#define FD(a, b) for((a) = 0; (a) < (b); (a)++)
#define all(a) (a).begin(),(a).end() 
#define sz(a) int((a).size())
#define PB push_back
#define INF 0x3fffffff
#define Y second
#define X first

char in[] = "A-small-attempt0.in";//"in.txt";
char out[] = "A-small-attempt0.out";

int m;
int dfs(vi &a, int n)
{
	if( 2*n > m ) return a[n];
	if( a[n] == 1 )
		return (dfs(a, 2*n) & dfs(a, 2*n+1));
	else return (dfs(a, 2*n) | dfs(a, 2*n+1));
}
int findVal(vi &g)
{
	int res = 0;
	if( g[1] == 1 && 2 <= sz(g) )
		res = (dfs(g, 2) & dfs(g, 3));
	else if( g[1] == 0 && 2 <= sz(g) )
		res = (dfs(g, 2) | dfs(g, 3));
	return res;
}
int n;
int main()
{
	freopen(in, "rt", stdin);
	freopen(out, "wt", stdout);

	int i, j, k, v;
	int T, tt, res, a, b;
	scanf("%d", &T);
	
	for(tt = 1; tt <= T; tt++)
	{
		res = INF;
		scanf("%d%d", &m, &v);
		vi t(2*m+1), chan;
		for(i = 1; i <= (m-1)/2; i++)
		{
			scanf("%d%d", &a, &b);
			t[i] = a;
			if( b == 1 ) chan.PB(i);
		}
		for(i = (m-1)/2 + 1; i <= m; i++)
		{
			scanf("%d", &a);
			t[i] = a;
		}
		int lim = (1 << (sz(chan)));

		if( findVal(t) == v )	res = min(res, 0);
		for(i = 0; i < lim; i++)
		{
			vi tm(t); k = 0;
			for(j = 0; j < sz(chan); j++)
			{
				if( i & (1 << j) )
				{
					if( tm[ chan[j] ] == 0 )
					{
						k++;
						tm[ chan[j] ] = 1;
					}
				}
				else if( !( i & (1 << j) ) && tm[ chan[j] ] == 1 )
				{
						k++;
						tm[ chan[j] ] = 0;
				}
			}
			if( findVal(tm) == v )
			{
				res = min(res, k);
			}
		}
		if( res != INF )
			printf("Case #%d: %d\n", tt, res);
		else printf("Case #%d: IMPOSSIBLE\n", tt);
	}
	return 0;
}