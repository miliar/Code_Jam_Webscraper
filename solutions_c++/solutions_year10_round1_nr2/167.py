#include<stdio.h>
#include<algorithm>
#include<string.h>

void chkmn(int &t, int v) {
	if(v<t) t=v;
}

int dp[2][256];
int solve() {
	int a=0, D, I, M, N;
	memset(dp[0], 0, sizeof(dp[0]));
	scanf("%d%d%d%d", &D, &I, &M, &N);
	for(int i=0;i<N;i++) {
		int v;
		scanf("%d", &v);
		for(int j=0;j<256;j++)
			dp[!a][j]=dp[a][j]+D;

		for(int j=0;j<256;j++) {
			for(int k=0;k<256;k++) {
				if(std::abs(j-k)<=M)
					chkmn(dp[!a][k], dp[a][j]+std::abs(v-k));
			}
		}
		a=!a;
		if(M) {
			for(int j=0;j<256;j++) {
				for(int k=0;k<256;k++) {
					int dif=std::abs(k-j);
					chkmn(dp[a][k], dp[a][j]+(dif+M-1)/M*I);
				}
			}
		}
	}

	int mn=10000000;
	for(int i=0;i<256;i++)
		chkmn(mn, dp[a][i]);
	return mn;
}

int main() {
	int t;
	scanf("%d", &t);
	for(int i=1;i<=t;i++)
		printf("Case #%d: %d\n", i, solve());
}