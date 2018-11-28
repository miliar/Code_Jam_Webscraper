#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <sstream>
#include <algorithm>

using namespace std;

#define sqr(a) ((a)*(a))
#define det2(a,b,c,d) ((a)*(d) - (b)*(c))
#define FOR(a,b,c) for(int a=(b); a<(c); ++a)

bool Less(vector<int> &a, vector<int> &b)
{
	FOR(i,0,a.size())
		if (a[i] >= b[i]) return false;
	return true;
}

vector<int> xy, yx, uy;

bool dfs(int v, vector< vector<bool> > &Adj)
{
	int n = xy.size();
	FOR(i,0,n)
	{
		if (Adj[v][i] && !uy[i])
		{
			uy[i] = true;
			if (yx[i] == -1 || dfs(yx[i], Adj))
			{
				yx[i] = v;
				xy[v] = i;
				return 1;
			}
		}
	}
	return 0;
}

int MaxMatching(vector< vector<bool> > &Adj)
{
	int n = Adj.size();
	xy = vector<int>(n, -1);
	yx = vector<int>(n, -1);

	int res = 0;
	FOR(i,0,n) if (xy[i] == -1)
	{
		uy = vector<int>(n, 0);
		res += dfs(i, Adj);
	}

	return res;
}

int sol1(vector< vector<int> > &prices)
{
	int n = prices.size();
	vector< vector<bool> > Adj(n, vector<bool>(n));
	FOR(i,0,n)
		FOR(j,0,n)
			Adj[i][j] = Less(prices[j], prices[i]);
	return n - MaxMatching(Adj);
}

int main()
{
    int T;

	scanf("%d", &T);
	FOR(cas,1,T+1)
	{
		int n, k;
		scanf("%d%d", &n, &k);
		vector< vector<int> > prices(n, vector<int>(k));

		FOR(i,0,n)
		{
			FOR(j,0,k) scanf("%d", &prices[i][j]);
		}

		printf("Case #%d: %d\n", cas, sol1(prices));
	}	

    return 0;
}
