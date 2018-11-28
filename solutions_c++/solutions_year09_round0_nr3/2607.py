#include<iostream>
#include<algorithm>
#include<string>
#include<cmath>
using namespace std;
#define MOD 10000
#define N 510
char s[N];
int dp[25];
int main()
{
//	#ifndef ONLINE_JUDGE
//    freopen("b.in","r",stdin);
//    freopen("out.txt","w",stdout);
//	#endif
	int t,len,casenum=1;
	char c;
	scanf("%d",&t);
	c=getchar();
	while(t--)
	{
		gets(s);
		len=strlen(s);
		memset(dp,0,sizeof(dp));
		for(int i=0;i<len;i++)
		{
			if(s[i]=='w')
			{
				dp[0]++;
				dp[0]%=MOD;
			}
			else if(s[i]=='e')
			{
				dp[1]+=dp[0];
				dp[1]%=MOD;
				dp[6]+=dp[5];
				dp[6]%=MOD;
				dp[14]+=dp[13];
				dp[14]%=MOD;
			}
			else if(s[i]=='l')
			{
				dp[2]+=dp[1];
				dp[2]%=MOD;
			}
			else if(s[i]=='c')
			{
				dp[3]+=dp[2];
				dp[3]%=MOD;
				dp[11]+=dp[10];
				dp[11]%=MOD;
			}
			else if(s[i]=='o')
			{
				dp[4]+=dp[3];
				dp[9]+=dp[8];
				dp[12]+=dp[11];
				dp[4]%=MOD;
				dp[9]%=MOD;
				dp[12]%=MOD;
			}
			else if(s[i]=='m')
			{
				dp[5]+=dp[4];
				dp[18]+=dp[17];
				dp[5]%=MOD;
				dp[18]%=MOD;
			}
			else if(s[i]==' ')
			{
				dp[7]+=dp[6];
				dp[10]+=dp[9];
				dp[15]+=dp[14];
				dp[7]%=MOD;
				dp[10]%=MOD;
				dp[15]%=MOD;
			}
			else if(s[i]=='t')
			{
				dp[8]+=dp[7];
				dp[8]%=MOD;
			}
			else if(s[i]=='d')
			{
				dp[13]+=dp[12];
				dp[13]%=MOD;
			}
			else if(s[i]=='j')
			{
				dp[16]+=dp[15];
				dp[16]%=MOD;
			}
			else if(s[i]=='a')
			{
				dp[17]+=dp[16];
				dp[17]%=MOD;
			}
		}
		printf("Case #%d: %04d\n",casenum++,dp[18]%MOD);
	}
				
//	#ifndef ONLINE_JUDGE
//    while(1);
//	#endif
	return 0;
}
