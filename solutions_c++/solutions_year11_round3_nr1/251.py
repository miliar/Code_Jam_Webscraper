
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

char table[51][51] ;

void solve ( void ) { 
	int R, C ;
	cin >> R >> C ;
	int count = 0 ; 
	for ( int i = 0 ; i < R ; i ++ ) {
		scanf("%s", table[i] ) ;
		for ( int j = 0 ; j < C ; j ++ ) {
			if ( table[i][j] == '#' ) { count ++ ; } 
		}
	}
	if ( count % 4 !=  0 ) { printf ("Impossible\n") ;return ; } 
	for ( int i = 0 ; i < R-1 ; i ++ ) {
		for ( int j = 0 ; j < C-1 ; j ++ ) {
			if ( table[i][j] == '#' ) {
				if ( table[i][j+1] == '#' && table[i+1][j] == '#' && table[i+1][j+1] == '#' ) {
					table[i][j] = table[i+1][j+1] = '/' ;
					table[i][j+1] = table[i+1][j] = '\\' ;
				} else { 
					printf("Impossible\n") ;
					return ; 
				}
			}
		}
	}

	for ( int i = 0 ; i < R ; i ++ ) {
		if ( table[i][C-1] == '#' ) { 
			printf("Impossible\n") ;
			return ; 
		}
	}
	for ( int j = 0 ; j < C ; j ++ ) {
		if ( table[R-1][j] == '#' ) {
			printf("Impossible\n") ;
			return ; 
		}
	}

	for ( int i = 0 ; i < R ; i ++ ) {
		for ( int j = 0 ; j < C ; j ++ ) {
			printf("%c",table[i][j] ) ;
		}
		putchar(10) ;
	}
	return ;
}

int main () {
	int Kases ;
	cin >> Kases ; 
	for ( int kases = 1 ; kases <= Kases ; kases ++ ) {
		printf("Case #%d:\n", kases ) ;
		solve() ;
	}
	return 0 ;
}
