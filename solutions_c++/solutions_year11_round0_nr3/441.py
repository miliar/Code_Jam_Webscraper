#include <cstdio>
#include <algorithm>

using namespace std;

void solve() {
	int N; scanf("%d", &N);

	int bsum = 0; int minimum = 0x7fffffff; int sum = 0;
	for (int i = 0; i < N; i++) {
		int a; scanf("%d", &a);
		minimum = min(minimum, a);
		bsum ^= a;
		sum += a;
	}

	if (bsum) printf("NO\n");
	else printf("%d\n", sum - minimum);
}

int main() {
	int T; scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}
