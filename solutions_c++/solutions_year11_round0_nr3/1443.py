#include <cstdio>
#include <cstdlib>

using namespace std;

int main() {
	int t;
	scanf("%d", &t);
	for (int nCase = 1; nCase <= t; ++nCase) {
		int n;
		scanf("%d", &n);
		int ans = 0, min = 10000000, sum = 0;
		for (int i = 0; i < n; ++i) {
			int c;
			scanf("%d", &c);
			if (min > c) {
				min = c;
			}
			ans ^= c;
			sum += c;
		}
		printf("Case #%d: ", nCase);
		if (ans == 0) {
			printf("%d\n", sum - min);
		} else printf("NO\n");
	}
	return 0;
}
