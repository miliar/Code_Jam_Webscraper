#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <iostream>
#include "gmp.h"

using namespace std ;

int K;
mpz_t Arr[100];

void Solve(int KKK)
{
	scanf("%d",&K);
	for (int i=1;i<=K;++i)
		mpz_init(Arr[i]);
	for (int i=1;i<=K;++i)
		gmp_scanf("%Zd",&Arr[i]);
	mpz_t MAX,Tmp;
	mpz_init(MAX);
	mpz_init(Tmp);
	mpz_sub(MAX,Arr[2],Arr[1]);
	for (int i=2;i<K;++i)
	{
		mpz_sub(Tmp,Arr[i+1],Arr[i]);
		if (mpz_sgn(Tmp)!=0)
			mpz_gcd(MAX,MAX,Tmp);
	}
	mpz_abs(MAX,MAX);
	mpz_mod(Tmp,Arr[1],MAX);
	if (mpz_sgn(Tmp)!=0)
		mpz_sub(Tmp,MAX,Tmp);
	gmp_printf("Case #%d: %Zd\n",KKK,Tmp);
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int Test;
	scanf("%d",&Test);
	for (int i=1;i<=Test;++i)
		Solve(i);
	return 0;
}