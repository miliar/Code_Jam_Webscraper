#include <cstdio>
#include <gmp.h>

int main () {
	int c, n;
	char buf[100];
	mpz_t first, next, result, tmp, tmp2;
	mpz_inits(first, next, result, tmp, tmp2, NULL);

	scanf("%d", &c);
	for (int i = 1; i <= c; i++) {
		scanf("%d", &n);
		scanf("%s", buf);
		mpz_set_str(first, buf, 10);
		mpz_set_si(result, 0);
		for (int j = 1; j < n; j++) {
			scanf("%s", buf);
			mpz_set_str(next, buf, 10);
			mpz_sub(tmp, next, first);
			mpz_gcd(tmp2, result, tmp);
			mpz_set(result, tmp2);
		}

		mpz_mul_si(tmp, first, -1);
		mpz_mod(tmp2, tmp, result);
		mpz_get_str(buf, 10, tmp2);
		printf("Case #%d: %s\n", i, buf);
	}
	return 0;
}
