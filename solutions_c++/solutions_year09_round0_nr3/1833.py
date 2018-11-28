#include "stdio.h"
#include "iostream"
#include "string"
using namespace std;
char ku[] = " welcome to code jam";
int dp[501][21];
char str[501];
int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int T,i,j;
	cin >> T;
	ku[0] = 1;
	getchar();
	for(int cas = 1; cas <= T ; cas ++) {
		gets(str);
		memset(dp,0,sizeof(dp));
		dp[0][0] = 1;
		for(i = 0 ; str[i] ; i ++) {
			if(i) {
				for(j = 0 ; ku[j] ; j ++) {
					dp[i][j] = dp[i-1][j];
				}
			}
			for(j = 0 ; ku[j] ; j ++) {
				if(str[i] == ku[j]) {
					dp[i][j] = (dp[i][j] + dp[i][j-1])%10000;
				}
			}
		}
		printf("Case #%d: %04d\n",cas,dp[i-1][j-1]);
	}
	return 0;
}