#include <stdio.h>

int main()
{
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; ++Case) {
		int N;
		scanf("%d", &N);
		int sum = 0;
		int min = 100000000;
		int r = 0;
		while (--N >= 0) {
			int d;
			scanf("%d", &d);
			sum += d;
			if (d < min)
				min = d;
			r ^= d;
		}
		if (r) {
			printf("Case #%d: NO\n", Case);
		} else {
			printf("Case #%d: %d\n", Case, sum - min);
		}
	}
	return 0;
}


