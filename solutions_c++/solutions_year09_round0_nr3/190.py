#include<iostream>
#include<string>
#include<stdio.h>
#include<vector>
#include<math.h>
#include<queue>
#include<sstream>
#include<algorithm>
#include<set>
using namespace std;
const int INF=1<<30;
typedef __int64 ll;
const int mod=10000;
int ca;
char ft[100]=" welcome to code jam";
char s[1000];
int dp[1000][100];
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,k,ca;
	scanf("%d",&ca);getchar();
	int kk=1;
	int len=strlen(ft+1);
	while(ca--) 
	{
		gets(s+1);
		int n=strlen(s+1);
		memset(dp,0,sizeof(dp));
		dp[0][0]=1;
		for(i=1;i<=n;i++) 
		{
			for(j=1;j<=len;j++) 
				if(ft[j]==s[i]) 
				{
					for(k=0;k<i;k++) 
						dp[i][j]=(dp[i][j]+dp[k][j-1])%mod;
				}
		}
		int ma=0;
		for(i=1;i<=n;i++) 
		{
			ma=(ma+dp[i][len])%mod;
		}
		printf("Case #%d: %04d\n",kk++,ma);
	}
	return 0;
}