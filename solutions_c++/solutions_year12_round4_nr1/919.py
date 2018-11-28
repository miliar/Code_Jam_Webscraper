#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker,"/STACK:64000000")

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

#define SMALL 0

void prepare()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
#else
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
}

const int nmax = 10005;
int d[nmax], l[nmax];
int dp[nmax];
int n,D;

lint dist2(lint x1,lint y1,lint x2,lint y2)
{
	return (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1);
}

bool can(int x,lint rad,int id)
{
	return d[id] <= x + rad;
}

bool solve()
{
	bool ans = false;
	scanf("%d",&n);
	for (int i = 0; i < n; i ++)
	{
		scanf("%d%d",&d[i],&l[i]);
	}
	scanf("%d",&D);
	for (int i = 0; i < n; i ++)
		dp[i] = -1;
	dp[0] = d[0];
	for (int i = 0; i < n; i ++)
	{
		if (dp[i] != -1)
		{
			int rad = dp[i];
			if (d[i] + rad >= D)
				ans = true;
			for (int j = i + 1; j < n; j ++)
			{
				if (can(d[i],rad,j))
				{
					dp[j] = max(dp[j], min(l[j],d[j] - d[i]));
				}
			}
		}
	}
	if (ans)
		printf("YES\n");
	else
		printf("NO\n");
	return false;
}

int main()
{
	prepare();
	int t;
	scanf("%d",&t);
	for (int i = 0; i < t; i ++)
	{
		printf("Case #%d: ",i + 1);
		solve();
	}
	return 0;
}