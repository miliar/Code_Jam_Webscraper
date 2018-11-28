#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;
const int M = 10000;

char w[25] = "welcome to code jam";
char s[510];
int dp[510][25], n, m;

int dfs(int i, int j)
{
	if(dp[i][j] != -1){
		return dp[i][j];
	}
	dp[i][j] = 0;
	for(int k = i; k < n; k++){
		if(s[k] == w[j]){
			dp[i][j] = (dp[i][j] + dfs(k + 1, j + 1)) % M;
		}
	}
	return dp[i][j];
}

int main()
{
	int T, j;
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	scanf("%d", &T);
	gets(s);
	for(int i = 1; i <= T; i++){
		gets(s);
		n = strlen(s), m = strlen(w);
		memset(dp, -1, sizeof(dp));
		for( j = 0; j < m; j++){
			dp[n][j] = 0;
		}
		for(j = 0; j <= n; j++){
			dp[j][m] = 1;
		}
		int ans = dfs(0, 0), k = 0;
		char t[4];
		while(k < 4){
			t[k++] = (ans % 10) + '0';
			ans /= 10;
		}
		printf("Case #%d: ", i);
		for(k -= 1; k >= 0; k--){
			putchar(t[k]);
		}
		puts("");
	}
	return 0;
}





		
