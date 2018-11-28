#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int dp[1024][20];
char pattern[] = "welcome to code jam";
int MAX = 19;
int main(){
	int t;
	scanf("%d ",&t);
	for(int ca = 0;ca < t;ca++){
		char str[1024];
		gets(str);
		int len = strlen(str);
		for(int i=0;i<len;i++)
			for(int j=0;j<20;j++)
				dp[i][j] = 0;
		for(int i=0;i<len;i++){
			for(int j=0;j<MAX;j++){
				if(pattern[j] == str[i]){
					if(j == 0){
						dp[i][j] = 1;
					}else{
						for(int k=0;k<i;k++){
							dp[i][j] += dp[k][j-1];
							dp[i][j] %= 10000;
						}
					}
				}
			}
		}
		int ans = 0;
		for(int i=0;i<len;i++){
			ans += dp[i][18];
			ans %= 10000;
		}
		printf("Case #%d: %04d\n",ca+1,ans % 10000);
	}
	return 0;
}
