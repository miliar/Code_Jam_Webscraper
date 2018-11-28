#include <stdio.h>
#include <algorithm>
using namespace std;
int main() {
	int T;
	scanf("%d", &T);
	for (int _ = 0; _ < T; _++) {
		printf("Case #%d: ", _+1);
		int N;
		scanf("%d", &N);
		int sum = 0, x = 0, mi = 1000000000;
		for (int i = 0; i < N; i++) {
			int temp;
			scanf("%d", &temp);
			sum += temp;
			x ^= temp;
			mi = min(mi, temp);
		}
		if (x) printf("NO\n");
		else printf("%d\n", sum - mi);
	}
	return 0;
}
