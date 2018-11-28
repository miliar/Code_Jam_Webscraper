
#include "cstdio"


int main(int argc, char *argv[]) {
  freopen(argv[1], "r", stdin);

	int tn;
	scanf("%d", &tn);

	for (int ti = 1; ti <= tn; ti++) {
		int n;
  	scanf("%d", &n);

		int wsum = 0;
		int min = 2000000;
		int sum = 0;
  	for (int i = 1; i <= n; i++) {
			int curr;
	  	scanf("%d", &curr);

			wsum ^= curr;
			sum += curr;
			//printf("curr: %d\n", curr);
			if (curr < min) {
				min = curr;
			}
		}

		printf("Case #%d: ", ti);
		if (wsum == 0) {
			printf("%d\n", sum - min);
		} else {
			printf("NO\n");
		}

	}


	return 0;
}




