#include<iostream>
#include<string>
using namespace std;
char a[]="welcome to code jam";
char s[1000];
int dp[501][20];
const int mod=10000;
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.txt","w",stdout);
	int zu;
	scanf("%d",&zu);
	gets(s);
	for(int ca=1;ca<=zu&&gets(s);ca++)
	{
		printf("Case #%d: ",ca);
		memset(dp,0,sizeof(dp));
		dp[0][0]=1;
		int len=strlen(a);
		for(int i=0;s[i];i++)
		{
			int j;
			for(j=0;j<=len;j++)
			{
				if(s[i]==a[j])
					dp[i+1][j+1]+=dp[i][j];
			}
			for(j=0;j<=len;j++)
				dp[i+1][j]+=dp[i][j];
			for(j=0;j<=len;j++)
				dp[i+1][j]%=10000;
		}
		printf("%04d\n",dp[strlen(s)][len]);
	}
}
