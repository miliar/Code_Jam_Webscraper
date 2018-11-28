#include <iostream>
#include <algorithm>

using namespace std;

int t, n, k;

int main() {
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		scanf("%d%d", &n, &k);
		int two = 1 << n;
		k = k % two;
		if (k == two - 1) printf("Case #%d: ON\n", i);
		else printf("Case #%d: OFF\n", i);
	}
	return 0;
}