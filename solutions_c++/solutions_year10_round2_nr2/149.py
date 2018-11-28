#include <cstdio>
#include <cstring>
#include <cstdlib>
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

#define maxn (1 << 7)

int x[maxn], v[maxn], p[maxn];

int getp(int v) {
	return (p[v] == v) ? v : (p[v] = getp(p[v]));
}

bool link(int u, int v) {
	u = getp(u);
	v = getp(v);
	if(u == v) return false;
	p[u] = v;
	return true;
}

int main() {
	int tt = 1, tc;
	for(scanf("%d", &tc); tt <= tc; tt++) {
		printf("Case #%d: ", tt);
		int n, k, b, t;
		scanf("%d%d%d%d", &n, &k, &b, &t);
		for(int i = 0; i < n; i++) p[i] = i;
		for(int i = 0; i < n; i++) scanf("%d", x+i);
		for(int i = 0; i < n; i++) scanf("%d", v+i);

		for(int i = n-1; i > 0; i--) {
			int j = getp(i);
			if(v[i-1] <= v[j] || (x[j] - x[i-1]) > t * (v[i-1] - v[j])) continue;
			link(i-1, j);
		}

		int cnt = 0, got = 0, ans = 0;
		for(int i = n-1; i >= 0 && got < k; i--) {
			int j = getp(i);
			if(x[i] + v[i] * t >= b) {
				got ++;
				if(x[j] + v[j] * t < b)
					ans += cnt;
			} else
				cnt ++;
		}

		if(got < k) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}
	return 0;
}
