#include <stdio.h>
#include <string>
#include <algorithm>
#define maxp 11
#define maxn 2049
using namespace std;

int T, t = 1, p;
int m[1025];
int cost[maxn];
int minm[1025][1025];
int lookup[maxn][maxn];

void computeMin()
{
	for(int i = 1; i <= (1 << p); ++i)
	{
		minm[i][i] = m[i];
		for(int j = i + 1; j <= (1 << p); ++j)
		{
			minm[i][j] = min(minm[i][j - 1], m[j]);
		}
	}
}
int getMin(int ll, int rr)
{
	return minm[ll][rr];
}
int dp(int id, int miss, int ll, int rr)
{
	if(ll == rr)
		return 0;

	if(lookup[id][miss] != -1)
		return lookup[id][miss];

	int ret = cost[id] + dp(id + id, miss, ll, (ll + rr) >> 1) + dp(id + id + 1, miss, ((ll + rr) >> 1) + 1, rr);
	if(getMin(ll, rr) > miss)
	{
		int res = dp(id + id, miss + 1, ll, (ll + rr) >> 1) + dp(id + id + 1, miss + 1, ((ll + rr) >> 1) + 1, rr);
		ret = ret < res ? ret : res;
	}
	lookup[id][miss] = ret;
	return ret;
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	for(scanf("%d", &T); T; --T)
	{
		scanf("%d", &p);

		for(int i = 1; i <= (1 << p); ++i)
			scanf("%d", m + i);
		computeMin();
		for(int i = 0; i < p; ++i)
		{
			for(int j = 0; j < (1 << (p - i - 1)); ++ j)
			{
				scanf("%d", cost + (1 << (p - i - 1)) + j);
			}
		}
		
		memset(lookup, -1, sizeof(lookup));

		int ans = dp(1, 0, 1, (1 << p));

		printf("Case #%d: %d\n", t++, ans);
	}
}
