#include <stdio.h>

int cs, ct;
long long n;
int p[1000000], t;

void make_prime()
{
	int i, j;
	bool isprime;
	t = 0;
	for (i = 2; i <= 1000000; i++) {
		isprime = 1;
		for (j = 2; j * j <= i; j++)
		if (i % j == 0) {
			isprime = 0;
			break;
		}
		if (isprime) p[t++] = i;
	}
}



int main()
{
	int i, k;
	long long j;

	make_prime();

	scanf("%d", &ct);
	for (cs = 1; cs <= ct; cs++) {
		scanf("%lld", &n);
		if (n == 1) {
			printf("Case #%d: %d\n", cs, 0);
			continue;
		}
		k = 0;
		for (i = 0; i < t; i++) {
			if (p[i] > n) break;
			j = n;
			while (j >= p[i]) {
				j /= p[i];
				k++;
			}
		}
		printf("Case #%d: %d\n", cs, k - i + 1);
	}	
	return 0;
}
