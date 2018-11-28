#include <iostream>
using namespace std;
char str[]="welcome to code jam";
int dp[600][30];
int main()
{
	int T;
	scanf("%d\n",&T);
	int n=strlen(str);
	for(int Ti=1;Ti<=T;Ti++)
	{
		char s[600];
		gets(s);
		int m=strlen(s);
		memset(dp,0,sizeof(dp));
		for(int i=0;i<m;i++) if(s[i]=='w') dp[0][i]=1;
		for(int i=1;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				if(s[j]==str[i])
				{
					for(int k=0;k<j;k++)
					{
						dp[i][j] += dp[i-1][k];
						dp[i][j] = dp[i][j]%10000;
					}
				}
			}			
		}
		int result=0;
		for(int i=0;i<m;i++)
			result += dp[n-1][i];
		result = result%10000;
		
		printf("Case #%d: %d%d%d%d\n",Ti,result/1000,(result/100)%10,(result/10)%10,result%10);
	}
}
