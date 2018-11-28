#include <stdio.h>

int main() {
	int tests;
	scanf("%d", &tests);
	for (int test_num = 0; test_num < tests; ++test_num) {
		int n, pd, pg;
		scanf("%d", &n);
		scanf("%d", &pd);
		scanf("%d", &pg);

		bool good_n = false;
		for (int i = 1; i <= n; ++i) {
			if (i * pd % 100 == 0)
			{
				good_n = true;
				break;
			}
		}
		bool bad_p = ((pd != 100 && pg == 100) ||
		              (pd != 0   && pg == 0));
		printf("Case #%d: %s\n",
		       (test_num + 1),
		       (good_n && !bad_p) ? "Possible" : "Broken"); 
	}
}
