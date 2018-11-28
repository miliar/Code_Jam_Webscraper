#include <stdio.h>
#include <string.h>
const int SIZE = 600;
const int LEN = 200;
const int MOD = 10000;
char base[]="welcome to code jam";
char buff[SIZE];
int dp[LEN];
void work();
int main(){
	int cas;
	scanf("%d",&cas);
	int i;
	gets(buff);
	for (i=1;i<=cas;i++){
		gets(buff);
		work();
		int ans = dp[0]%MOD;
		printf("Case #%d: %04d\n",i,ans);
	}
	return 0;
}
void work(){
	memset(dp,0,sizeof(dp));
	int n = strlen(base);
	int m = strlen(buff);
	int i,j;
	for (i=m-1;i>=0;i--){
		for (j=0;j<n;j++){
			if (base[j]==buff[i]){
				if (j==n-1){//last
					dp[j]=(dp[j]+1)%MOD;
				}else{
					if (dp[j+1]>0){
						dp[j]=(dp[j]+dp[j+1])%MOD;
					}
				}
			}
		}
	}
}