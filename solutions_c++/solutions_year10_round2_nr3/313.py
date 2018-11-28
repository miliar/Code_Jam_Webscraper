#include <iostream>
#include <algorithm>
#define p 100003 
using namespace std ;
int dp[510][510] ;
int c[510][510] ;
int choice(int n , int k){
	if(c[n][k] != 0) return c[n][k] ;
	if(n == k || k == 0) return 1 ;
	return c[n][k] = (choice(n-1,k) + choice(n-1,k-1)) % p ;
}
int f(int n , int rank){
	if(dp[n][rank] != 0) return dp[n][rank] ;
	if(rank == 1) return 1 ;
	int ans = 0 ;
	for(int i = max(1,rank - (n-rank)); i<rank ; i++){
		ans = (ans + f(rank,i) * choice(n-rank-1,rank-i-1)) % p ;
	}
	return dp[n][rank] = ans ;
}
int result(int n){
	int ans = 0 ;
	for(int i = 1 ; i < n ; i++)
		ans = (ans + f(n,i)) % p ;
	return ans ;
}
int main(){
	int T ; cin >> T ;
	for(int t = 1 ; t <= T ; t++){
		int n ; cin >> n ;
		cout << "Case #" << t << ": " << result(n) << endl ;
	}
}
