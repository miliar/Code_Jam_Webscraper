#include <iostream>
#include <string>
#include <map>
using namespace std;

const int N = 505, M = 25;
char text[N], pattern[M] = "welcome to code jam";
int dp[N][M];

const int MOD = 1000;

int main(int argc, char** argv){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cas;
	scanf("%d", &cas);
	gets(text);
	for(int cs = 1; cs <= cas; ++cs){
		gets(text);
		memset(dp, 0, sizeof(dp));
		int n = strlen(text);
		int m = strlen(pattern);
		dp[0][0] = text[0] == pattern[0];
		for(int i = 1; i < n; ++i){
			for(int j = 0; j < m && j <= i; ++j){
				dp[i][j] = dp[i - 1][j];
				if(text[i] == pattern[j]){
					dp[i][j] += j ? dp[i - 1][j - 1] : 1;
					if(dp[i][j] >= MOD)
						dp[i][j] -= MOD;
				}

			}
		}
		printf("Case #%d: %04d\n", cs, dp[n - 1][m - 1]);
	}
	return 0;
}