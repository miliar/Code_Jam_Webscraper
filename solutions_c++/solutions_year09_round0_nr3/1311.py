#include<stdio.h>
#include<string.h>

int dp[1000][19];
char S[20]={"welcome to code jam"};

int main()
{
	int t;
	scanf("%d",&t);
	getchar();
	for(int kase=1;kase<=t;kase++)
	{
		char str[510];
		fgets(str,510,stdin);
		int nstr=strlen(str);
		memset(dp,0,sizeof(dp));
		for(int i=0;i<nstr;i++)
			for(int j=0;j<19;j++)
			{
				if(str[i]!=S[j])
					dp[i][j]=0;
				else
				{
					if(j==0)
						dp[i][0]=1;
					else
						for(int k=0;k<i;k++)
							if(str[k]==S[j-1])
								dp[i][j]=(dp[i][j]+dp[k][j-1])%10000;
				}
			}
		int ans=0;
		for(int i=0;i<nstr;i++)
			ans=(ans+dp[i][18])%10000;
		printf("Case #%d: %04d\n",kase,ans);
	}
	return 0;
}