#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <cmath>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
const int inf=(1<<30);
#define mset(a,x) memset(a,x,sizeof(a))
#define ABS(a) ((a) >= 0 ? (a) : -(a))
#define dbg(x) cerr<<#x<<" : "<<x<<endl
int n;
int dp[505][25];
char str[505];

int main() 
{
	freopen("C-large.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int T;
	int cnt=0;
	scanf("%d", &T);
	getchar();
	while (T--) {
	       gets(str);
		   n = strlen(str);
		   mset(dp, 0);
		   for (int i = 1; i <= n; i++) {
		        for (int j = 1; j <= 19; j++)
					 dp[i][j] += dp[i-1][j];
				if (str[i-1] == 'w') {
				    dp[i][1]++;
				}
				if (str[i-1] == 'e') {
				    dp[i][2] += dp[i-1][1];
					dp[i][7] += dp[i-1][6];
					dp[i][15] += dp[i-1][14];
				}
				if (str[i-1] == 'l') {
				    dp[i][3] += dp[i-1][2];
				}
				if (str[i-1] == 'c') {
				    dp[i][4] += dp[i-1][3];
					dp[i][12] += dp[i-1][11];
				}
				if (str[i-1] == 'o') {
				    dp[i][5] += dp[i-1][4];
					dp[i][10] += dp[i-1][9];
					dp[i][13] += dp[i-1][12];
				}
				if (str[i-1] == 'm') {
				    dp[i][6] += dp[i-1][5];
					dp[i][19] += dp[i-1][18];
				}
				if (str[i-1] == ' ') {
				    dp[i][8] += dp[i-1][7];
					dp[i][11] += dp[i-1][10];
					dp[i][16] += dp[i-1][15];
				}
				if (str[i-1] == 't') {
				    dp[i][9] += dp[i-1][8];
				}
				if (str[i-1] == 'd') {
					dp[i][14] += dp[i-1][13];
				}
				if (str[i-1] == 'j') {
				    dp[i][17] += dp[i-1][16];
				}
				if (str[i-1] == 'a') {
				    dp[i][18] += dp[i-1][17];
				}
				for (int j = 1; j <= 19; j++) {
					 //printf("dp[%d][%d]=%d\n", i, j, dp[i][j]);
					 //system("pause");
					 dp[i][j] %= 10000;
				}
				//res %= 10000;
		   }
		   printf("Case #%d: %04d\n", ++cnt, dp[n][19]);
	}

    return 0;
}
