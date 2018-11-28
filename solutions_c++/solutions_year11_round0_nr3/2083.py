//I write the problem to test the python scripts
//It seems download - test - submit can be fully automated
//Hope it works this time

#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <map>
#include <string>
#include <set>
#include <vector>

using namespace std ;

const int MAX_C = 1000001 ;

int main(){
	int i, cs, T, N ;
	int min, sum, cur ;
	scanf("%d", &T) ;
	for ( cs = 1 ; cs <= T ; cs ++ ){
		min = MAX_C ; 
		sum = 0 ;
		cur = 0 ;
		scanf("%d", &N) ;
		for ( i = 0 ; i < N ; i ++ ){
			int t ;
			scanf("%d", &t) ;
			sum += t ;
			cur ^= t ;
			if ( t < min ){
				min = t ;
			}
		} 
		if ( cur == 0 ) {
			printf("Case #%d: %d\n", cs, sum - min) ;
		} else {
			printf("Case #%d: NO\n", cs) ;
		}
	}
	return 0 ;
}
