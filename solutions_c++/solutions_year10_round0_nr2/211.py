//g++ main.cpp -lgmpxx -lgmp
#include <gmp.h>

#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
    int no_cases = 0;
    cin >> no_cases;
    for (int c=0; c < no_cases; ++c) {
        int no_vals = 0;
        cin >> no_vals;
        
        mpz_t* vals = new mpz_t[no_vals];
        for (int v=0; v < no_vals; ++v) {
            string val_string;
            cin >> val_string;
            mpz_init(vals[v]);
            mpz_set_str(vals[v], val_string.c_str(), 10);
        }

        mpz_t T, T2;
        mpz_init(T);
        mpz_init(T2);
        bool first = true;
        for (int v1=0; v1 < no_vals; ++v1) {
            for (int v2=v1+1; v2 < no_vals; ++v2) {
                if (vals[v1] != vals[v2]) {
                    mpz_t temp, temp2;
                    mpz_init(temp);
                    mpz_init(temp2);
                    mpz_sub(temp, vals[v1], vals[v2]);
                    mpz_abs(temp2, temp);
                    
                    if (first)
                        mpz_init_set(T, temp2);
                    else {
                        mpz_gcd(T2, T, temp2);
                        mpz_set(T, T2);
                    }
                    first = false;
                    mpz_clear(temp);
                    mpz_clear(temp2);
                }
            }
        }

        // y = T - mod(vals[0], T)
        mpz_t y, y2, modtemp;
        mpz_init_set(y, T);
        mpz_init(y2);
        mpz_init(modtemp);
        mpz_mod(modtemp, vals[0], T);
        mpz_sub(y2, y, modtemp);

        if (mpz_cmp(y2, T) == 0)
            mpz_set_si(y2, 0);
        
        char* s = mpz_get_str(0, 10, y2);
        cout << "Case #" << (c+1) << ": " << s << endl;
        mpz_clear(y);
        mpz_clear(y2);
        mpz_clear(modtemp);
        mpz_clear(T);
        for (int v=0; v<no_vals; ++v)
            mpz_clear(vals[v]);
        delete[] vals;
    }
    return 0;
}
