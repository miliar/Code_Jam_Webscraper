#include <stdio.h>

int dp[510][20];
char ref[]=" welcome to code jam";

int main(){
	int t,u,i,j,k;
	char s[500];
	gets(s);
	sscanf(s,"%d",&t);
	for (u=0; u<t; u++){
		gets(s+1);
		for (j=1; j<=19; j++) dp[0][j]=0;
		dp[0][0]=1;
		for (i=1; s[i]; i++){
			for (j=0; j<=19; j++) dp[i][j]=dp[i-1][j];
			for (j=1; j<=19; j++){
				if (s[i]==ref[j]) dp[i][j]=(dp[i][j]+dp[i-1][j-1])%10000;
			}
		}
		printf("Case #%d: %04d\n",u+1,dp[i-1][19]);
	}
	return 0;
}
