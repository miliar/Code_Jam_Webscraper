#include<cstdio>
#include<cstring>
int z,Z,i,j,dp[2][505],t,N;
char a[505],s[25];
int main(){
	for (i=0;i<19;++i) s[i] = "welcome to code jam"[i];
	
	scanf("%d\n",&Z);
	for (z=1;z<=Z;++z){
		gets(a);
		N = strlen(a);
//		printf("!!  %d\n",N);
		
		for (i=0;i<N;++i) dp[1][i] = 1;
		
		for (i=0;i<19;++i){
			
			for (j=i;j<N;++j){
				
				//fflush(stdin);
				if (j!=i){
					if (a[j]==s[i]) dp[i&1][j] = (dp[i&1][j-1] + dp[(i+1)&1][j-1])%10000;
					else dp[i&1][j] = dp[i&1][j-1];
				}else{
					if (a[j]!=s[i]) dp[i&1][j] = 0;
					else dp[i&1][j] = dp[(i+1)&1][j];
				}
//			printf("%d %d    %d\n",i,j,dp[i&1][j]);
			}
		}
		if (N<19) printf("Case #%d: 0000\n",z);
		else printf("Case #%d: %04d\n",z,dp[0][N-1]);
	}
	return 0;
}
