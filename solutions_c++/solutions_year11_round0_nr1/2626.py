#include <cstdio>

int abs(int x) {
	if (x < 0) return -x;
	else return x;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		int n;
		scanf("%d", &n);

		int cp[2];
		cp[0] = cp[1] = 1;
		int turn = 2;
		int elapsed = 0;
		int total = 0;

		while (n--) {
			char r;
			int p;
			scanf(" %c %d", &r, &p);

			int ri;
			if (r == 'O') ri = 0;
			else ri = 1;

			int diff = abs(cp[ri] - p);

			if (turn == ri) {
				int spent = diff + 1;
				elapsed += spent;
				total += spent;
			} else {
				int spent = 1;
				if (diff > elapsed) spent += (diff - elapsed);
				elapsed = spent;
				total += spent;
				turn = ri;
			}
			cp[ri] = p;
		}
		printf("Case #%d: %d\n", i, total);
	}
	return 0;
}
