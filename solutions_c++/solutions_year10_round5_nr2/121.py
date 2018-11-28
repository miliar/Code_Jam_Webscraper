// Adrian Kügel
#include <stdio.h>
#include <vector>
#include <set>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <map>
#include <assert.h>
#include <limits.h>
#include <complex>
#include <algorithm>
#include <ctype.h>
#include <string>
#include <string.h>
using namespace std;

typedef set<int> SI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef complex<double> tComp;
typedef pair<short, int> PCI;

int b[100];

long long dp[110000];

void update(long long &a, long long b) {
	if (a < 0 || a > b)
		a = b;
}

int main() {
	int tc;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		long long l;
		int n;
		scanf("%lld %d", &l, &n);
		for (int i=0; i<n; ++i)
			scanf("%d", &b[i]);
		long long best = -1;
		for (int i=0; i<n; ++i) {
			int want = l % b[i];
			int add = min(l, 100000LL) / b[i];
			assert(l / b[i] - add >= 0);
			want += add * b[i];
			memset(dp, -1, sizeof(dp));
			dp[0] = 0;
			for (int j=0; j<n; ++j)
				for (int k=b[j]; k<=want; ++k)
					if (dp[k-b[j]] >= 0)
						update(dp[k], dp[k-b[j]] + 1);
			if (dp[want] >= 0)
				update(best, dp[want] + l / b[i] - add);
		}
		if (best < 0)
			puts("IMPOSSIBLE");
		else
			printf("%lld\n", best);
	}
	return 0;
}
