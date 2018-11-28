#include <cstdio>
#include <algorithm>
#include <climits>

int T;
int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; t ++) {
		int N;
		scanf("%d", &N);
		int min = INT_MAX;
		int sum = 0;
		int xOr = 0;
		for (int i = 0; i < N; i ++) {
			int tmp;
			scanf("%d", &tmp);
			sum += tmp;
			xOr ^= tmp;
			min = std :: min(min, tmp);
		}
		printf("Case #%d: ", t);
		if (xOr) {
			printf("NO\n");
		} else {
			printf("%d\n", sum - min);
		}
	}
}