#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
#define MAXN 20010

int l[MAXN], d[MAXN], dp[MAXN];
int n, D;

int BinFind(int x)
{
	int mid, l = 0, r = n - 1, ans = -1;
	while (l <= r)
	{
		mid = (l + r) / 2;
		printf("mid = %d  d = %d\n", mid, d[mid]);
		if (d[mid] <= x)
		{
			ans = mid;
			printf("	ans = %d   %d\n", ans, d[ans]);
			l = mid + 1;
		}
		else
			r = mid - 1;
	}
	return ans;
}

int Find(int idx, int len)
{
	int fur = d[idx] + len, i;
	int furIdx = BinFind(fur);
	printf("fur = %d furIdx = %d\n", fur, furIdx);
	//printf("furIdx = %d\n", furIdx);
	for (i = furIdx; i > idx; i--)
		if (l[i] >= d[i] - d[idx])
			return i;
	return -1;
}

void Solve()
{
	int i, j, cur, idx, grab, nxt, len;
	scanf("%d", &n);
	for (i = 0; i < n; i++)
		scanf("%d%d", d + i, l + i);
	
	scanf("%d", &D);
	
	memset (dp, 0, sizeof dp);
	
	dp[0] = d[0];
	
	for (i = 0; i < n; i++)
		for (j = i + 1; j < n; j++)
			if (d[j] - d[i] <= dp[i] && dp[j] - d[i] <= l[j])
				dp[j] = max(dp[j], min(l[j], d[j] - d[i]));
	// for(i = 0; i < n; i++)
		// printf("%d ", dp[i]);
	// printf("\n");
	for (i = 0; i < n; i++)
		if (D - d[i] <= dp[i])
		{
			printf("YES\n");
			return;
		}
	printf("NO\n");
}

int main()
{
	int cas, i;
	scanf("%d", &cas);
	for (i = 1; i <= cas; i++)
	{
		printf("Case #%d: ", i);
		Solve();
	}
	return 0;
}
