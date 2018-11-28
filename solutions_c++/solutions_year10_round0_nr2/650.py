#include <cstdio>
#include <iostream>
#include <gmpxx.h>

using namespace std;

void resoud(){
	mpz_class T,debut,cur,pgcd;
	int N;
	scanf("%d",&N);
	cin>>debut;
	for (int i=1;i<N;i++){
		cin>>cur.get_mpz_t();
		cur-=debut;
		if (cur<0) cur=-cur;
		if (i==1)
			pgcd=cur;
		else
			mpz_gcd (pgcd.get_mpz_t(), pgcd.get_mpz_t(), cur.get_mpz_t());
	}
	mpz_class res=(pgcd-(debut%pgcd))%pgcd;
	cout<<res.get_mpz_t()<<endl;
}

int main(){
	int T;
	scanf("%d",&T);
	for (int i=0;i<T;i++){
		printf("Case #%d: ",i+1);
		resoud();
	}
}
