//* Problem  : Saving the Universe
//* Date     : 2008.07.17
//* Author   : alt
//* Language : C++
//* Compiler : Microsoft Visual C++ 8.0

#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <queue>
#include <map>
#include <string>

using namespace std;

#define int64 long long
#define MP(a,b) make_pair(a,b)
#define PB(a) push_back(a)
#define SZ(a) (int)a.size()
#define FOR(i, n) for (int i = 0; i < (int)n; i++)
#define INF 1000*1000*1000
#define ALL(a) a.begin(), a.end()

#define int64 long long

int n, m, it, nt, res;

int a[1000];

char s[1000];

map <string, int> mp; int imp;

int p[128];

int dp[1024][128];

void solve()
{
	for (int k = 1; k <= m; k++)
		dp[n][k] = a[n] == k;
	for (int i = n - 1; i >= 1; i--)
		for (int k = 1; k <= m; k++)
			if (a[i] != k)
			{
				dp[i][k] = dp[i + 1][k];
			}
			else
			{
				dp[i][k] = INF;
				for (int j = 1; j <= m; j++)
					if (j != k)
						dp[i][k] = min(dp[i][k], dp[i+1][j] + 1);
			}
	res = INF;
	for (int k = 1; k <= m; k++)
		res = min(res, dp[1][k]);
}

void result()
{
	printf("Case #%d: %d\n", it, res);
}

int index(char *s)
{
	string ss(s);
	int res = mp[ss];
	if (!res)
		res = mp[ss] = ++imp;
	return res;
}

int main()
{
#ifdef _DEBUG
	freopen("1064", "r", stdin);
	freopen("A-large.out", "w", stdout);	
#endif
	gets(s); sscanf(s, "%d", &nt);
	for (it = 1; it <= nt; it++)
	{
		imp = 0; mp.clear();
		memset(p, 0, sizeof(p));
		gets(s); sscanf(s, "%d", &m);
		FOR(i, m)
		{
			gets(s);
			index(s);
		}
		gets(s); sscanf(s, "%d", &n);
		for (int i = 1; i <= n; i++)
		{
			gets(s); 
			a[i] = index(s);
		}
		solve();
		result();
	}
	return 0;
}

