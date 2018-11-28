#include <cstdio>
#include <cstring>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>

#define Eo(x) { std::cerr << #x << " = " << x << std::endl; }

typedef long long int64;

#define maxn (1 << 10)

int r, k, n, g[maxn];
int was[maxn];
int64 money[maxn];

int main() {
	int t = 1, tc;
	for(scanf("%d", &tc); t <= tc; t++) {
		printf("Case #%d: ", t);
		scanf("%d%d%d", &r, &k, &n);
		for(int i = 0; i < n; i++) scanf("%d", g+i);
		memset(was, -1, sizeof(was[0])*n);
		int j = 0, ps = 0;
		int64 prof = 0;
		for(; j < r && was[ps] == -1; j++) {
			was[ps] = j;
			money[ps] = prof;
			int cap = k, pso = ps;
			do {
				if(cap < g[ps]) break;
				cap -= g[ps];
				ps = (ps+1) % n;
			} while(ps != pso);
			prof += (k-cap);
		}
		if(j == r) {
			printf("%Ld\n", prof);
			continue;
		}
		int64 cyc = prof - money[ps];
		int len = j - was[ps];
		int64 tot = money[ps];
		int cnt = (r-was[ps]) / len;
		int nj = cnt * len + was[ps];
		tot += cnt * cyc;
		for(j = nj; j < r; j++) {
			int cap = k, pso = ps;
			do {
				if(cap < g[ps]) break;
				cap -= g[ps];
				ps = (ps+1) % n;
			} while(ps != pso);
			tot += (k-cap);
		}
		printf("%Ld\n", tot);
	}
	return 0;
}
