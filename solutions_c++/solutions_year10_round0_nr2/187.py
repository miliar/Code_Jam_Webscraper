#include <iostream>
#include <gmp.h>

using namespace std;

void gcd (mpz_t rop, mpz_t a, mpz_t b) {
    // No negatives
    mpz_abs(a, a);
    mpz_abs(b, b);

    // Ensure a >= b; can save a useless MOD
    if (mpz_cmp(b, a) > 0) { mpz_swap(a, b); }

    // Main loop of algorithm
    mpz_t temp;
    mpz_init(temp);
    while (mpz_cmp_si(b, 0) > 0) {
        mpz_set(temp, b);
        mpz_mod(b, a, b);
        mpz_set(a, temp);
    } // end while
    mpz_set(rop, a);
} // end GCD()


void doCase(int caseNum) {
    int N;

    cin >> N;

    mpz_t t[N];

    mpz_t smallest;
    mpz_init(smallest);

    int smallest_idx = -1;
    for (int i = 0; i < N; i++) {
        string ti_s;

        cin >> ti_s;

        mpz_init_set_str(t[i], ti_s.c_str(), 10);

        if (i == 0 || mpz_cmp(t[i], smallest) < 0) {
            mpz_set(smallest, t[i]);
            smallest_idx = i;
        }
    }

    mpz_t denom;
    mpz_init(denom);
    mpz_set(denom, t[smallest_idx == 0 ? 1 : 0]);
    mpz_sub(denom, denom, smallest);
    for (int i = 1; i < N; i++) {
        if (i == smallest_idx) continue;

        mpz_t temp;
        mpz_init(temp);
        mpz_sub(temp, t[i], smallest);
        gcd(denom, denom, temp);
    }

    mpz_t r;
    mpz_init(r);
    mpz_mod(r, smallest, denom);

    mpz_t ans;
    mpz_init(ans);
    mpz_sub(ans, denom, r);
    mpz_mod(ans, ans, denom);

    char *out = mpz_get_str(NULL, 10, ans);

    cout << "Case #" << caseNum << ": " << out << endl;
}

int main() {
    int T;

    cin >> T;

    for (int i = 0; i < T; i++) {
        doCase(i+1);
    }
}
