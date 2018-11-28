#include <cstdio>
#include <iostream>

using namespace std;

int main () {
	freopen("lardwtg.in", "r", stdin);
	freopen("lardwtg.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		int n, s, p, ans = 0;
		scanf("%d%d%d", &n, &s, &p);
		for (int j = 1; j <= n; j++) {
			int b, c;
			scanf("%d", &c);
			c -= c / 3;
			b = c / 2; c -= b;
			if (c >= p) ans++;
			else {
				if (c == b && c + 1 >= p && s > 0 && c > 0) {
					ans++;
					s--;
				}
			}
		}
		printf("Case #%d: %d\n", i, ans);
	}
} 

			
