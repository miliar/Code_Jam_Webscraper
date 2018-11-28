#include <stdio.h>
#include <assert.h>

int main(void) {
	int T, cs=0;
	scanf("%d", &T);
	for(cs=1;cs<=T;cs++){
		int n;
		int sum = 0, min = 1000005, Xor = 0;
		scanf("%d", &n);
		for(int i=0;i<n;i++){
			int x;
			scanf("%d", &x);
			sum += x;
			Xor ^= x;
			assert(x <= 1000000);
			if (x < min)
				min = x;
		}
		
		printf("Case #%d: ", cs);
		fprintf(stderr, "Case #%d: ", cs);
		if (Xor != 0) {
			printf("NO\n");
			fprintf(stderr, "NO\n");
		} else {
			printf("%d\n", sum - min);
			fprintf(stderr, "%d\n", sum - min);
		}
	}
	return 0;
}
