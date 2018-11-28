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
#include <time.h>
#include <bitset>

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

const int INF = 1000 * 1000 * 1000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-9;

void prepare()
{
	freopen("input.txt","r", stdin);
#ifndef _DEBUG
	freopen("output.txt","w",stdout);
#endif
}

int fun[35][2];

void precalc(int P)
{
	_(fun,-1);
	for (int i = 0; i <= 10; i ++)
	{
		for (int j = 0; j <= 10; j ++)
		{
			for (int k = 0; k <= 10; k ++)
			{
				int d = max(abs(i - j),abs(i - k));
				d = max(d,abs(j - k));
				if (d <= 2)
				{
					if (d == 2)
						fun[i + j + k][1] = max(i,max(j,k)) >= P;
					else
						fun[i + j + k][0] = max(i,max(j,k)) >= P;
				}
			}
		}
	}
}

int n,s,p;
int t[105];
int dp[105][105];

bool solve()
{
	scanf("%d%d%d",&n,&s,&p);
	for (int i = 0; i < n; i ++)
		scanf("%d",&t[i]);
	precalc(p);
	_(dp,-1);
	dp[0][0] = 0;
	for (int i = 0; i < n; i ++)
	{
		for (int j = 0; j <= min(s,i); j ++)
		{
			if (dp[i][j] != -1)
			{
				for (int k = 0; k < 2; k ++)
				{
					if (fun[t[i]][k] != -1)
					{
						dp[i + 1][j + k] = max(dp[i + 1][j + k],
							dp[i][j] + fun[t[i]][k]);
					}
				}
			}
		}
	}
	printf("%d\n",dp[n][s]);
	return false;
}

int main()
{
	prepare();
	int nTests;
	scanf("%d",&nTests);
	for (int i = 0; i < nTests; i ++)
	{
		printf("Case #%d: ",i + 1);
		solve();
	}
	return 0;
}