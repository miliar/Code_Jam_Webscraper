#include<stdio.h>
#include<string.h>

	/////////1234567890123456789
char s[] = "Xwelcome to code jam";

int dp[30][505];
char t[505];

int main(){

	int i,j;

	int T,N;
	scanf("%d",&T);
	gets(t);

	for(N=1;N<=T;N++){
		gets(t+1);

		memset(dp,0,sizeof(dp));

		dp[0][0] = 1;
		for(j=1;t[j];j++)
			dp[0][j] = 1;

		for(i=1;i<=19;i++){
			for(j=1;t[j];j++){
				dp[i][j] = (dp[i][j-1] + (dp[i-1][j-1] * (t[j]==s[i]))%10000) % 10000;
			}
		}
		
		printf("Case #%d: %04d\n",N,dp[19][j-1]);

	}

	return 0;
}