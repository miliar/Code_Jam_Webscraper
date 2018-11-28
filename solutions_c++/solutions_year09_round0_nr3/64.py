#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define SET(A,p) memset(A,p,sizeof(A))

int dp[512][20];
char we[] = "welcome to code jam";
char buf[512];

int main()
{
	int T, te = 1;
	cin.getline(buf,512);
	sscanf(buf,"%d",&T);
	while(T--)
	{
		cin.getline(buf,512);
		SET(dp,0); FOR(i,0,512) dp[i][19] = 1;
		int n = strlen(buf);
		for(int i = n-1; i >= 0; i--)
			FOR(j,0,19) dp[i][j] = (dp[i+1][j] + ((buf[i] == we[j])?dp[i+1][j+1]:0))%10000;
		printf("Case #%d: %04d\n",te,dp[0][0]);
		te++;
	}
	return 0;
}
