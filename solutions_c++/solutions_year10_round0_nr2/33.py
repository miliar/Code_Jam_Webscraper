#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <stdio.h>
#include <gmp.h>	// if GMP is not allowed, I apologize
using namespace std;

int main()
{

fstream In("b-large.in", ios::in);
fstream Out("b-large.out", ios::out);

int tests;

In >> tests;

for(int h=0; h<tests; h++)
{

int N;

In >> N;
mpz_t v[1010];
for(int i=0; i<N; i++) mpz_init(v[i]);

for(int i=0; i<N; i++)
{
In >> v[i];
}

mpz_t ret, temp;
mpz_init(ret);
mpz_init(temp);

mpz_sub(ret, v[0], v[1]);
mpz_abs(ret, ret);

for(int i=0; i<N; i++)
for(int j=i+1; j<N; j++)
{
	mpz_sub(temp, v[i], v[j]);
	mpz_abs(temp, temp);
	mpz_gcd(ret, ret, temp);
}

cout << ret << endl;

mpz_mod(temp, v[0], ret);
mpz_sub(temp, ret, temp);
mpz_mod(temp, temp, ret);

Out << "Case #" << h+1 << ": " << temp << endl;

}

In.close();

Out.close();

return 0;

}
 
