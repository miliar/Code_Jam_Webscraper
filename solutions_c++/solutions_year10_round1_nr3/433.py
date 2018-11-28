#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std ;

#define FOR(i, n) for(int i = 0 ; i < (n) ; i++)

int a1, a2, b1, b2, ans ;

bool gcd(int a, int b){
	if ( a == 0 ) return true ;
	if ( gcd(b % a, a) == true ){
		if (b / a > 1) return true ;
		return false ;
	}else{
		return true ;
	}
}

int main(){
	int T ; scanf(" %d", &T) ;
	for(int q = 0 ; q < T ; q++){
		int ans = 0 ;
		scanf(" %d %d %d %d", &a1, &a2, &b1, &b2) ;
		for(int i = a1 ; i <= a2 ; i++)
			for(int j = b1 ; j <= b2 ; j++)
				if ( i != j && gcd(min(i, j), max(i, j)) ){
					ans ++ ;
				}
		cout << "Case #" << q + 1 << ": " << ans << endl ;
	}
}
