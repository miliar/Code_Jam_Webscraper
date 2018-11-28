// Adrian Kügel
#include <stdio.h>
#include <string.h>
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

int p[1<<10];
int miss[1<<10];
int memo[1<<10][11];
int n;

// m is number of missed matches so far
int solve(int round, int id, int m) {
	assert(id < (1<<n));
	if (round == 0) {
		int tid = id - (1<<(n-1));
		assert(tid >= 0 && tid < (1<<(n-1)));
		int m1 = miss[tid*2];
		int m2 = miss[tid*2+1];
		if (m > min(m1, m2))
			return INT_MAX;
		if (m < min(m1, m2))
			return 0;
		return p[id];
	}
	int &ret = memo[id][m];
	if (ret >= 0)
		return ret;
	// recursively evaluate subtrees
	long long s1 = solve(round-1, id*2, m);
	long long s2 = solve(round-1, id*2, m+1);
	long long s3 = solve(round-1, id*2+1, m);
	long long s4 = solve(round-1, id*2+1, m+1);
	ret = min((long long)INT_MAX, min(s2 + s4, s1 + s3 + p[id]));
	return ret;
}

int main() {
	int tc;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		int N;
		scanf("%d", &n);
		N = 1 << n;
		for (int i=0; i<N; ++i)
			scanf("%d", &miss[i]);
		for (int i=0; i<n; ++i) {
			int cn = 1 << (n - i - 1);
			for (int j=0; j<cn; ++j)
				scanf("%d", &p[cn+j]);
		}
		memset(memo, -1, sizeof(memo));
		printf("%d\n", solve(n-1, 1, 0));
	}
	return 0;
}
