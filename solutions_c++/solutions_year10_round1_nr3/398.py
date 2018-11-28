#include <algorithm>
#include <cstdio>

int T, A1, A2, B1, B2;

bool won(int a, int b, bool colour = true) {
	if (b > a) std::swap(a, b);
	int k = std::max(1, a/b-2);
	while (a-k*b > 0) {
		if (won(a-k*b, b, !colour) == colour) return colour;
		k++;
	}
	return !colour;
}

int	main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d %d %d %d", &A1, &A2, &B1, &B2);

		int total = 0;
		for (int a = A1; a <= A2; ++a)
			for (int b = B1; b <= B2; ++b)
				if (won(a, b)) ++total;
		printf("Case #%d: %d\n", t, total);
	}
}
