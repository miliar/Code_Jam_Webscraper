#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std ;
#define fo(i,a,b) for ( int i = a ; i <= b ; i ++ )
#define fi(i,a,b) for ( int i = a ; i >= b ; i -- )
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define MEM(a) memset(a,0xff,sizeof(a))
#define MaxN 600000+13
int N , d ;
int A[MaxN] , B[MaxN] , opt[MaxN] , nx[MaxN] ;
int GetNext(int p) { return opt[nx[p]] < 0 ? nx[p] : nx[p] = GetNext(nx[p]) ; }
void Init() { cin >> N ; fo(i,1,N) cin >> A[i] >> B[i] ; cin >> d ; }
void Solve() {
	MEM(opt) ; opt[1] = A[1] ; A[N+1] = d ; B[N+1] = A[N+2] = 0x7FFFFFFF ;
	fo(i,1,N+1) nx[i] = i+1 ;
	fo(i,1,N) for ( int j = GetNext(i) ; A[j] <= A[i] + opt[i] ; j = GetNext(j) ) opt[j] = min(A[j]-A[i] , B[j]) ;
	if ( opt[N+1] >= 0 ) puts("YES") ; else puts("NO") ;
}
int main() {
	freopen("A.in" , "r", stdin ) ; freopen("A.out", "w", stdout) ;
	int Test ; cin >> Test ;
	fo(i,1,Test) {
		printf( "Case #%d: " , i ) ; Init() ; Solve() ;
	}
}