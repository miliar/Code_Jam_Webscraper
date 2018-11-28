#include <stdio.h>
#include <algorithm>
#include <string>
#include <iostream>
#include <memory.h>

using namespace std;

#define MOD 10000

const string wel="welcome to code jam";

int dp[1000][20];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n;
	scanf("%d\n",&n);
	char cs[1000];
	for (int K=0;K<n;K++)
	{
		memset(dp,0,sizeof(dp));
		memset(cs,0,sizeof(cs));
		string t;
		gets(cs);
		t=cs;
		int res=0;
		for (int i=1;i<=t.size();i++)
		{
			for (int j=1;j<=wel.size();j++)
			{
				if (t[i-1]!=wel[j-1])
					continue;
				if (j==1)
					dp[i][j]=1;
				else for (int k=1;k<i;k++)
					if (t[k-1]==wel[j-2])
					{
						dp[i][j]+=dp[k][j-1];
						dp[i][j]%=MOD;
					}
			}
			res+=dp[i][wel.size()];
			res%=MOD;
		}
		printf("Case #%d: %04d\n",K+1,res);
	}
	return 0;
}