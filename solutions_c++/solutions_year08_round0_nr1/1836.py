#include<stdio.h>
#include<memory.h>
#include<string.h>
int main()
{
	int n,s,q,i,j,k,l,min,t;
	char se[110][110];
	char tmp[110];	
	int dp[110][1024];		
	scanf("%d",&n);
	for(l=1;l<=n;l++)
	{
		memset(dp,0,sizeof(dp));
		scanf("%d\n",&s);		
		for(i=0;i<s;i++)
		{
			gets(se[i]);		
		}
		scanf("%d\n",&q);
		for(i=1;i<=q;i++)
		{
			gets(tmp);			
			for(j=0;j<s;j++)
			{
				if(strcmp(tmp,se[j])==0){t=j;break;}
			}
			for(j=0;j<s;j++)
			{
				min=9999999;
				for(k=0;k<s;k++)
				{
					if(k!=j && dp[i-1][k]<min) min=dp[i-1][k];
				}
				min++;
				if(j==t || dp[i-1][j]>=min)
				{					
					dp[i][j]=min;
				}
				else
				{					
					dp[i][j]=dp[i-1][j];
				}
			}
		}
		min=9999999;
		for(i=0;i<s;i++)if(dp[q][i]<min)min=dp[q][i];
		printf("Case #%d: %d\n",l,min);
	}
	return 0;
}