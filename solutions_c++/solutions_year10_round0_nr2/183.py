//Jakub Sygnowski
#include <cstdio>
#include <gmp.h> // http://gmplib.org/
#include <algorithm>
using namespace std;
#define REP(I,N) for(int I=0;I<(N);I++)
#define ALL(X) (X).begin(),(X).end()
mpz_t tab[1007];
char tt[54];
int n,t;
mpz_t nwd,temp;
bool obr;
int main(){
	scanf("%d",&t);
	REP(nr,t){
		printf("Case #%d: ",nr+1);
		scanf("%d",&n);
		REP(i,n){
		       scanf("%s",tt);
		       mpz_set_str(tab[i],tt,10);
		}
		obr=true;
		while(obr){
		obr=false;
		REP(i,n-1){
			if (mpz_cmp(tab[i],tab[i+1])>0){
				obr=true;
				mpz_swap(tab[i],tab[i+1]);
			}
		}
		}
		mpz_sub(nwd,tab[1],tab[0]);
		for(int i=2;i<n;i++){
	//		mpz_out_str(stdout,10,tab[i]);
	//		printf(" ");
			mpz_sub(temp,tab[i],tab[i-1]);
			mpz_gcd(nwd,nwd,temp);
		}
	//	printf("\n");
	//	mpz_out_str(stdout,10,nwd);
	//	printf("\n");
		if (!mpz_cmp(nwd,tab[0]))
			printf("0\n");
		else {
			mpz_mod(temp,tab[0],nwd);
	//		mpz_out_str(stdout,10,temp);
			mpz_sub(temp,nwd,temp);
			mpz_mod(temp,temp,nwd);
//			mpz_sub(nwd,nwd,temp);
			mpz_out_str(stdout,10,temp);
			printf("\n");
		}
	}
}
