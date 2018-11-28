#include<stdio.h>
#include<stdlib.h>
#include<string.h>
using namespace std;
int size;
char line[1000];
int dp[600][30];
char str[]="$welcome to code jam";
int main()
{
	size=strlen(str);
	gets(line);
	int cases;
	sscanf(line,"%d",&cases);
	for(int t=1;t<=cases;++t)
	{
		gets(line+1);
		memset(dp,0,sizeof(dp));
		dp[0][0]=1;
		int len=strlen(line+1);
		for(int i=1;i<=len;++i)
		{
			for(int j=1;j<size;++j)
			{
				if(str[j]!=line[i])continue;
				for(int k=0;k<i;++k)
					dp[i][j]=(dp[i][j]+dp[k][j-1])%10000;
			}
		}
		int ans=0;
		for(int i=1;i<=len;++i)
			ans=(ans+dp[i][size-1])%10000;
		printf("Case #%d: %04d\n",t,ans);
	}
	return 0;
}
