#include <cstdio>
#include <cstdlib>
#include <gmp.h>
using namespace std;


int main()
{
    FILE * input = fopen("input", "r");
    FILE * output = fopen("output", "w");
    int C;
    fscanf(input, "%d", &C);
    for(int cas = 1; cas <= C; cas++)
    {
        int N;
        fscanf(input, "%d", &N);
        mpz_t t[N];
        for(int i = 0; i < N; i++)
        {
            mpz_init(t[i]);
            gmp_fscanf(input, "%Zd", t[i]);
        }
        mpz_t pgcd;
        mpz_init(pgcd);
        mpz_t diff;
        mpz_init(diff);
        mpz_t result;
        mpz_init(result);

        mpz_sub(pgcd, t[1], t[0]);
        for(int i = 2; i < N; i++)
        {
            mpz_sub(diff, t[i], t[i-1]);
            mpz_gcd(pgcd, pgcd, diff);
        }
        mpz_mod(result, t[0], pgcd);
        mpz_sub(result, pgcd, result);
        mpz_mod(result, result, pgcd);
        gmp_fprintf(output, "Case #%d: %Zd\n", cas, result);
        printf("%d\n", cas);
    }
    printf("done\n");
}

