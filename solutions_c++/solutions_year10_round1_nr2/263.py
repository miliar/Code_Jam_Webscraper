#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;
#define MAXN 300
#define MAXP 256
int N, ins, del, M;
int n[MAXN];
int dp[MAXN][MAXN];
bool isfind[MAXN][MAXN];

int DP(int x, int lastp){
	if(x >= N)
		return 0;
	if(isfind[x][lastp])
		return dp[x][lastp];

	dp[x][lastp] = INT_MAX;

	//change
	for(int i = 0;i < MAXP; i++){
		int v = abs(i - n[x]);

		if(abs(lastp - i) > M && M > 0){
			int in = (abs(lastp - i) / M);
			if(abs(lastp - i) % M == 0)in--;
				dp[x][lastp] = min(dp[x][lastp], DP(x + 1, i) + v +
						in * ins);
		}
		else if(abs(lastp - i) <= M)
			dp[x][lastp] = min(dp[x][lastp], DP(x + 1, i) + v);
	}

	//delete this
	dp[x][lastp] = min(dp[x][lastp], DP(x + 1, lastp) + del);

	//printf("%d %d = %d\n", x, lastp, dp[x][lastp]);
	isfind[x][lastp] = true;
	return dp[x][lastp];
}

int main(){
	int ca = 1, cases;

	freopen("test", "r", stdin);
	freopen("out", "w", stdout);
	scanf("%d", &cases);
	while(cases--){
		memset(n, 0, sizeof(n));
		memset(isfind, 0, sizeof(isfind));
		scanf("%d%d%d%d", &del, &ins, &M, &N);
		for(int i = 0;i < N; i++)
			scanf("%d", &n[i]);

		int ans = INT_MAX;
		for(int i = 0;i < MAXP; i++)
			ans = min(ans, DP(0, i));


		printf("Case #%d: %d\n", ca++, ans);

	}
	return 0;
}
