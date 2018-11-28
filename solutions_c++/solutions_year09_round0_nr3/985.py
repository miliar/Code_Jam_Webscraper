#include <cstdio>
#include <iostream>
using namespace std;

const int MOD=10000;

int dp[20],T,cas=1,sum[20];
char s[600];

int main()
{
	freopen("d://C-large.in","r",stdin);
	freopen("d://2.txt","w",stdout);
	scanf("%d",&T);
	getchar();
	while(T--)
	{
		memset(dp,0,sizeof(dp));
		dp[0]=1;
		gets(s);
		for(int i=0;i<strlen(s);i++)
		{
			if(s[i]=='w')
				dp[1]=(dp[0]+dp[1])%MOD;
			else if(s[i]=='e')
			{
				dp[2]=(dp[1]+dp[2])%MOD;
				dp[7]=(dp[6]+dp[7])%MOD;
				dp[15]=(dp[15]+dp[14])%MOD;
			}
			else if(s[i]=='l')
			{
				dp[3]=(dp[3]+dp[2])%MOD;
			}
			else if(s[i]=='c')
			{
				dp[4]=(dp[3]+dp[4])%MOD;
				dp[12]=(dp[12]+dp[11])%MOD;
			}
			else if(s[i]=='o')
			{
				dp[5]=(dp[5]+dp[4])%MOD;
				dp[10]=(dp[10]+dp[9])%MOD;
				dp[13]=(dp[13]+dp[12])%MOD;
			}
			else if(s[i]=='m')
			{
				dp[6]=(dp[6]+dp[5])%MOD;
				dp[19]=(dp[19]+dp[18])%MOD;
			}
			else if(s[i]==' ')
			{
				dp[8]=(dp[8]+dp[7])%MOD;
				dp[11]=(dp[11]+dp[10])%MOD;
				dp[16]=(dp[16]+dp[15])%MOD;
			}
			else if(s[i]=='t')
			{
				dp[9]=(dp[9]+dp[8])%MOD;
			}
			else if(s[i]=='d')
			{
				dp[14]=(dp[14]+dp[13])%MOD;
			}
			else if(s[i]=='j')
			{
				dp[17]=(dp[17]+dp[16])%MOD;
			}
			else if(s[i]=='a')
			{
				dp[18]=(dp[18]+dp[17])%MOD;
			}
			else continue;
		}
		printf("Case #%d: %04d\n",cas++,dp[19]%MOD);
	}
	return 0;
}