#include <iostream>
#include <string>
#include <cstring>
using namespace std;
#define MOD 10000
#define GI ({int t; scanf("%d\n",&t); t;})
char str[]="welcome to code jam";
int dp[501][25];
char inp[510];
int main() {
  int t = GI;
  int len = strlen(str);
  dp[0][0] = 1;
  for (int cas = 1 ; cas <= t; cas++) {
    cin.getline(inp,510);
    int k = strlen(inp);
    for (int i = 1; i <= k; i++) {
      for (int j = 0; j <= len; j++) {
	dp[i][j] = dp[i-1][j];
	if (j && inp[i-1] == str[j-1]) {
	  dp[i][j] += dp[i-1][j-1];
	  dp[i][j] %= MOD;
	}
      }
    }
    /*printf("%d ",dp[7][1]);
    for (int j = 2; j <= len; j++) {
      cout << dp[j][j+7] << " ";
      }
      cout << endl;*/
    printf("Case #%d: %0.4d\n",cas,dp[k][len]);
  }
  
}
