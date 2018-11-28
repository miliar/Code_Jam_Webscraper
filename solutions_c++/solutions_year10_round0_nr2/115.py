#include<iostream>
#include<gmp.h>
using namespace std ;
main()
{

	int C, N;
	cin >> C;
	for(int cas=0;  cas<C ; cas++)
	{
		mpz_t gcd, intermediaire, t1plusT, t[1000] ; 
		mpz_init(gcd);
		mpz_init(intermediaire);
		mpz_init(t1plusT);
		cin >> N;
	       	char truc[100];	
		for(int j = 0 ; j< N ; j++)
		{
			cin >> truc ;
			mpz_init(t[j]);
			mpz_set_str(t[j], truc, 10 ) ;
		}
		mpz_sub(gcd, t[0], t[1]);
		mpz_abs(gcd,gcd);
		for(int i = 1 ; i< N-1 ; i++)
		{
			mpz_sub(intermediaire, t[i], t[i+1]);
			mpz_abs(intermediaire, intermediaire);
			mpz_gcd(gcd , gcd , intermediaire);
		}
		mpz_add(t1plusT, t[0] , gcd) ;
		mpz_mod(intermediaire, t1plusT, gcd);
		mpz_sub(intermediaire, gcd , intermediaire) ;
		//cout << "GCD : " ;
		//mpz_out_str(stdout, 10,  gcd);
		//cout << endl; 
		cout << "Case #" << cas+1 << ": ";
		if(mpz_cmp_ui(gcd, 1) == 0)
			cout << 0 ;
		else
			if(mpz_cmp(gcd, intermediaire ) == 0)
				cout << 0 ;
			else
				mpz_out_str(stdout, 10, intermediaire);
		cout << endl;
		

	}
	return 0;
}

