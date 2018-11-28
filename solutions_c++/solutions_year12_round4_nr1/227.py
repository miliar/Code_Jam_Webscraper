#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>
#include <string>

using namespace std;

typedef long long ll;

int d[10010], l[10010];
int dp[10010];

int main() {
	int T;
	cin >> T;
	for(int c = 1; c <= T; ++c) {
		int n;
		cin >> n;
		for(int i = 0; i < n; ++i) cin >> d[i] >> l[i];
		cin >> d[n];
		l[n] = 0;
		for(int i = 0; i <= n; ++i) dp[i] = -1;
		dp[0] = d[0];
		for(int i = 0; i < n; ++i) if(dp[i] != -1) {
			for(int j = i + 1; j <= n && d[j] <= d[i] + dp[i]; ++j) {
				dp[j] = max(dp[j], min(d[j] - d[i], l[j]));
			}
		}
		printf("Case #%d: ", c);
		if(dp[n] != -1) puts("YES");
		else puts("NO");
	}
	return 0;
}
