#include<cstdio>
#include<cstring>
#include<vector>
#include<string>
#include<algorithm>
#include<queue>

using namespace std;

int main(){
	int T;
	scanf("%d", &T);
	for (int cc = 1; cc <= T; ++cc){
		printf("Case #%d: ", cc);
		int M, V;
		scanf("%d%d", &M, &V);
		int typ[M+1], can[M+1];
		int dp[M+1][2];
		for (int i = 1 ; i <= (M-1)/2; ++i)
			scanf("%d%d", typ+i, can+i);
		memset(dp, 0, sizeof(dp));
		for (int i = 0 ; i <= M; ++i) dp[i][0] = dp[i][1] = (1<<29);
		for (int i = (M-1)/2+1; i <= M; ++i){
			int j;
			scanf("%d", &j);
			dp[i][j] = 0;
		}
		for (int i = (M-1)/2; i; --i){
			int x = i*2, y = i*2+1;
			if (!can[i]){
				int x0 = dp[x][0], x1 = dp[x][1], y0 = dp[y][0], y1 = dp[y][1];
				if (typ[i]){ // AND
					dp[i][0] = min(dp[i][0], x0+y0);
					dp[i][0] = min(dp[i][0], x0+y1);
					dp[i][0] = min(dp[i][0], x1+y0);
					dp[i][1] = min(dp[i][1], x1+y1);
				}else{ //OR
					dp[i][0] = min(dp[i][0], x0+y0);
					dp[i][1] = min(dp[i][1], x0+y1);
					dp[i][1] = min(dp[i][1], x1+y0);
					dp[i][1] = min(dp[i][1], x1+y1);
				}
			}else{
				int x0 = dp[x][0], x1 = dp[x][1], y0 = dp[y][0], y1 = dp[y][1];
				if (typ[i]){ // AND
					dp[i][0] = min(dp[i][0], x0+y0);
					dp[i][0] = min(dp[i][0], x0+y1);
					dp[i][0] = min(dp[i][0], x1+y0);
					dp[i][1] = min(dp[i][1], x1+y1);
					dp[i][0] = min(dp[i][0], x0+y0+1);
					dp[i][1] = min(dp[i][1], x0+y1+1);
					dp[i][1] = min(dp[i][1], x1+y0+1);
					dp[i][1] = min(dp[i][1], x1+y1+1);
				}else{ //OR
					dp[i][0] = min(dp[i][0], x0+y0+1);
					dp[i][0] = min(dp[i][0], x0+y1+1);
					dp[i][0] = min(dp[i][0], x1+y0+1);
					dp[i][1] = min(dp[i][1], x1+y1+1);
					dp[i][0] = min(dp[i][0], x0+y0);
					dp[i][1] = min(dp[i][1], x0+y1);
					dp[i][1] = min(dp[i][1], x1+y0);
					dp[i][1] = min(dp[i][1], x1+y1);
				}
			}
		}
		if (dp[1][V] == (1<<29)) printf("IMPOSSIBLE\n");
		else printf("%d\n", dp[1][V]);
	}
	return 0;
}
