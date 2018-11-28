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

const int N = 1111;

int a[N];
bool color[N];

int main() {
#ifndef ONLINE_JUDGE
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif
	
	int t;

	scanf("%d", &t);
	for (int tt = 0; tt < t; ++tt) {
		int n;
		int ans = 0;
		memset(color, 0, sizeof(color));
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%d", &a[i]);
			--a[i];
		}
		for (int i = 0; i < n; ++i) {
			if (!color[i]) {
				int cnt = 0;
				int j = i;
				while (!color[j]) {
					color[j] = 1;
					++cnt;
					j = a[j];
				}
				if (cnt > 1) {
					ans += cnt;
				}
			}
		}
		printf("Case #%d: %d\n", tt + 1, ans);
	}

	return 0;
}
