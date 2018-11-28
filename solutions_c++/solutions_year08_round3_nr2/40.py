#include <stdio.h>
#include <string.h>

int main()
{
	__int64 ans;
	__int64 dp[42][210];
	char s[1024];
	int cas,asd,tmp;
	int i,j,k,count,l;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&cas);
	for(asd=0;asd<cas;asd++)
	{
		scanf("%s",s);
		l =strlen(s);
		for(i=0;i<=l;i++)
		{
			for(j=0;j<210;j++)
				dp[i][j]=0;
		}
		tmp = s[i]-'0';
		dp[0][0] = 1;
		for(i=1;i<=l;i++)
		{
			for(j=0;j<i;j++)
			{
				count=0;
				for(k=j;k<i;k++)
					count = (10 * count + s[k] - '0')%210;
				if(j!=0)
				{
					for(k=0;k<210;k++)
					{
						dp[i][k] += dp[j][ (k + count) % 210];
						dp[i][k] += dp[j][ (k + 210 - count) %210];
					}
				}
				else
					dp[i][count] = 1;
			}
		}
		ans=0;
		for(i=0;i<210;i++)
		{
			if(i%2 ==0 || i %3 ==0 || i%5==0 || i%7 ==0)
				ans += dp[l][i];
		}
		printf("Case #%d: %I64d\n",asd+1,ans);
	}
	return 0;
}