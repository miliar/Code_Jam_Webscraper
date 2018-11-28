#include <stdio.h>
#include <string.h>
#include <stdlib.h>

const int MAX = 510;
char p[20];

int dp[MAX][26];

int main(){
	//freopen("C-large.in","r",stdin);
	
	strcpy(p,"welcome to code jam");
	
	char buffer[MAX];
	int turn, T;
	fgets(buffer,MAX,stdin);
	sscanf(buffer,"%d",&T);
	for(turn=0;turn<T;++turn){
		fgets( buffer,MAX,stdin );
		int i, j, m = strlen(buffer);
		memset( dp, 0, sizeof(dp) );
		if( buffer[0]=='w' )	dp[0][0] = 1;
		for(i=1;i<m;++i){
			dp[i][0] = dp[i-1][0];
			if( buffer[i]==p[0] )	dp[i][0]++;
			for(j=1;j<19;++j){
				dp[i][j] = dp[i-1][j];
				if( p[j]==buffer[i] )	dp[i][j] += dp[i-1][j-1];
			}
			for(j=0;j<19;++j)	if(dp[i][j] >= 10000 )	dp[i][j] %= 10000;
		}
		printf("Case #%d: %04d\n",1+turn,dp[m-1][18]);
	}
	return 0;
}
