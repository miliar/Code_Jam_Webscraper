#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
	int tests; scanf("%d", &tests);
	for (int test = 1; test <= tests; test++) {
		int n; scanf("%d", &n);
		int sum = 0, mini = 100000000, total = 0;
		for (int i = 0; i < n; i++) {
			int x; scanf("%d", &x);
			mini = min(mini, x);
			sum ^= x;
			total += x;
		}
		printf("Case #%d: ", test);
		if (sum == 0)
			printf("%d\n", total - mini);
		else
			printf("NO\n");
	}

	return 0;
}
