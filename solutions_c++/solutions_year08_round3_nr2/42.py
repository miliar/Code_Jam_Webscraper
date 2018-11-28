#include <stdio.h>
#include <string.h>

const int N = 50;

typedef long long LL;

LL dp[N][2][3][5][7];
int mod[N][N][4];
int x[4] = {2, 3, 5, 7};

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.txt", "w", stdout);

	int ntc, tc = 0;
	scanf("%d", &ntc);
	char w[50];
	while(ntc--) {
		printf("Case #%d: ", ++tc);
		scanf("%s", w);
		int n = strlen(w), i, j, k, a, b, c;

		for(i = 0; i < n; ++i) {
			for(j = i+1; j <= n; ++j) {
				int ans[4] = {0};
				for(k = i; k < j; ++k) {
					for(a = 0; a < 4; ++a) {
						ans[a] *= 10;
						ans[a] += w[k]-'0';
						ans[a] %= x[a];
					}
				}
				for(a = 0; a < 4; ++a) {
					mod[i][j][a] = ans[a];
				}
			}
		}

		memset(dp, 0, sizeof(dp));
		dp[0][0][0][0][0] = 1;
		for(i = 0; i <= n; ++i) {
			for(j = 0; j < 2; ++j) {
				for(k = 0; k < 3; ++k) {
					for(a = 0; a < 5; ++a) {
						for(b = 0; b < 7; ++b) if(dp[i][j][k][a][b] != 0) {
							for(c = i+1; c <= n; ++c) {
								int jj = (mod[i][c][0] + j)%2;
								int kk = (mod[i][c][1] + k)%3;
								int aa = (mod[i][c][2] + a)%5;
								int bb = (mod[i][c][3] + b)%7;
								dp[c][jj][kk][aa][bb] += dp[i][j][k][a][b];

								if(i != 0) {
									int jjj = ((j-mod[i][c][0])%2+2)%2;
									int kkk = ((k-mod[i][c][1])%3+3)%3;
									int aaa = ((a-mod[i][c][2])%5+5)%5;
									int bbb = ((b-mod[i][c][3])%7+7)%7;
									dp[c][jjj][kkk][aaa][bbb] += dp[i][j][k][a][b];
								}
							}
							if(dp[i][j][k][a][b] < 0) {
								printf("dp[%d][%d][%d][%d][%d] = %d\n", i, j, k, a, b, dp[i][j][k][a][b]);
							}
						}
					}
				}
			}
		}

		LL ans = 0;
		for(i = 0; i < 2; ++i) {
			for(j = 0; j < 3; ++j) {
				for(k = 0; k < 5; ++k) {
					for(a = 0; a < 7; ++a) {
						if(i == 0 || j == 0 || k == 0 || a == 0) {
							ans += dp[n][i][j][k][a];
							if(ans < 0) while(1) printf("!");
						}
					}
				}
			}
		}
		printf("%I64d\n", ans);
	}
	return 0;
}
