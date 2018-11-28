#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>

using namespace std;

#pragma comment(linker, "/STACK:160000000")

int main() {
#ifndef ONLINE_JUDGE
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif
	int t;

	scanf("%d", &t);
	for (int tt = 0; tt < t; ++tt) {
		int n;
		scanf("%d", &n);
		int sum = 0;
		int x = 0;
		int mn = 0x3f3f3f3f;
		for (int i = 0; i < n; ++i) {
			int a;
			scanf("%lld", &a);
			sum += a;
			x ^= a;
			mn = min(mn, a);
		}
		printf("Case #%d: ", tt + 1);
		if (x != 0) {
			printf("NO\n");
		} else {
			printf("%lld\n", sum - mn);
		}
	}

	return 0;
}
