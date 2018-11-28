#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

bool dp[31][11][2];
bool not[31][11][2];

int N, T, S, p, val[100];
int dp2[101][101];

int main() {
	//3 2 9 14 6 30
	freopen("B-small.in", "r", stdin);
	freopen("Ans.txt", "w", stdout);
	memset(dp, false, sizeof(dp));
	memset(not, false, sizeof(not));

	for(int i = 0; i <= 10; ++i) {
		for(int j = 0; j <= 10; ++j) {
			for(int k = 0; k <= 10; ++k) {
				int sum = i + j + k;
				int t = max(i, max(j, k));
				bool sup = false;

				int t1 = abs(i - j);
				t1 = max(t1, abs(j - k));
				t1 = max(t1, abs(k - i));
				if(t1 > 2) continue;

				if(abs(i - j) == 2 || abs(j - k) == 2 || abs(k - i) == 2) {
					sup = true;
				}
				if(sup) {
					for(int v = t + 1; v <= 10; ++v) {
						not[sum][v][1] = true;
					} 
				}else {
					for(int v = t + 1; v <= 10; ++v) {
						not[sum][v][0] = true;
					}
				}

				for(int v = 0; v <= t; ++v) {
					if(sup)
						dp[sum][v][1] = true;
					else
						dp[sum][v][0] = true;
				}
			}
		}
	}

	scanf("%d", &N);
	for(int ca = 1; ca <= N; ++ca) {
		scanf("%d %d %d", &T, &S, &p);
		for(int i = 0; i < T; ++i) {
			scanf("%d", &val[i]);
		}
		memset(dp2, 0, sizeof(dp2));
		for(int i = 0; i < T; ++i) {
			if(i == 0) {
				if(dp[val[i]][p][0]) dp2[0][0] = 1;
				if(dp[val[i]][p][1] && S != 0) dp2[0][1] = 1;
			} else {
				if(not[val[i]][p][0]) {
					for(int j = 0; j <= S; ++j) {
						dp2[i][j] = dp2[i - 1][j];
					}
				}
				if(not[val[i]][p][1]) {
					for(int j = 1; j <= S; ++j) {
						dp2[i][j] = max(dp2[i][j], dp2[i - 1][j - 1]);
					}
				}
				if(dp[val[i]][p][0]) {
					for(int j = 0; j <= S; ++j) {	
						dp2[i][j] = max(dp2[i][j], dp2[i - 1][j] + 1);
					}
				}
				if(dp[val[i]][p][1]) {
					for(int j = 1; j <= S; ++j) {
						dp2[i][j] = max(dp2[i][j], dp2[i - 1][j - 1] + 1);
					}
				}

			}
		}
		printf("Case #%d: %d\n", ca, dp2[T - 1][S]);
	}
	return 0;
}