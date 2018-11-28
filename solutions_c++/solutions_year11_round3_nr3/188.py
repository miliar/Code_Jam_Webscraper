#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cstdlib>
using namespace std;

#define N 10010
int t, xx, n, m, l, h, x[N], ans;
char s[N][N];

void open() {
	freopen("C.txt", "r", stdin);
	freopen("C2.txt", "w", stdout);
}

int main() {
	open();
	xx = 1;
	scanf("%d", &t);
	while (t--) {
		scanf("%d%d%d", &n, &l, &h);
		int lcm = 1;
		for (int i = 0; i < n; i++) {
			scanf("%d", &x[i]);
		}
		bool impossible = 1;
		for (int i = l; i <= h; i++) {
			bool found = 1;
			for (int j = 0; j < n; j++) {
				if (!(i % x[j] == 0 || x[j] % i == 0))  {
					found = 0; break;
				}
			}
			if (found) {
				ans = i;
				impossible = 0;
				break;
			}
		}
		printf("Case #%d: ", xx++);
		if (impossible) printf("NO\n");
		else printf("%d\n", ans);
	}
	return 0;
}