#include<stdio.h>
#include<string.h>

int dp[11][1<<10][11];
void chkmn(int &t, int a) {
	if(a<t) t=a;
}

int solve() {
	const int inf=1000000000;
	int P;
	scanf("%d", &P);
	for(int i=0;i<(1<<P);i++) {
		int t;
		scanf("%d", &t);
		for(int j=0;j<=t;j++)
			dp[P][i][j]=0;
		for(int j=t+1;j<=P;j++)
			dp[P][i][j]=inf;
	}
	for(int i=P-1;i>=0;i--) {
		for(int j=0;j<(1<<i);j++) {
			int *d1=dp[i+1][j*2], *d2=dp[i+1][j*2+1], price;
			scanf("%d", &price);
			dp[i][j][P]=d1[P]+d2[P]+price;
			chkmn(dp[i][j][P], inf);
			for(int k=P-1;k>=0;k--) {
				int r=dp[i][j][k+1];
				chkmn(r, d1[k+1]+d2[k+1]);
				chkmn(r, d1[k]+d2[k]+price);
				dp[i][j][k]=r;
			}
		}
	}
	return dp[0][0][0];
}

int main() {
	int T;
	scanf("%d", &T);
	for(int c=1;c<=T;c++) {
		printf("Case #%d: %d\n", c, solve());
	}
}