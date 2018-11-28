#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <queue>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int T;
long long L, t, N;
long long av[1000008];
double dp[1008][3];
long long cc[10000];
int C;

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.txt", "w", stdout);
	scanf("%d", &T);
	for(int vv = 1; vv <= T; ++vv) {
		scanf("%lld %lld %lld %d", &L, &t, &N, &C);
		for(int i = 0; i < C; ++i) {
			scanf("%lld", &cc[i]);
		}

		int start = 0;
		for(int i = 1; i <= N; ++i) {
			av[i] = cc[start++];
			start %= C;
		}

		memset(dp, 0, sizeof(dp));
		for(int i = 1; i <= N; ++i) {
			//dis = av[i];
			for(int k = 0; k <= L; ++k) {
				dp[i][k] = dp[i - 1][k] + av[i] * 2;
			}
			for(int k = 1; k <= L; ++k) {
				double tmp;
				if(dp[i - 1][k - 1] >= t) {
					tmp = dp[i - 1][k - 1] + av[i];
				} else {
					tmp = dp[i - 1][k - 1] + av[i]  + (t - dp[i - 1][k - 1]) * 1.0 / 2;
				}
				
				dp[i][k] = min(dp[i][k], tmp);
			}
		}

		double mins = 1000000000000000000LL;
		for(int i = 0; i <= L; ++i) {
			mins = min(mins, dp[N][i]);
		}

		printf("Case #%d: %lld\n", vv, (long long)(mins + 0.25));
		
	}
	return 0;
}