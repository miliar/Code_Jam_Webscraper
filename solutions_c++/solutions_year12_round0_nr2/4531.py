#include <cstdio>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <iostream>
#include <cmath>
using namespace std;

int a[1000];

int main() {
	int test;
	scanf("%d ", &test);
	for (int cas = 1; cas <= test; ++cas) {
		int n, s, p;
		scanf("%d%d%d", &n, &s, &p);
		for (int i = 0; i < n; ++i)
			scanf("%d", a + i);
		int ans = 0;
		for (int i = 0; i < n; ++i) {
			if ((a[i] + 2) / 3 >= p) {
				++ans;
				continue;
			}
			if (a[i] % 3 == 1) continue;
			if (a[i] == 0) continue;
			if ((a[i] + 2) / 3 + 1 < p) continue;
			if (s == 0) continue;
			++ans; --s;
		}
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}
