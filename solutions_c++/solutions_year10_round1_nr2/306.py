#include <stdio.h>
#include <string.h>
int dp[110][256], tmp[256];
int val[110];
int D, I, M, n;

int abs(int x) {
	return x>0?x:-x;
}

int need(int x, int y) {
	if (M == 0) {
		if (x==y) return 0; else
		return -1;
	} else {
		return (abs(x-y)-1)/M*I;
	}
}

int main() {
	int ca, cases = 0;
	int i, j, k, l;
	scanf("%d", &ca);
	while (ca--) {
		printf("Case #%d: ", ++cases);
		scanf("%d%d%d%d", &D, &I, &M, &n);
		for (i=0;i<n;++i) {
			scanf("%d", &val[i]);
		}
		for (i=0;i<256;++i) {
			dp[0][i] = 0;
		}
		for (i=1;i<=n;++i) {
			for (j=0;j<256;++j) {
				dp[i][j] = dp[i-1][j]+D;
				for (k=0;k<256;++k) {
					if (need(k, j) == -1) continue;
					if (dp[i][j] > dp[i-1][k]+abs(val[i-1]-j)+need(k,j))
						dp[i][j] = dp[i-1][k]+abs(val[i-1]-j)+need(k,j);
				}
			}
			
			// for (j=0;j<256;++j) {
				// for (k=0;k<256;++k) {
					// if (need(k,j)==-1) continue;
					// int cost = need(k,j) + abs(val[i-1]-k);
					// int minn = 0x3fffffff;
					// for (l=0;l<256;++l) if (abs(l-k)<=M && dp[i-1][l] < minn) {
						// minn = dp[i-1][l];
					// }
					// if (cost + minn < dp[i][j]) {
						// dp[i][j] = cost + minn;
					// }
				// }
			// }
		}
		int minn = 0x3fffffff;
		for (i=0;i<256;++i) {
			if (dp[n][i] < minn) minn = dp[n][i];
		}
		printf("%d\n", minn);
	}
	return 0;
}
