#include <stdio.h>
#include <algorithm>
using namespace std;
#define MAX 1234
#define INF 100000000000000

int p;
int miss[MAX];
int cost[MAX];
long long dp[MAX*2][12];

void Solve()
{
	scanf("%d", &p);
	for (int i=0; i<(1<<p); i++)
		scanf("%d", &miss[i]);
	for (int i=0; i<(1<<p)-1; i++)
		scanf("%d", &cost[i]);

	for (int i=0; i<(1<<p); i++)
	{
		int k = p-miss[i];
		for (int j=0; j<=p; j++)
			dp[i][j] = j<k ? INF : 0;
	}
	int prevs = 0;
	int s = (1<<p);
	for (int r=p-1; r>=0; r--)
	{
		int t = s + (1<<r);
		for (int i=s; i<t; i++)
		{
			int i1 = prevs + (i-s)*2;
			for (int j=0; j<=r+1; j++)
				dp[i][j] = dp[i1][j] + dp[i1+1][j];
			int c = cost[i - (1<<p)];
			for (int j=0; j<=r; j++)
				dp[i][j] = min(dp[i][j], dp[i][j+1] + c);
		}
		prevs = s;
		s = t;
	}
	printf("%I64d\n", dp[s-1][0]);
}


int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int T;
	scanf("%d",&T);
	for (int t1=0;t1<T;t1++)
	{
		printf("Case #%d: ", t1+1);
		Solve();
	}

	return 0;
}

