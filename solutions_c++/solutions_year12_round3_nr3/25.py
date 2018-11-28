#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <vector>
#include <map>

#define mp make_pair
#define f first
#define s second

using namespace std;

typedef long long lld;

vector<pair<lld, lld> > a, b;
map<lld, lld> cache[123][123];

void initIO() {
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("out.txt", "w", stdout);
}

int n, m;

lld dp(int ni, int mi, lld left) {
	if (ni == n) return 0;
	map<lld, lld>::iterator it = cache[ni][mi].upper_bound(left);
	if (cache[ni][mi].size() && it != cache[ni][mi].begin()) {
		return (--it)->second;
	}
	lld ret = 0;
	lld runtot = 0, remain = a[ni].s;
	if (a[ni].f == b[mi].f) {
		runtot += min(left, a[ni].s);
		remain -= min(left, a[ni].s);
		ret = dp(ni+1, mi, left-min(left, a[ni].s)) + runtot;
	}
	else {
		ret = dp(ni+1, mi, left);
	}

	for (int i=mi+1; i<m; i++) {
		lld minus = 0;
		if (a[ni].f == b[i].f) {
			minus = min(b[i].s, remain);
			runtot += minus;
			remain -= minus;
		}
		ret = max(ret, dp(ni+1, i, b[i].s-minus)+runtot);
	}
	//printf("best at %d, %d, %lld is %lld\n", ni, mi, left, ret);
	return cache[ni][mi][left] = ret;
}

int main() {
	initIO();
	int t;
	scanf("%d", &t);
	for (int ti=1; ti<=t; ti++) {
		a.clear();
		b.clear();
		scanf("%d%d", &n, &m);
		for (int i=0; i<123; i++) {
			for (int j=0; j<123; j++) {
				cache[i][j].clear();
			}
		}
		for (int i=0; i<n; i++) {
			lld i1, i2;
			scanf("%lld%lld", &i1, &i2);
			a.push_back(mp(i2, i1));
		}
		for (int i=0; i<m; i++) {
			lld i1, i2;
			scanf("%lld%lld", &i1, &i2);
			b.push_back(mp(i2, i1));
		}
		lld best = dp(0, 0, b[0].s);
		printf("Case #%d: %lld\n", ti, best);
	}

	return 0;
}