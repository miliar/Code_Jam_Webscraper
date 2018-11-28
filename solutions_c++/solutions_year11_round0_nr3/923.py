#include <cstdio>

int main()
{
	int testCases;

	scanf("%d", &testCases);
	for (int t = 1; t <= testCases; ++ t) {
		int n, val, sum = 0, min = 0x7FFFFFFF, result = 0;
		scanf("%d", &n);
		while (n --) {
			scanf("%d", &val);
			sum += val;
			min = min < val ? min : val;
			result ^= val;
		}
		if (result) {
			printf("Case #%d: NO\n", t);
		} else {
			printf("Case #%d: %d\n", t, sum - min);
		}
	}
	return 0;
}
