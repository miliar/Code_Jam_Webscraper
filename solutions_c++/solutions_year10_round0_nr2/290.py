#include <iostream>
#include <fstream>
#include <stddef.h>
#include "gmp.h"

using namespace std;

int C, N;
char t[1001][51];
mpz_t t2[1001];
mpz_t dif[1000];
mpz_t Gr,qq,rr;
char ans[51];


int main()
{
    mpz_init (Gr);
    mpz_init (qq);
    mpz_init (rr);



    ifstream b_file ( "input.txt" );
    ofstream a_file ( "output.txt" );





    b_file >> C;
    for (int i=1; i<=C; i++)
        {
        b_file >> N;


        for (int j=0; j<N; j++)
        {
            b_file >> t[j];
            mpz_set_str(t2[j],t[j],10);
            if (j != 0) mpz_sub(dif[j-1],t2[j],t2[j-1]);
        }

        mpz_gcd(Gr,dif[0],dif[0]);
        for (int j=0; j<N-1; j++)
        {
            mpz_gcd(Gr,Gr,dif[j]);
        }

        mpz_cdiv_qr (qq, rr, t2[0], Gr);
        mpz_abs(rr, rr);
        mpz_get_str (ans, 10, rr);

        cout << i << "\n";
        a_file<<"Case #"<<i<<": "<<ans<<"\n";
        }


    cin.get();

    return 0;
}

