#include <stdio.h>
#include <stdlib.h>

#define MAX 100000000
//#define MAX 	100
#define MAXN 	32

typedef struct{
	int n;
	int k;
	int casen; // case number
}SET;

int SETcmp(const void *a, const void *b){
	return ( ((SET *)a)->k  - ((SET *)b)->k  );
}

main(){
	int n,t,c=0,p=0,i,j,k;

	scanf("%d\n", &t);

	SET input[t];
	bool *solns = (bool *)calloc(t, sizeof(bool));

	for(i=0;i<t;i++){
		scanf("%d %d", &input[i].n, &input[i].k);
		input[i].casen = i+1;
	}

	qsort(input, t, sizeof(SET), SETcmp );
		
	bool *s = (bool *)calloc(MAXN , sizeof(bool));

	for (j=0;j<=MAX;j++){

		for(;c<=t && input[c].k<=j; c++){
			if (input[c].k == j){
				if (s[input[c].n-1] && p>=(input[c].n-1) ){
					solns[input[c].casen] = true;
				}
			}
		}

		for (i=0;i<=p;i++) s[i] = !s[i];

		for (i=0;i<(MAXN-1) && s[i];i++);
		p = i;

	}
		
	for(i=1;i<=t;i++){
		printf("Case #%d: ", i);
		printf( (solns[i]) ? "ON" : "OFF");
		printf("\n");
	}

	free(s);
	free(solns);


}
