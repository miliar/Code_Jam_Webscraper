#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <string>
#include <map>

using namespace std;

const int SZ=510;
const int L=19;
const int mod=10000;
const char ss[]="welcome to code jam";
int dp[SZ][L+1];
char s[SZ];

int main()
{
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
	int N;
	scanf("%d", &N);
	getchar();
	for(int n=1; n<=N; n++)
	{
		gets(s);
		memset(dp, 0, sizeof(dp));
		int l=strlen(s);
		for(int i=0; i<=l; i++)
		{
			dp[i][0]=1;
		}
		for(int i=1; i<=l; i++)
		{
			for(int j=1; j<=L; j++)
			{
				if(ss[j-1]==s[i-1])
				{
					//cout<<"=="<<endl;/////////////////////
					dp[i][j]=(dp[i-1][j-1]+dp[i-1][j])%mod;
				}
				else
				{
					//cout<<"!="<<endl;/////////////////////
					dp[i][j]=dp[i-1][j];
					//cout<<dp[i-1][j]<<endl;///////////////////
				}
				//printf("dp[%d][%d]=%d\n", i, j, dp[i][j]);/////////////////////
			}
		}
		int r=dp[l][L];
		printf("Case #%d: ", n);
		int out[4];
		for(int i=3; i>=0; i--)
		{
			out[i]=r%10;
			r=r/10;
		}
		for(int i=0; i<4; i++)
		{
			printf("%d", out[i]);
		}
		printf("\n");
	}
    return 0;
}

