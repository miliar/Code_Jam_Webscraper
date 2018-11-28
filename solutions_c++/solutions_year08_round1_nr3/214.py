
// USING GMP - GNU MULTI PRECISION LIBRARY

#include <iostream>
#include <gmp.h>
#include <gmpxx.h>

using namespace std;

int main()
{
    int N;

    cin >> N;

    for( int CASE = 1; CASE <= N; CASE++ )
    {
        unsigned int n;
        mpf_class five(5.0);
        mpf_class p(0, 512*1024);
        p = sqrt(five);
        p += 3;

        cin >> n;
        mpf_class power(0, 1024*512);
        mpf_pow_ui(power.get_mpf_t(), p.get_mpf_t(), n);
        mpz_class result(floor(power));

        result = result%1000;

        int r = (int) result.get_si();

        cout << "Case #" << CASE << ": " << (r/100)%10 <<
                                            (r/10)%10  <<
                                            r%10 << endl;
    }

    return 0;
}


