#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>
using namespace std;

#define FOR(i) for(int i = 0;  i< 3; ++i)
typedef  long long int Int;
char buf[1000];

bool isprime(Int q){
	if( q %2 == 0) return q==2;
	for(int p = 3; p*p <= q; p+=2){
		if( q%p == 0) return false;
	}
	return true;
}

int R[1000001], C[1000001];
static inline int getroot(int nd){
    for(; R[nd] != nd; nd=R[nd] ) R[nd] = R[R[nd]];
    return nd;
}
static inline void join(int nd1, int nd2){
    int r1 = getroot( nd1 ), r2 = getroot(nd2);
    if(r1 != r2) {
		if( C[r2] < C[r1] ) C[r1] += C[r2], R[r2] = r1;
        else                C[r2] += C[r1], R[r1] = r2;
	}
}



// usa la tabla lp[...] anterior para factorizar un número y encontrar sus divisores.
struct factor {
	Int pf[20],np,nd,lp;
	factor(Int n){
		memset( pf,0,sizeof(pf));np = 0;
		Int d = 2;
		for( ; d <= n; d++){
			if( n%d == 0 ) {
				while( n%d == 0 ){
					pf[np]=d; pf[np+1]++; n/=d;np+=2;
				}
			}
		}
	}
};

Int nsets(){
	Int A, B, P;
	for(int j = 0; j < 1000000; ++j) R[j] = j,C[j] = 0;
	gets(buf); sscanf(buf,"%lld %lld %lld",&A,&B,&P);
	for(Int x = A; x<= B; ++x){
		factor f(x);
		for(int j = 0; j < f.np; j+=2){
			Int p = f.pf[j];
			if( p >= P)
			for(Int y = x+p; y <= B; y+=p){
				join( x-A,y-A);
			}
		}
	}
	Int NT = 0;
	for(int t = A; t <= B; ++t){
		if( getroot(t-A) == t-A ) NT++;
	}
	return NT;
}

int main(){
	freopen("Bin.txt","r",stdin);
	freopen("Bout.txt","w",stdout);

	int N;
	gets(buf); sscanf(buf,"%d", &N);

	for(int nc = 1; nc <= N; ++nc){
		fprintf(stderr,"%d / %d ",nc,N);
		Int r = nsets();
		printf( "Case #%d: %lld\n", nc, r);
	}
}
