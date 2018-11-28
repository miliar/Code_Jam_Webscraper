#include<iostream>
#include<string.h>

using namespace std;

char in[105][1005];
char a[1005];
int dp[10005][105];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int s,q,n,i,j,l,t;
	scanf("%d",&n);
	for(t = 1; t <= n; t ++)
	{
		scanf("%d",&s);
		getchar();
		for(i = 1; i <= s; i ++)
		{
			gets(in[i]);
		}
		for(i = 1; i <= s; i ++)
		{
			for(j = 0; j <= 1005; j ++)
				dp[j][i] = INT_MAX;
		}
		int now;
		scanf("%d",&q);
		getchar();
		for(i = 1 ; i <= q; i ++)
		{
			gets(a);
			now = 0;
			if(i == 1)
			{
				for(j = 1; j <= s; j ++)
				{
					if(strcmp(a,in[j]) != 0)
						dp[i][j] = 0;
				}
			}
			else
			{
				for(j = 1; j <= s; j ++)
				{
					if(strcmp(a,in[j]) == 0)
						continue;
					for(l = 1; l <= s; l ++)
					{
						if(dp[i-1][l] != INT_MAX)
						{
							if(j == l)
							{
								if(dp[i-1][l] < dp[i][j])
									dp[i][j] = dp[i-1][l];
							}
							else
							{
								if(dp[i-1][l]+1 < dp[i][j])
									dp[i][j] = dp[i-1][l]+1;
							}
						}
					}
				}
			}
			
		}
		int ans  = INT_MAX;
		if(q == 0 )
			ans = 0;
		else
		{
			for(j = 1; j <= s; j ++)
			{
				if(dp[q][j] < ans)
					ans = dp[q][j];
			}
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}

