#include <stdio.h>
#include <iostream>
#include <gmpxx.h>
using namespace std;

int main() {
    int c;
    scanf("%d", &c);

    for (int line = 1; line <= c; line++) {
	mpz_class t[1000];
	int n;

	cin >> n;
	for (int i = 0; i < n; i++) cin >> t[i];

	int imax = 0;
	for (int i = 0; i < n; i++)
	    if (t[i] > t[imax]) imax = i;

	mpz_class diff[1000];
	for (int i = 0; i < n; i++) diff[i] = t[imax] - t[i];

	for (int i = 1; i < n; i++) {
	    mpz_gcd(diff[0].get_mpz_t(),
		diff[0].get_mpz_t(), diff[i].get_mpz_t());
	}

	mpz_class result;
	mpz_class x = -t[0];

	mpz_fdiv_r(result.get_mpz_t(),
	    x.get_mpz_t(), diff[0].get_mpz_t());

	printf("Case #%d: ", line);
	cout << result;
	printf("\n");
    }
}
