#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <valarray>
#include <algorithm>
#include <functional>
#include <numeric>
#include <complex>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
using namespace std;

typedef long long LL;
const int MAXN = 1000000;
LL dp[MAXN];
int a[105];
const LL INF = 1000000000000000005LL;

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		LL len;
		int n;
		scanf("%lld %d", &len, &n);
		for (int i = 0; i < n; ++i)
			scanf("%d", &a[i]);
		memset(dp, -1, sizeof(dp));
		dp[0] = 0;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < MAXN - a[i]; ++j) {
				int k = j + a[i];
				if (dp[j] == -1)
					continue;
				if (dp[k] == -1)
					dp[k] = dp[j] + 1;
				else
					dp[k] = min(dp[k], dp[j] + 1);
			}
		}
		LL res = INF;
		for (int i = 0; i < MAXN; ++i) {
			if (dp[i] == -1)
				continue;
			LL tmp = dp[i];
			for (int j = 0; j < n; ++j) {
				if ((len - i) % a[j] == 0)
					res = min(res, tmp + (len - i) / a[j]);
			}
		}
		printf("Case #%d: ", t);
		if (res == INF) {
			puts("IMPOSSIBLE");
		}
		else
			printf("%lld\n", res);
	}
	return 0;
}