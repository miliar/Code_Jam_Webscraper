#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <gmp.h>

using namespace std;

#define forall(i,n) for(int i=0; i<(int)(n); i++)


int main() {
    int nTests;
    int rc = scanf("%d", &nTests);
    assert(rc == 1);
    for (int iTest=1; iTest<=nTests; iTest++) {
	int nEvents;
	int rc = scanf("%d", &nEvents);
	assert(rc == 1);

	mpz_t time1;
	mpz_init(time1);
	rc = mpz_inp_str(time1, stdin, 10);
	assert(rc > 0);

	mpz_t gcd, time, diff, temp, ans;
	mpz_init(gcd);
	mpz_init(time);
	mpz_init(diff);
	mpz_init(temp);
	mpz_init(ans);

	for (int iEvent=2; iEvent <= nEvents; iEvent++) {
	    int rc = mpz_inp_str(time, stdin, 10);
	    assert(rc > 0);

	    // gcd = GCD(gcd, time-time1);
	    mpz_sub(diff, time, time1);
	    mpz_gcd(temp, gcd, diff);
	    mpz_set(gcd, temp);
	}

	// int ans = gcd - (time1 % gcd);
	mpz_fdiv_r(temp, time1, gcd);
	mpz_sub(ans, gcd, temp);
	// if (ans==gcd) ans=0;
	if (mpz_cmp(ans, gcd) == 0)
	    mpz_set_ui(ans, 0);

	// cout << "Case #" << iTest <<": " << res << endl;
	printf("Case #%d: ", iTest);
	rc = mpz_out_str(stdout, 10, ans);
	assert(rc > 0);
	printf("\n");
    }
}
