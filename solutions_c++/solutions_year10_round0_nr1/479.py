#include <iostream>

using namespace std;

int main()
{
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);
	int tc, nc, dua, n, k;
	scanf("%d", &tc);
	for (nc = 1; nc <= tc; nc++) {
		scanf("%d%d", &n, &k);
		dua = (1<<n);
		k %= dua;
		if (k == dua-1)
			printf("Case #%d: ON\n", nc);
		else
			printf("Case #%d: OFF\n", nc);
	}
}
