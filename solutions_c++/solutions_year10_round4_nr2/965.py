#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
int m[1024], c[1024], mk[2048];
int dp[2048][10];
int p;

int main() {
	int ca, cases = 0;
	int i, j, k;
	scanf("%d", &ca);
	while (ca--) {
		printf("Case #%d: ", ++cases);
		scanf("%d", &p);
		memset(dp, -1, sizeof(dp));

		for (i=0;i<(1<<p);++i) {
			scanf("%d", &m[i]);			
			mk[i + (1<<p) - 1] = m[i];
			for (j=0;j<=m[i];++j)
				dp[i + (1<<p) - 1][j] = 0;
		}
		for (i = p-1; i >=0 ; --i) {
			for (j = 0; j < (1<<i); ++j) {
				k = (1 << i) - 1 + j;
				scanf("%d", &c[k]);
				mk[k] = 1000;
			}
		}
		
		for (i=(1<<p)-2;i>=0;--i) {
			mk[i] = min(mk[i*2+1], mk[i*2+2]);
		}
		
		
		int minn = 0x3fffffff;
		for (i=(1<<p)-2; i>=0 ; --i) {
			for (j=0;j<=mk[i];++j) {
				// miss myself
				int minl = 0x3fffffff;
				int minr = 0x3fffffff;
				for (k =j+1; k <= mk[i*2+1]; ++k) {
					if (dp[i*2+1][k] < minl && dp[i*2+1][k] != -1) minl = dp[i*2+1][k];
				}
				for (k =j+1; k <= mk[i*2+2]; ++k) {
					if (dp[i*2+2][k] < minr && dp[i*2+2][k] != -1) minr = dp[i*2+2][k];
				}
				// printf("-%d:%d %d %d\n", i, j, minl, minr);
				if (minl < 0x3fffffff && minr < 0x3fffffff && (dp[i][j] == -1 || dp[i][j] > minl+minr)) {
					dp[i][j] = minl + minr;
				}
				// use myself
				if (dp[i*2+1][j] < minl && dp[i*2+1][j] != -1) minl = dp[i*2+1][j];
				if (dp[i*2+2][j] < minr && dp[i*2+2][j] != -1) minr = dp[i*2+2][j];
				// printf("-%d:%d %d %d\n", i, j, minl, minr);
				if (minl < 0x3fffffff && minr < 0x3fffffff && (dp[i][j] == -1 || dp[i][j] > minl+minr+c[i])) {
					dp[i][j] = minl + minr + c[i];
				}
				// printf("dp[%d][%d] = %d\n", i, j, dp[i][j]);
				
				if (i == 0 && dp[i][j] != -1 && dp[i][j] < minn)
					minn = dp[i][j];
			}
		}
		printf("%d\n", minn);
	}
	return 0;
}