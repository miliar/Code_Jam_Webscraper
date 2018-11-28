#include <iostream>
using namespace std;

int main() {
	int ntc;
	
	scanf("%d", &ntc);
	
	for (int tc = 1; tc <= ntc; ++tc) {
		int l, t, n;
		int c;
		
		scanf("%d %d %d", &l, &t, &n);
		int dis[n];
		int a[n];
		
		scanf("%d", &c);
		
		for (int i = 0; i < c; ++i)
			scanf("%d", &a[i]);
		
		for (int i = 0; i < n; ++i) {
			dis[i] = a[i % c];
		}
		
		int dp[n + 1][3];
		
		for (int i = 0; i < n; ++i) {
			dp[i][0] = 2147483647;
			dp[i][1] = 2147483647;
			dp[i][3] = 2147483647;
		}
		
		dp[0][0] = 0;
		for (int i = 1; i <= n; ++i){
			for (int j = 0; j <= l; ++j) {
				long long gaPake = (long long)dp[i - 1][j] + (long long)dis[i - 1] * 2LL;
				long long pake = 2147483647;
				if (j > 0) {
					if (dp[i - 1][j - 1] > t)
						pake = (long long)dp[i - 1][j - 1] + (long long)dis[i - 1];
					else {
						int sisa = t - (long long)dp[i - 1][j - 1];
						pake = (long long)dp[i - 1][j - 1] + (long long)dis[i - 1] - (sisa / 2) + sisa;
					}
				}
					
				dp[i][j] = min(gaPake, pake);
			}
		}
		
		int minim = 2147483647;
		
		for (int i = 0; i <= l; ++i) {
			minim = min(minim, dp[n][i]);
		}
		
		printf("Case #%d: %d\n", tc, minim);
	}
	
	return 0;
}