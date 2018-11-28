
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>

using namespace std ;

typedef long long ll ;

ll gcd ( ll a, ll b ) { return b ? a : gcd(b, a%b) ; }
ll MAX ( ll a, ll b ) { return a > b ? a : b ; }
ll MIN ( ll a, ll b ) { return a < b ? a : b ; }
ll lcm ( ll a, ll b ) { return (a*b) / gcd(a,b) ; }

int a[1000] ;

void solve ( void ) {
	int N , L , H ; 
	cin >> N >> L >> H ;
	for ( int i = 0 ; i < N ; i ++ ) { cin >> a[i] ; } 
	for ( int i = L ; i <= H ; i ++ ) {
		bool done = true ; 
		for ( int j = 0 ; j < N ; j ++ ) {
			if ( i%a[j] == 0 || a[j]%i == 0 ) { } 
			else { done = false ; break ;} 
		}
		if ( done ) {
			printf("%d\n", i ) ;
			return ;
		}
	}
	printf("NO\n") ;
	return ;
}

int main () {
	int Kases ;
	cin >> Kases ; 
	for ( int kases = 1 ; kases <= Kases ; kases ++ ) {
		printf("Case #%d: ", kases ) ;
		solve() ;
	}
	return 0 ;
}
