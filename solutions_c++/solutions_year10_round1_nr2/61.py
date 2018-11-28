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
using namespace std;

typedef set<int> SI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef complex<double> tComp;
typedef pair<short, int> PCI;

int dp[128][256];
int a[128];
int M, I;

int make_smooth(int diff) {
	if (diff <= M)
		return 0;
	if (M == 0)
		return 1000000000;
	return ((diff - 1) / M) * I;
}

int main() {
	int tc, d, n;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		scanf("%d %d %d %d", &d, &I, &M, &n);
		int best = d * n;
		for (int i=0; i<n; ++i) {
			scanf("%d", &a[i]);
			for (int j=0; j<256; ++j) {
				dp[i][j] = abs(j - a[i]);
				int mv = i * d;
				for (int ii=0; ii<i; ++ii) {
					for (int k=0; k<256; ++k) {
						int t = (i - ii - 1) * d + dp[ii][k] + make_smooth(abs(k-j));
						if (t < mv)
							mv = t;
					}
				}
				dp[i][j] += mv;
				best = min(best, dp[i][j] + (n-i-1) * d);
			}
		}
		printf("%d\n", best);
	}
	return 0;
}
