#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
using namespace std;


int main()
{
	freopen("in.txt","r",stdin);
	freopen("cbig.txt","w",stdout);

	string welcome = "welcome to code jam";
	int T;
	scanf("%d\n",&T);
	for(int t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);

		char str[512];
		gets(str);
		int dp[512][24]={0};
		for(int i=0;str[i];i++)
			if(str[i]==welcome[0])
				dp[i][0]=1;

		for(int i=0;str[i];i++)
		{
			for(int j=0;j<welcome.length()-1;j++)
			{
				if(dp[i][j]==0)continue;

				for(int k=i+1;str[k];k++)
				{
					if(str[k]==welcome[j+1])
					{
						dp[k][j+1]+=dp[i][j];
						dp[k][j+1]%=10000;
					}
				}
			}
		}

		int ans=0;
		for(int i=0;str[i];i++)
			ans = (ans + dp[i][welcome.length()-1])%10000;

		printf("%04d\n",ans);
	}
}