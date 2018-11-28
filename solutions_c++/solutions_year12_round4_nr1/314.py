#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int t;
	
	scanf("%d", &t);
	
	for(int time = 1; time <= t; ++time) {
		
		int n, dist, d[10000], l[10000];
		
		scanf("%d", &n);
		for(int i = 0; i < n; ++i)
			scanf("%d%d", d + i, l + i);
		scanf("%d", &dist);
		
		bool ans = false;
		int dp[10000] = {0};
		
		dp[0] = d[0];
		
		for(int i = 0; i < n; ++i) {
		
			for(int j = i + 1; j < n && d[i] + dp[i] >= d[j]; ++j) {
			
				dp[j] = max(dp[j], min(d[j] - d[i], l[j]));
			}
			
			//printf("[Debug] %d -> %d\n", i, dp[i]);
		
			if(d[i] + dp[i] >= dist)
				ans = true;
		}
		
		printf("Case #%d: %s\n", time, ans ? "YES" : "NO");
	
	}
	
	return 0;
}