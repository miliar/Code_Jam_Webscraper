#include <iostream>
#include <cstdio>

using namespace std;

int d[29];
int u[2000009];

int main () {
	freopen("rn.in", "r", stdin);
	freopen("rn.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		int a, b;
		scanf("%d%d", &a, &b);
		int x = a, l = 0, ans = 0;
		for ( ; x > 0; x /= 10) l++; 
		for (int j = a; j <= b; j++) u[j] = 0;
		for (int j = a; j < b; j++) {
			x = j;
			int k = 0;
			for ( ; k < 2 * l; k++) {
				if (k < l) {
					d[k] = x % 10;
					x /= 10;
				}
				else d[k] = d[k - l];
			}
			for (k = 2 * l - 2; k >= l; k--) {
				int s = 0;
				for (int o = k; o > k - l; o--)
					s = s * 10 + d[o];
				if (u[s] != j && j < s && s <= b) {
					ans++;
					u[s] = j;
				}
			}
		}
		printf("Case #%d: %d\n", i, ans);
	}
}
			
			