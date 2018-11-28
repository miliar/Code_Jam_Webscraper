
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

char table[101][101] ;
double wp[101] ; 
int wp_demon [101] ;
int wp_numer [101] ; 
double owp[101] ;
double oowp[101] ;

int main () {
	int Kases ;
	cin >> Kases ; 
	int n ; 
	for ( int kases = 1 ; kases <= Kases ; kases ++ ) {
		cin >> n ;
		for ( int i = 0 ;i < n ; i ++ ) { scanf("%s",table[i] ) ; }
		for ( int i = 0 ; i < n ; i ++ ) {
			wp_demon[i] = wp_numer[i] = 0 ;
			for ( int j = 0 ; j < n ; j ++ ) {
				if ( table[i][j] == '0' ) { wp_demon[i] ++ ; } 
				else if ( table[i][j] == '1' ) { wp_demon[i] ++ ; wp_numer[i] ++ ; } 
			}
			wp[i] = (1.0*wp_numer[i]) / (1.0*wp_demon[i]) ; 
		}
		
		for ( int i = 0 ; i < n ; i ++ ) {
			owp[i] = 0.0 ;
			int count = 0 ; 
			for ( int j = 0 ; j < n ; j ++ ) {
				if ( table[j][i] == '0' ) { owp[i] += ((1.0*wp_numer[j])/(1.0*(wp_demon[j]-1))) ;  count ++ ; } 
				else if ( table[j][i] == '1' ) { owp[i] += ((1.0*(wp_numer[j]-1))/(1.0*(wp_demon[j]-1))) ;  count ++ ; }
			}
			owp[i] /= count ;
		}

		for ( int i = 0 ; i < n ; i ++ ) {
			oowp[i] = 0.0 ;
			int count = 0 ;
			for ( int j = 0 ; j < n ; j ++ ) {
				if ( table[j][i] != '.' ) {
					oowp[i] += owp[j] ;
					count ++ ; 
				}
			}
			oowp[i] /= count ;
		}

		printf("Case #%d:\n", kases ) ;
		for ( int i = 0 ; i < n ; i ++ ) {
			printf("%lf\n", 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i] ) ;
		}
	}
	return 0 ;
}
