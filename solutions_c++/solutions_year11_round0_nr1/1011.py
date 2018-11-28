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
		int ans = 0;
		int opos = 1;
		int bpos = 1;
		int ofree = 0;
		int bfree = 0;
		for (int i = 0; i < n; ++i) {
			char q;
			int pos;
			scanf(" %c %d", &q, &pos);
			if (q == 'O') {
				int len = abs(opos - pos);
				ans += max(len - ofree, 0) + 1;
				bfree += max(len - ofree, 0) + 1;
				ofree = 0;
				opos = pos;
			} else {
				int len = abs(bpos - pos);
				ans += max(len - bfree, 0) + 1;
				ofree += max(len - bfree, 0) + 1;
				bfree = 0;
				bpos = pos;
			}
		}
		printf("Case #%d: %d\n", tt + 1, ans);
	}
	return 0;
}
