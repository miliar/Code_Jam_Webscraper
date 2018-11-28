#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<set>

using namespace std;

const int N = 1024;

int min(int a, int b)
{
	return a < b ? a : b;
}

int max(int a, int b)
{
	return a > b ? a : b;
}

int d[10010], l[10010];
int dp[10010];

int main()
{
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-small2.out", "w", stdout);
	
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int i, j, k;
	int cas;
	int T;
	scanf("%d", &T);
	for(cas = 1; cas <= T; cas ++)
	{
		int n, m;
		scanf("%d", &n);
		j = 1;
		bool flag = false;
		int mx = 0;
		for(i = 1; i <= n; i ++)
		{
			scanf("%d %d", &d[i], &l[i]);
			dp[i] = 0;
			if(i == 1)
			{
				dp[i] = min(d[i], l[i]);
			}
			else {
				while(j < i && dp[j]+d[j] < d[i])
				{
					j ++;
				}
				if(j < i)
				{
					dp[i] = min(d[i]-d[j], l[i]);
				}
			}
			if(dp[i] > 0 && dp[i]+d[i] > mx)mx = dp[i]+d[i];
			//printf("%d ", dp[i]);
		}
		int D;
		scanf("%d", &D);
		if(D <= mx)
		{
			printf("Case #%d: YES\n", cas);
		}
		else {
			printf("Case #%d: NO\n", cas);
		}
	}
	return 0;
}
