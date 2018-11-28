#include <stdio.h>
#include <string.h>

char *W = " welcome to code jam";
char s[1000];
int dp[510][30],n;

int main(){
	int t,i,j,k,c=0,sum;
	
	scanf("%d%*c",&t);
	while(t--) {
		gets(s+1);
		n = strlen(s+1);
		memset(dp,0,sizeof(dp));
		for(i=1;i<=n;i++)
			if(s[i] == W[1])
				dp[i][1] = 1;
		for(i=2;i<=19;i++)
			for(j=1;j<=n;j++)
				if(s[j] == W[i])
					for(k=1;k<j;k++)
						if(dp[k][i-1] > 0)
							dp[j][i] = (dp[j][i]+dp[k][i-1])%10000;
		sum = 0;
		for(i=1;i<=n;i++)
			sum = (sum+dp[i][19])%10000;
		printf("Case #%d: %04d\n",++c,sum);
	}
	
	return 0;
}
