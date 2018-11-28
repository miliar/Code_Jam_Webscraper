#include <stdio.h>
#include <string.h>

int a[100];
int dp[101][257];

int inline abs(int x){
	return x>0?x:-x;
}

int main(){
	int T;
	scanf("%d", &T);
	for (int ttt = 1; ttt <= T; ttt++){
		memset(dp, 127, sizeof(dp));
		int D, I, M, N;
		scanf("%d%d%d%d", &D, &I, &M, &N);
		for (int i = 0; i < N; i++){
			scanf("%d", a + i);
		}
		dp[0][256] = 0;
		for (int j = 0; j < 256; j++) dp[0][j] = I;
		for (int i = 1; i <= N; i++){
			dp[i][256] = dp[i-1][256] + D;
			for (int j = 0; j < 256; j++){
				//delete
				dp[i][j] = dp[i-1][j] + D;
				//keep & change value
				for (int v = 0; v < 256; v++){
					int mincost = dp[i-1][v];
					for (int m = 1; m <= M; m++){
						if (v-m>=0 && dp[i-1][v-m] < mincost)
							mincost = dp[i-1][v-m];
						if (v+m<256 && dp[i-1][v+m] < mincost)
							mincost = dp[i-1][v+m];
					}
					if (mincost > dp[i-1][256])
						mincost = dp[i-1][256];
					mincost += abs(v - a[i-1]);
					//insert from v to j
					int d = abs(v - j);
					if (d > 0){
						if (M == 0) continue;
						d = (d-1)/M + 1;
					}
					mincost += d * I;
					if (dp[i][j] > mincost) dp[i][j] = mincost;
				}
			}
		}
		int ret = dp[N][0];
		for (int j = 1; j < 257; j++){
			if (ret > dp[N][j]) ret = dp[N][j];
		}
		printf("Case #%d: %d\n", ttt, ret);
	}
	return 0;
}