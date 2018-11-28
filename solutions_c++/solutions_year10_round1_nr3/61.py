#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
#include <set>
#include <map>

using namespace std;

const int MAXN = 1000005;
int A1, A2, B1, B2, T;

int dp[MAXN];

inline bool good(int x, int y) {
	if (x == y) {return false;}
	if (x > y) {swap(x, y);}
	return (y >= dp[x]);
}

inline void init() {
	dp[1] = 2;
	dp[2] = 4;
	dp[3] = 5;
	dp[4] = 7;
	for(int i = 5 ; i < MAXN ; i++) {
		int v = dp[i - 1];
		while (good(v - i, i)) {
			v++;
		}
		dp[i] = v;
	}
}

int main() {
	init();
	scanf("%d",&T);
	for(int t = 1 ; t <= T ; t++) {
		scanf("%d %d %d %d",&A1,&A2,&B1,&B2);
		long long ans = 0;
		for(int i = A1 ; i <= A2 ; i++) {
			int lo = max(max(i + 1, B1), dp[i]);
			int hi = B2;
			if (lo <= hi) {
				ans += (hi - lo + 1);
			}
		}
		for(int i = B1 ; i <= B2 ; i++) {
			int lo = max(max(i + 1, A1), dp[i]);
			int hi = A2;
			if (lo <= hi) {
				ans += (hi - lo + 1);
			}
		}
		printf("Case #%d: %lld\n",t,ans);
	}
	return 0;
}
