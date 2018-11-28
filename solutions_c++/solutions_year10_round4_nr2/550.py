#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std ;

const long long Max_N = 4 * 1024 + 105 ;
#define FOR(i, n) for(long long i = 0 ; i < (n) ; i++)
#define SZ(x) (int)x.size()
#define PB push_back

long long n, p, Min[Max_N][Max_N], prc[Max_N], M[Max_N], ans[Max_N][30], Sum ;

void input(){
	FOR(i, Max_N) FOR(j, Max_N) Min[i][j] = 0 ;
	FOR(i, Max_N) FOR(j, 30) ans[i][j] = M[i] = prc[i] = Sum = 0 ;
	//-----------------------------------
	scanf(" %lld", &p); n = 1 << p ; 
	//-----------------------------------
	for(long long i = 0 ; i < n ; i++)
		scanf(" %lld", &M[i]) ;
	for(long long i = 0 ; i < n ; i++)
		for(long long j = i ; j < n ; j++)
			Min[i][j] = *min_element(M + i, M + j + 1) ;
	//-----------------------------------
	for(long long i = p-1 ; i >= 0 ; i--){
		for(long long j = 0 ; j < (1 << i) ; j++){
			long long id = (1 << i) + j ;
			scanf(" %lld", &prc[id]) ;
			Sum += prc[id] ;
		}
	}
	n = 1 << (p+1) ;
	//-----------------------------------
	FOR(i, n) FOR(j, p) ans[i][j] = -1 ;
}

long long getMin(long long v){
	long long L = v, R = v ;
	while(L * 2 < n) L = 2 * L ; 
	while(R * 2 + 1 < n) R = 2 * R + 1 ;
	//-----------------------------------
	return Min[L - n/2][R - n/2];
}

long long solve(long long v, long long k){
	if ( v >= n ) return 0 ;
	if ( ans[v][k] != -1 ) return ans[v][k] ;
	//-------------------------------------
	long long m = getMin(v) - k, ret = 0, L = 2 * v, R = 2 * v + 1 ;
	ret = max(ret, solve(L, k) + solve(R, k)) ; 
	if ( m != 0 )
		ret = max(ret, prc[v] + solve(L, k+1) + solve(R, k+1)) ;
	return (ans[v][k] = ret);
}

int main(){
	long long t ; scanf(" %lld", &t) ;
	for(long long tst = 0 ; tst < t ; tst++){
		input() ;
		printf("Case #%lld: %lld\n", tst+1, Sum - solve(1, 0)) ;
	}
}
