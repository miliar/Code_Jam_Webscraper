#include <stdio.h>
#include <math.h>
#include <string.h>


long T;
long N;
long m;
long data[1000];
long ctr, intersec;

int main()
{
	ctr = intersec = 0;
	char filename[32];
	char infile[32], outfile[32];
	//scanf("%s", filename);
	sprintf(filename,"%s", "A-large");

	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	
	fscanf(fp, "%d", &T);

	for(long i = 0; i< T; i++){
		fscanf(fp, "%d", &N);
		for(long j = 0; j< N; j++){
			long A[1000],B[1000],tmpA, tmpB;

			fscanf(fp, "%ld", &A[j]);
			fscanf(fp, "%ld", &B[j]);
			
			if(j>0){
				for(long k = 0; k< j; k++){
					if(A[j]<A[k] && B[j]>B[k]) intersec++;
					if(A[j]>A[k] && B[j]<B[k]) intersec++;
				}
			}
		}
		//printf("Case #%d: %d\n",i,intersec);intersec = 0;
		fprintf(ofp, "Case #%d: %d\n",i+1,intersec);intersec = 0;
	}

	return 0;
}
