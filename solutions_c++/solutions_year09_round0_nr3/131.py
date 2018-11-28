#include<stdio.h>

char line[800];
char code[]="welcome to code jam";
int dp[20],temp[20];

int main()
{
	freopen("chard.out","w",stdout);

	int ks,cases,i,j;

	gets(line);
	sscanf(line,"%d",&cases);
	for(ks=1;ks<=cases;ks++)
	{
		gets(line);
		for(i=0;i<=19;i++)
			dp[i]=0;
		dp[0]=1;

		for(i=0;line[i];i++)
		{
			for(j=0;j<=19;j++) temp[j]=dp[j];

			for(j=0;j<19;j++)
				if(code[j]==line[i])
				{
					temp[j+1]=(temp[j+1]+dp[j])%10000;
				}

			for(j=0;j<=19;j++) dp[j]=temp[j];
		}

		printf("Case #%d: %04d\n",ks,dp[19]);
	}

	return 0;
}