#include <cstdio>

int T, n;
int sum, small, mask;

int main(void) {
	scanf("%d", &T);
	for(int C = 1; C <= T; C++) {
		scanf("%d", &n);

		sum = 0;
		small = 0x3f3f3f3f;
		mask = 0;

		for(int i = 0; i < n; i++) {
			int num;
			scanf("%d", &num);
			mask ^= num, sum += num;
			if(num < small) small = num;
		}

		if(mask) printf("Case #%d: NO\n", C);
		else printf("Case #%d: %d\n", C, sum - small);
	}

	return 0;
}
