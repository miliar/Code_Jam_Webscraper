//* uses the publicly avaliable library gmp. See http://gmplib.org/
//* compile with  -lgmp
//*

#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <gmp.h>
using namespace std;


inline bool isdig(int a){return unsigned(a-'0') < 10;}
template<class T> static inline T getnum(){
   unsigned i; T j;
   do i = getchar(); while(!isdig(i));
   j = i-'0';  i=getchar() ;
   while(isdig(i)){ j = (j<<1)+(j<<3)+(i-'0'); i = getchar(); }
   return j;
}

bool mpz_less( mpz_t *z1, mpz_t *z2){
	return mpz_cmp(*z1, *z2) < 0;
}

void prt( mpz_t z){
	char out[100];
	 mpz_get_str( out, 10, z);
	printf("%s\n",out);
	fflush(stdout);
}

mpz_t n[1000], *s[1000];
char out[60000];

int main(int argc, char *argv[]){
	#ifndef ONLINE_JUDGE
		freopen("Bb.txt","r",stdin);
	#endif
	int nt = getnum<int>();
	for(int j = 1; j <= nt; ++j){
		unsigned N = getnum<unsigned>();
		for(int nn = 0; nn < N; ++nn){
			mpz_init( n[nn] );
			s[nn] = n+nn;
		}
		memset(out,0,sizeof(out));
		gets( out ); char *p=out, *q;
		for(int nn = 0; nn < N; ++nn){
			while(*p == ' ') p++;
			q = p;
			while(*q != ' ' && *q != '\r' && *q!='\n') q++;
			*q = 0;
			mpz_set_str(n[nn], p, 10);
			p = q+1;
		}
		std::sort( s, s+N, mpz_less );
		mpz_t g, h; mpz_init(g);mpz_init(h);
		mpz_sub( g, *s[1], *s[0] );
		for(int nn = 2; nn < N; ++nn){
			mpz_sub( h, *s[nn], *s[nn-1] );
			mpz_gcd( g, g, h );
		}
		mpz_t m; mpz_init(m);
		mpz_t d; mpz_init(d );
		mpz_sub_ui( m, *s[N-1], 1u);
		mpz_add(m,m,g);
		mpz_fdiv_q( d, m, g); mpz_mul( d, d, g); mpz_sub( d, d, *s[N-1] );
		printf( "Case #%d: ", j); prt( d);
		mpz_clear( g);
		mpz_clear( h);
		mpz_clear( m);
		mpz_clear( d);
		for(int nn = 0; nn < N; ++nn)
			mpz_clear( n[nn] );
	}
}
