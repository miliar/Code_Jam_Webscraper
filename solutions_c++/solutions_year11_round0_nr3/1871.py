#include <stdio.h>

int main()
{
	int kase, serial=1,
		n, score, min_score,
		xor_all;
	long long total;

	scanf("%d", &kase);
	while (kase--) {
		// begin test case

		total = xor_all = 0;
		min_score = -1;

		scanf("%d", &n);
		scanf("%d", &score);
		total = xor_all = min_score = score;
		for (int i=1; i<n; ++i) {
			scanf("%d", &score);
			total += score;
			xor_all ^= score;
			if (min_score > score)
				min_score = score;
		}

		/**
		 * If there is a solution,
		 *    a ^ b ^ c ^ ... = x ^ y ^ z ^ ...
		 * <=> a ^ b ^ c ^ ... ^ x ^ y ^ z ^ ... = 0
		 */
		if (xor_all == 0)
			printf("Case #%d: %lld\n", serial++, total - min_score);
		else
			printf("Case #%d: NO\n", serial++);
		// end test case
	}
	return 0;
}
