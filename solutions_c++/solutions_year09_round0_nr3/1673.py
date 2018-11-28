#include<iostream>
using namespace std;
__int64 dp[1000];
int main()
{
	__int64 t,i;
	char s[10000];
	__int64 tt=0;

	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%I64d",&t);
	getchar();
	while(t--)
	{
		tt++;
		memset(dp,0,sizeof(dp));
		gets(s);
		__int64 max=0;
		for(i=0;s[i]!='\0';i++)
		{
			if(s[i]=='w')
				dp[1]++;
			else if(s[i]=='e')
			{
				dp[2]+=dp[1];
				dp[7]+=dp[6];
				dp[15]+=dp[14];
			}
			else if(s[i]=='l')
			{
				dp[3]+=dp[2];
			}
			else if(s[i]=='c')
			{
				dp[4]+=dp[3];
				dp[12]+=dp[11];
			}
			else if(s[i]=='o')
			{
				dp[5]+=dp[4];
				dp[10]+=dp[9];
				dp[13]+=dp[12];
			}
			else if(s[i]=='m')
			{
				dp[6]+=dp[5];
				dp[19]+=dp[18];
				if(dp[19]>max)
					max=dp[19];
			}
			else if(s[i]==' ')
			{
				dp[8]+=dp[7];
				dp[11]+=dp[10];
				dp[16]+=dp[15];
			}
			else if(s[i]=='t')
			{
				dp[9]+=dp[8];
			}
			else if(s[i]=='d')
				dp[14]+=dp[13];
			else if(s[i]=='j')
				dp[17]+=dp[16];
			else if(s[i]=='a')
				dp[18]+=dp[17];
		}
		printf("Case #%I64d: %04I64d\n",tt,max%10000);
	}
	return 0;
}