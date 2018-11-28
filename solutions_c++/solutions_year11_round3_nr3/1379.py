#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <string>
using namespace std;
typedef long long int Int;
typedef vector<Int> vI;
typedef pair<Int,int> Ii;
typedef vector<Ii> vIi;

inline bool isdig(int a){return unsigned(a-'0') < 10;}
template<class T> static inline T getnum(){
   unsigned i; T j;
   do i = getchar(); while(!isdig(i));
   j = i-'0';  i=getchar() ;
   while(isdig(i)){ j = (j<<1)+(j<<3)+(i-'0'); i = getchar(); }
   return j;
}

Int GCD( Int a, Int b){
	if( a == 0LL) return b; if(b==0LL) return a;
	a = a<0LL?-a:a; b = b<0LL?-b:b;
	Int r; do { r = a %b; a = b; b = r; } while( r != 0LL ); 
	return a;
}
Int MCM( Int A, Int B){
	Int C = GCD(A,B);
	if( C == 0 ) return C;
	else return (A/C)*B;
}

// itera d a través de los divisores de n, donde f es un factor
// y j indica el número de divisor.
#define fordiv(d,f,j) for(int j=0, d=1; j<f.nd; d=f.div[++j])

char buf[100];

int main(int argc, char *argv[]){
	#ifndef ONLINE_JUDGE
		freopen("Aa.txt","r",stdin);
	#endif
	int nt = getnum<int>();

	for(int j = 1; j <= nt; ++j){
		int N = getnum<int>();
		Int L = getnum<Int>();
		Int H = getnum<Int>();
		bool found = false;
		vI P(N);
		vI mcm(N);
		vI gcd(N);
		for(int i = 0; i < N; ++i){
			P[i] = getnum<Int>();
		}
		sort(P.begin(), P.end());

		Int bst = 20000000000000000LL;
		for(int t = L; t <= H; ++t){
			int j = 0;
			bool ok = true;
			for(j = 0; j<N && P[j] <= t ; ++j) {
				if( t % P[j] != 0){
					ok = false; break;
				}
			}
			if(ok){
				for(; j<N ; ++j) {
					if( P[j]%t != 0){
						ok = false; break;
					}
				}
			}
			if( ok ) { bst = t; found = true; break;}
		}
/*
		mcm[0] = P[0], gcd[N-1] = P[N-1];
		for(int i = N-2; i >= 0; --i){
			gcd[i] = GCD(gcd[i+1],P[i]);
		}
		Int M = 1LL;
		int i = 0;
		Int bst = 20000000000000000LL;
		while( i< N ){
			if( gcd[i] >= L && gcd[i] % M == 0LL ){
				Int quot = gcd[i] / M;
				for(Int q = max(1LL,L/M); q*q < quot; q++){
					if( quot % q == 0LL && q * M <= H  && q * M >= L){
						found = true;
						if( q*M < bst) bst = q*M; 
						goto next;
					}
				}
			}
			next:			
			Int C = GCD( M, P[i] );
			if( double(M)*double(P[i]) / double(C)< 1e16)
				M = (M/C)*P[i];
			if(++i>=N) break;;
		}
*/
		printf( "Case #%d: ", j);
		if( !found) 
			printf( "NO\n");
		else {
			int j = 0;buf[j]='0';
			for(; bst > 0LL;){
				buf[j] = '0'+int( bst % 10LL);
				bst = bst /10LL;
				++j;
			}
			for(int k = j-1; k >= 0; --k)
				printf("%c", buf[k]);
			printf("\n");
		}
	}
	return 0;
}
