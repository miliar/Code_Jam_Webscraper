#include <iostream>
#include <vector>


using namespace std;


bool counted[2000][2000];
int dp[2000][2000], price[2000], canLose[2000];


int dfs(int now, int losed, int depth, int nowDepth)
{
	if(counted[now][losed])
		return dp[now][losed];
	if(nowDepth == depth)
	{
		int toRet;
		if(losed < canLose[now])
			toRet = 0;
		else
			toRet = price[now];
		dp[now][losed] = toRet;
		counted[now][losed] = true;
		return toRet;
	}
	int toRet = dfs(now * 2, losed, depth, nowDepth + 1) + dfs(now * 2 + 1, losed, depth, nowDepth + 1) + price[now];
	if(losed < canLose[now])
		toRet = min(toRet, dfs(now * 2, losed + 1, depth, nowDepth + 1) + dfs(now * 2 + 1, losed + 1, depth, nowDepth + 1));
	counted[now][losed] = true;
	dp[now][losed] = toRet;
	return toRet;
}


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	scanf("%d", &tests);
	for(int asdf = 0; asdf < tests; asdf++)
	{
		printf("Case #%d: ", asdf + 1);
		int n;
		scanf("%d", &n);
		memset(canLose, 0, sizeof(canLose));
		memset(dp, 0, sizeof(dp));
		memset(counted, false, sizeof(counted));
		for(int i = 0; i < (1 << n); i++)
			scanf("%d", &canLose[i + (1 << n)]);
		for(int i = (1 << n) - 1; i >= 1; i--)
			canLose[i] = min(canLose[i * 2], canLose[i * 2 + 1]);
		for(int i = n - 1; i >= 0; i--)
			for(int j = 0; j < (1 << i); j++)
				scanf("%d", &price[(1 << i) + j]);
		printf("%d\n", dfs(1, 0, n, 1));
	}
}