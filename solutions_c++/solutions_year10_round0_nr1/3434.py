/*
 * =====================================================================================
 *
 *       Filename:  snap.cpp
 *
 *    Description:  
 *
 *         Author:  Victor Carbune (victor.carbune@gmail.com)
 *	     Info:  Grupa 325, Seria CA
 *
 * =====================================================================================
 */


#include <stdio.h>


int main() {
	long long testcases, n, k, i;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%lld", &testcases);
	for ( i = 1; i <= testcases; i++) {
		scanf("%lld %lld", &n, &k);
		if ( k%(1<<n) == (1<<n) - 1)
			printf("Case #%lld: ON\n", i);
		else
			printf("Case #%lld: OFF\n", i);
	}

	return 0;
}
