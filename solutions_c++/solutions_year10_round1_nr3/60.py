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
typedef pair<int, int> PII;

map<PII, bool> memo;

int loss_range[1000001][2];

bool eval(int a, int b) {
	if (!a || !b)
		return true;
	if (b >= loss_range[a][0] && b <= loss_range[a][1])
		return false;
	if (a >= loss_range[b][0] && a <= loss_range[b][1])
		return false;
	return true;
}

int main() {
	int tc, a1, a2, b1, b2;
	loss_range[1][0] = loss_range[1][1] = 1;
	int cur_lo = 1;
	for (int i=2; i<=1000000; ++i) {
		if (!eval(i - cur_lo, cur_lo)) {
			++cur_lo;
			assert(eval(i - cur_lo, cur_lo));
		}
		loss_range[i][0] = cur_lo;
		loss_range[i][1] = cur_lo + i - 1;
	}
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		scanf("%d %d %d %d", &a1, &a2, &b1, &b2);
		assert(a1 <= a2 && b1 <= b2);
		long long res = (a2-a1+1LL)*(b2-b1+1LL);
		for (int i=a1; i<=a2; ++i) {
			long long t1 = max(loss_range[i][0], b1);
			long long t2 = min(loss_range[i][1], b2);
			if (t1 <= t2)
				res -= (t2 - t1 + 1);
		}
		printf("%lld\n", res);
	}
	return 0;
}
