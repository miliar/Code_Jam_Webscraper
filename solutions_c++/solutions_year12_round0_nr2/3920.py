#include <cstdio>
#include <cstdlib>

int nbTests = 0 ;
int results[100] ;

int main() {
	scanf("%d", &nbTests) ;

	for (int i = 0 ; i < nbTests ; i++) {
		results[i] = 0 ;
	}

	for (int i = 0 ; i < nbTests ; i++) {
		int nbGooglers, nbSurprises, bestScore ;
		scanf("%d %d %d", &nbGooglers, &nbSurprises, &bestScore) ;
		
		int score ;
		for (int j = 0 ; j < nbGooglers ; j++) {
			scanf("%d", &score) ;
			
			if (score >= 3*bestScore - 2) {
				results[i]++ ;
			} else if (score >= 3*bestScore - 4 && nbSurprises > 0 && score >= bestScore) {
				results[i]++ ;
				nbSurprises-- ;
			}
		}
	}
	
	for (int i = 0 ; i < nbTests ; i++) {
		printf("Case #%d: %d\n", i+1, results[i]) ;
	}
}