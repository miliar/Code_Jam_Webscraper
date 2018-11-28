#include <cstdio>

int casei, cases, n, m;

int main() {
	//freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	//freopen("A-small-attempt1.out", "w", stdout);
	freopen("A-large.out", "w", stdout);

	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		scanf("%d%d", &n, &m);
		if (m % (1 << n) == (1 << n) - 1) printf("Case #%d: ON\n", casei);
		else printf("Case #%d: OFF\n", casei);
	}
	return 0;
}
