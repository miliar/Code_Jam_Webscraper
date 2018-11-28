#include <cstdio>
#include <cstring>
using namespace std;

char str[1000];
int dp[1000][19];

int main()
{
	int N;

	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	scanf("%d", &N);
	gets(str);
	for (int n = 1; n <= N; ++n) {
		memset(dp, 0, sizeof(dp));
		gets(str);
		dp[0][0] = (str[0] == 'w') ? 1 : 0;
		int i;
		for (i = 1; str[i]; ++i) {
			for (int j = 0; j < 19; ++j)
				dp[i][j] = dp[i - 1][j];
			switch(str[i]) {
				case 'w':
					dp[i][0] = (dp[i][0] + 1) % 10000;
					break;
				case 'e':
					dp[i][1] = (dp[i][1] + dp[i][0]) % 10000;
					dp[i][6] = (dp[i][6] + dp[i][5]) % 10000;
					dp[i][14] = (dp[i][14] + dp[i][13]) % 10000;
					break;
				case 'l':
					dp[i][2] = (dp[i][2] + dp[i][1]) % 10000;
					break;
				case 'c':
					dp[i][3] = (dp[i][3] + dp[i][2]) % 10000;
					dp[i][11] = (dp[i][11] + dp[i][10]) % 10000;
					break;
				case 'o':
					dp[i][4] = (dp[i][4] + dp[i][3]) % 10000;
					dp[i][9] = (dp[i][9] + dp[i][8]) % 10000;
					dp[i][12] = (dp[i][12] + dp[i][11]) % 10000;
					break;
				case 'm':
					dp[i][5] = (dp[i][5] + dp[i][4]) % 10000;
					dp[i][18] = (dp[i][18] + dp[i][17]) % 10000;
					break;
				case ' ':
					dp[i][7] = (dp[i][7] + dp[i][6]) % 10000;
					dp[i][10] = (dp[i][10] + dp[i][9]) % 10000;
					dp[i][15] = (dp[i][15] + dp[i][14]) % 10000;
					break;
				case 't':
					dp[i][8] = (dp[i][8] + dp[i][7]) % 10000;
					break;
				case 'd':
					dp[i][13] = (dp[i][13] + dp[i][12]) % 10000;
					break;
				case 'j':
					dp[i][16] = (dp[i][16] + dp[i][15]) % 10000;
					break;
				case 'a':
					dp[i][17] = (dp[i][17] + dp[i][16]) % 10000;
					break;
			}
		}
		printf("Case #%d: %04d\n", n, dp[i - 1][18]);
	}
	return 0;
}