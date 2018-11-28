#include <iostream>
using namespace std;

int dp[600][50], res[4], lt, ls;
char s[601], t[] = "welcome to code jam";
int solveDp(int i, int j){
	if(dp[i][j] != -1) return dp[i][j];
	dp[i][j] = 0;
	if(s[i] != t[j]) return dp[i][j];
	if(j == lt - 1) return dp[i][j] = 1;
	if(i >= ls - 1) return dp[i][j] = 0;
	for(int k = i + 1; k < ls; ++k){
		dp[i][j] += solveDp(k, j + 1);
		if(dp[i][j] >= 10000) dp[i][j] -= 10000;
	}
	return dp[i][j];
}

int main(){
	int cases;
	lt = strlen(t);
	freopen("D:\\C-large.in", "r", stdin);
	freopen("D:\\C.out", "w", stdout);
	scanf("%d", &cases);
	gets(s);
	for(int case_t = 1; case_t <= cases; ++case_t){
		gets(s);
		ls = strlen(s);
		memset(dp, -1, sizeof(dp));
		int sum = 0;
		for(int i = 0; i < ls; ++i){
			sum += solveDp(i, 0);
			if(sum >= 10000) sum -= 10000;
		}
		for(int i = 0; i < 4; ++i){
			res[i] = sum % 10;sum /= 10;
		}
		printf("Case #%d: ", case_t);
		for(int i = 3; i >= 0; --i) printf("%d", res[i]);
		putchar('\n');
	}
	return 0;
}