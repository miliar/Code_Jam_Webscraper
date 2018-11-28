#include <cstdio>

int isPrime(int n) {
		if (n == 1) return 0;
		if (n == 2) return 1;
		for (int i = 2; i * i <= n; ++i) {
				if (n % i == 0) return 0;
		}
		return 1;
}

int main() {
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
		int r;
		int case_no = 0;
		scanf("%d", &r);
		while (r--) {
				int n;
				scanf("%d", &n);
				printf("Case #%d: ", ++case_no);
				if (n == 1) {
						printf("0\n");
						continue;
				}
				int p1 = 0, p2 = 0;
				for (int i = 1; i <= n; ++i) {
						int t = isPrime(i);
						p1 += t;
						if (t) {
								int j = i;
								while (j <= n) {
										p2++;
										j *= i;
								}
						}
				}				
				printf("%d\n", p2 - p1 + 1);
		}

		return 0;
}