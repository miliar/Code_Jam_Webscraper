#include <iostream>
#include <cstdio>

using namespace std;

int dp[35];

int main() {
	
	for (int i = 1; i <= 31; i++)
		dp[i] = (dp[i-1] << 1) + 1;\
	
	int t, n, k;
	
	scanf("%d", &t);
	
	for (int i = 1; i <= t; i++) {
		scanf("%d %d", &n, &k);
		
		printf("Case #%d: ", i);
		if (k % (dp[n] + 1) == dp[n])
			printf("ON\n");
		else
			printf("OFF\n");
	}
	
	return 0;
	
}