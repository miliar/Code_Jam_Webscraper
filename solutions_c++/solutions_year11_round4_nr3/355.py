#include <iostream>
#include <vector>
using namespace std ;
int main(){
	vector<int> primes ; 
	primes.push_back(2) ;
	primes.push_back(3) ;
	for(int i = 3 ; i < 1000000 ; i+=2){
		if(i % 6 != 1 && i % 6 != 5) continue ;
		bool check = true ;
		for(int j = 0 ; j < primes.size() ; j++){
			int p = primes[j] ;
			if(p * p > i) break ;
			if(i % p == 0){
				check = false ; break ;
			}
		}
		if(check) primes.push_back(i) ;
	}
	int T ; cin >> T ;
	for(int t = 1 ; t <= T ; t++){
		long long n ; cin >> n ;
		int ans = 1 ;
		for(int i = 0 ; i < primes.size() ; i++){
			int p = primes[i] ;
			if(n / p < p) break ;
			long long x = n ;
			while(x) x /= p , ans++ ;
			ans -= 2 ;
		}
		if(n == 1) ans = 0 ;
		printf("Case #%d: %d\n", t, ans) ;
	}

}
