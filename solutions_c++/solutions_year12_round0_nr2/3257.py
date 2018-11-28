#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){


	int n,s,p, i, t,j, vysledky[101],pocitadlo;
	double priemery[101],pom,pom1,pom2;

	scanf("%d", &t);

	for(j=1;j<=t;j++){

		scanf("%d %d %d", &n, &s, &p);

		for(i=0; i<n;i++){
			scanf("%d", &vysledky[i]);
		}

		pocitadlo = 0;

		for(i=0; i<n;i++){
			pom = float(vysledky[i])/3;
			priemery[i] = ceil(pom);
		}

		for(i=0; i<n;i++){
			if(priemery[i]>=p)
				pocitadlo++;
			if((priemery[i]+1==p) && s != 0 && priemery[i] != 0){

				pom1 = vysledky[i] - p;
				
				if((p - floor(pom1/2))<=2){
					pocitadlo++;
					s--;
				}
			}
		}

		printf("Case #%d: %d\n", j, pocitadlo);
	}

	return 0;
}