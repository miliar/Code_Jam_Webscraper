#include <stdio.h>
#include <stdlib.h>

int main()
{
	int cases;
	scanf("%d", &cases);
	for (int cas = 1; cas <= cases; cas++) {
		int n, i, num[1000], tot = 0, sum = 0, min = 0;
		scanf("%d", &n);
		for (i = 0; i < n; i++) {
			scanf("%d", &num[i]);
			tot = tot ^ num[i];
			sum += num[i];
			//for (x = num[i], j = 0; x != 0; x >>= 1, j++) {
			//	if ((x & 1) != 0) cnt[j]++;
			//}
			if (i == 0) min = num[i];
			if (num[i] < min) min = num[i];
		}
		printf("Case #%d: ", cas);
		if (tot != 0) printf("NO\n");
		else printf("%d\n", sum - min);
	}
	return 0;
}
