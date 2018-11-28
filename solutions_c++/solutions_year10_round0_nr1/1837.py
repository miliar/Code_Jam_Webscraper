#include <cstdio>

using namespace std;

int tt, q, n, x;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);

	scanf("%d", &tt);
	for (q = 1; q <= tt; q++) {
		scanf("%d%d", &n, &x);
		if ((x + 1) % (1 << n) == 0)
			printf("Case #%d: ON\n", q);
		else
			printf("Case #%d: OFF\n", q);
	}


	return 0;
}
