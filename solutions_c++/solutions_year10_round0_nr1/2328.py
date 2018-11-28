#include <stdio.h>

#define MAX 25

int main() {
	unsigned long T, N, K;


	unsigned long M[MAX];
	M[0] = 1;
	for(int i = 1; i < MAX; i++) {
		M[i] = (M[i-1])*2;
		//printf("%ld\n", M[i]);
	}
	

	FILE *infile;
	infile = freopen("A-small-attempt1.in", "r", stdin);

	FILE *outfile;
	outfile = fopen("a1.out", "w");

	scanf("%ld", &T);
	unsigned long tmp;
	for(int cs = 0; cs < T; cs++) {
		scanf("%ld %ld", &N, &K);
		if(K < M[N] - 1) {
			printf("Case #%ld: OFF\n", cs+1);
			fprintf(outfile,"Case #%ld: OFF\n", cs+1); 
		}
		else {
			tmp = M[N] -1;
			if( (K- tmp) % M[N] == 0) {
				printf("Case #%ld: ON\n", cs+1);
				fprintf(outfile,"Case #%ld: ON\n", cs+1);
			}
			else {
				printf("Case #%ld: OFF\n", cs+1);
				fprintf(outfile,"Case #%ld: OFF\n", cs+1);
			}
		}
	}
	
}