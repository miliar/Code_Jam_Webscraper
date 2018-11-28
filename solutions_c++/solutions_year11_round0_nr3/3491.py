
#include <stdio.h>
#include <iostream>

using namespace std ;

int main () {
	int n ;
	int a, sum, exor ;
	int Kases ;
	cin >> Kases ;
	for ( int kases = 1 ; kases <= Kases ; kases ++ ) {
		cin >> n ;
		int min = 100001 ;
		exor = 0 ;
		sum = 0 ;
		for ( int i = 0 ; i < n ; i ++ ) {
			cin >> a ;
			if ( a < min ) {
				min = a ; 
			}
			sum += a ;
			exor ^= a ;
		}
	 
		if ( exor == 0 ) {
			printf("Case #%d: %d\n",kases, sum-min);
		} else {
			printf("Case #%d: NO\n", kases ) ;
		}
	}
	return 0 ; 
}
