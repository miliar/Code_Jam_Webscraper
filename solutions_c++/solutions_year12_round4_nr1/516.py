#include <stdio.h>
#include <string.h>

const int mx=10010;

struct vine
{
	int dist;
	int len;
}a[mx];

int dp[mx];

int main()
{
	int ca=1;
	int t,n;
	int i,j,k,dis_total;

	scanf("%d",&t);

	while(t--)
	{
		scanf("%d",&n);
		for(i=1;i<=n;i++)
		{
			scanf("%d%d",&a[i].dist,&a[i].len);
		}
		memset(dp,0,sizeof(dp));
		dp[1]=a[1].dist;
		scanf("%d",&dis_total);

		for(i=1;i<=n;i++)
		{
			if(dp[i])
			{
				if(dp[i]>a[i].len)
					dp[i]=a[i].len;
				for(j=i+1;j<=n;j++)
				{
					int tmp1=a[j].dist-a[i].dist;
					if(tmp1>dp[i]) break;
					if(dp[j]==0) dp[j]=tmp1;
					else if(tmp1>dp[j]) dp[j]=tmp1;
				}
			}
		}
		for(i=1;i<=n;i++)
		{
			if(dp[i]>a[i].len)
			{
				dp[i]=a[i].len;
			}
		}
		int flag=0;
		for(i=1;i<=n;i++)
		{
			if(a[i].dist+dp[i]>=dis_total)
			{
				flag=1;
				break;
			}
		}

		printf("Case #%d: ",ca++);
		if(flag)
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}

