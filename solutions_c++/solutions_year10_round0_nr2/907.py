#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b);
int func_gcd(int a, int b);

int C, N;
int t[3], gcd, ans;

int main()
{
	scanf("%d", &C);
	for (int i = 0; i < C; i++) {
		scanf("%d", &N);
		for (int j = 0; j < N; j++) {
			scanf("%d", t+j);
		}
		qsort(t, N, sizeof(int), cmp);
		if (N == 3) {
			if (t[0] == t[1]) {
				t[1] = t[2];
				N--;
			} else if (t[1] == t[2]) {
				N--;
			}
		}
		if (N == 2) {
			gcd = t[1] - t[0];
		} else {
			gcd = func_gcd(t[2] - t[0], t[1] - t[0]);
		}

		if (t[0] % gcd == 0) {
			printf("Case #%d: 0\n", i+1);
		} else {
			printf("Case #%d: %d\n", i+1, gcd - (t[0] % gcd));
		}
	}
}

int cmp(const void *a, const void *b)
{
	int *c = (int *)a;
	int *d = (int *)b;
	return *c - *d;
}

int func_gcd(int a, int b)
{
	if (a % b == 0) {
		return b;
	}
	return func_gcd(b, a%b);
}
