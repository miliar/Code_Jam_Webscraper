#include <iostream>
#include <stdio.h>
#include <map>
#include <iomanip>
#include <string.h>
#include <math.h>
#include <memory.h>
#include <string>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <fstream>

using namespace std;

#define N 10007
int d[N];
int l[N];
int D, n;
int dp[N];

int getdp(int i)
{
	if (dp[i]+1) return dp[i];
	if (i == 0) return dp[i] = d[i];
	int ans = -2;
	for ( int j=i-1; j>=0; j--)
	{
		if (getdp(j) < d[i]-d[j]) continue;
		ans = max(ans, d[i]-d[j]);
	}
	ans = min(ans, l[i]);
	return dp[i] = ans;
}

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, ca=1;
	scanf("%d", &T);
	while (T --)
	{
		scanf("%d", &n);
		memset(dp, -1, sizeof(dp));
		for ( int i=0; i<n; i++)
		{
			scanf("%d%d", &d[i], &l[i]);
		}
		scanf("%d", &D);
		int mm = 0;
		for ( int i=0; i<n; i++)
		{
			if (getdp(i) != -2)
				mm = max(mm, getdp(i)+d[i]);
		}
		printf("Case #%d: %s\n", ca++, mm >= D ? "YES" : "NO");
	}
	return 0;
}

