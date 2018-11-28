#include <cstdio>
using namespace std;

int main() {
	freopen("x.in", "r", stdin);
	freopen("snap.out", "w", stdout);
	int i, t, n, k, ok, n1;
	scanf("%d", &t);
	for (i = 1; i <= t; i++) {
		scanf("%d %d", &n, &k);
		n1 = ((1 << n) - 1);
		ok = k & n1;
		printf("Case #%d: ", i);
		if (ok == n1)
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}
