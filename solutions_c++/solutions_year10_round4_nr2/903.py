#include <stdio.h>
#include <algorithm>

int m[2000];

int foo(int l, int r) {
	bool ok = true;
	for (int i = l; i <= r; ++i) {
		if (m[i] > 0) {
			ok = false;
			m[i]--;
		}
	}
	if (ok) return 0;
	return l+1 == r ? 1 : 1 + foo(l, (r+l)/2) + foo((l+r)/2+1, r);
}

int go() {
	int p, k;
	scanf("%d", &p);
	k = 1 << p;
	for (int i=  0; i < k; ++i) {
		scanf("%d", &m[i]);
		m[i] = p - m[i];
	}
	int tmp;
	for (int i = p-1; i >= 0; --i)
		for (int j = 1<<i; j > 0; --j)
			scanf("%d", &tmp);
	return foo(0, k-1);
}

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i=  0; i < t; ++i)
		printf("Case #%d: %d\n", i+1, go());
}