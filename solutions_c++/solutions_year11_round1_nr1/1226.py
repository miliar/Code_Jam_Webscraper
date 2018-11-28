#include <stdio.h>

inline int gcd(int a, int b) {
	while (b != 0) {
		int temp = a;
		a = b;
		b = temp % b;
	}
	return a;
}

int main() {
	int T = 0;
	scanf("%d", &T);
	for (int t = 0; t < T; ++t) {
		int N, Pd, Pg;
		scanf("%d %d %d", &N, &Pd, &Pg);
		bool possible = false;
		if (Pg == 0 || Pg == 100) {
			possible = Pd == Pg;
		}
		else {
			possible = N >= 100 / gcd(Pd, 100);
		}
		printf("Case #%d: %s\n", t + 1, possible ? "Possible" : "Broken");
	}
}
