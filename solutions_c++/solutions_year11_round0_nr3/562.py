#include <cstdio>

using namespace std;

int t;
int n;

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("c.out", "w", stdout);

	scanf("%d", &t);

	for (int gi = 0; gi < t; gi++) {
		scanf("%d", &n);
		int sum = 0;
		int min = 1000001;
		int xor = 0;
		for (int i = 0; i < n; i++) {
			int a;
			scanf("%d", &a);
			sum += a;
			if (min > a) { min = a; }
			xor ^= a;
		}

		if (xor != 0) {
			printf("Case #%d: NO\n", gi+1);
		}
		else {
			printf("Case #%d: %d\n", gi+1, sum-min);
		}
	}

	return 0;
}
