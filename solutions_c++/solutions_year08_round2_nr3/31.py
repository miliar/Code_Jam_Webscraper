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

int ost[1<<21], offset;
int ans[1<<20];

int rank(int p) {
	p += offset;
	int r = 0;
	while(p>1) {
		if (p&1)
			r += ost[p-1];
		p >>= 1;
	}
	return r;
}

int sel(int p) {
	int r = 1;
	while(r < offset) {
		r *= 2;
		if (ost[r] < p) {
			p -= ost[r];
			++r;
		}
	}
	assert(p == 1);
	assert(ost[r] == 1);
	return r-offset;
}

int main() {
	int tc;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d:", scen);
		int k, n;
		scanf("%d %d", &k, &n);
		for (offset=1; offset<k; offset<<=1);
		memset(ost, 0, sizeof(int)*offset*2);
		memset(ans, 0, sizeof(int) * k);
		for (int i=0; i<k; ++i)
			ost[i+offset] = 1;
		for (int i=offset-1; i>0; --i)
			ost[i] = ost[i*2]+ost[i*2+1];
		int pos = 0;
		for (int i=1; i<=k; ++i) {
			assert(ans[pos] == 0);
//			printf("%d %d\n", pos, i);
			ans[pos] = i;
			if (i == k)
				break;
			int p = pos + offset;
			while(p) {
				--ost[p];
				p >>= 1;
			}
			int cur = rank(pos);
			assert(ost[1] == k-i);
			// total rank = i
			int rem = (i+1)%(k-i);
			rem += cur;
			rem %= (k-i);
			if (!rem)
				rem += k - i;
			assert(rem >= 1 && rem <= k-i);
//			if (rem <= i)
				pos = sel(rem);
/*			else {
				rem -= i;
				if (rem < 1)
					rem += k-i;
				assert(rem >= 1 && rem <= k-i);
				pos = sel(rem);
			}*/
		}
		for (int i=0; i<n; ++i) {
			int di;
			scanf("%d", &di);
			printf(" %d", ans[di-1]);
		}
		puts("");
	}
	return 0;
}
