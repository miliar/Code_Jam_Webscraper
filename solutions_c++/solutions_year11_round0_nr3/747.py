#include <algorithm>
#include <string.h>
#include <stdio.h>

using namespace std;
#define mymin(x, y) ((x) < (y) ? (x) : (y))
int main()
{
	int T, N, min_t;
	scanf("%d", &T);
	for (int ncas = 1; ncas <= T; ncas++) {
		scanf("%d", &N);
		int tmp = 0, num; min_t = (1 << 30);
		int tot = 0;
		for (int i = 0; i < N; i++) {
			scanf("%d", &num);
			min_t = mymin(min_t, num);
			tmp ^= num;
			tot += num;
		}
		printf("Case #%d: ", ncas);
		if (tmp == 0) {
			printf("%d\n", tot - min_t);
		} else {
			printf("NO\n");
		}
	}
	return 0;
}
