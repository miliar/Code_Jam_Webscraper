#include <stdio.h>
#include <math.h>
#include <string.h>

long R;
long tmpR;
long K;
long N;
long M;

int main()
{

	char filename[32];
	char infile[32], outfile[32];
	
	//scanf("%s", filename);
	sprintf(filename,"%s", "C-small-attempt1");

	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int i, j;
	fscanf(fp, "%d", &M);



	long tmp[1024];
	long tmpsum = 0;
	long sum = 0;
	long summin = 0;
	for(i=1;i<=M;i++) {
		fscanf(fp, "%ld %ld %ld", &R, &K, &N);		//R = round  K = capacity N = length of the seqeunce
		tmpR = R;
		for(j=0;j<N;j++){
			fscanf(fp, "%ld", &tmp[j]);  //printf("read=%ld\n", tmp[j]);
		}

		j = -1;
		while(1){
			j = (j+1)%N;
			tmpsum+=tmp[j];

			if (tmpsum > K){
				j--;
				tmpsum = 0;
				R--;				
			}
			else {
				sum+=tmp[j];
				//printf("%ld\n", tmp[j]);
			}

			if(R==0) {

				for(j=0;j<N;j++){
				summin+= tmp[j];
				}
				
				#define min(a,b) (((a) < (b)) ? (a) : (b))
				fprintf(ofp, "Case #%d: %ld\n", i, min(sum,summin*tmpR));


				tmpsum = 0;
				sum = 0;
				summin = 0;
				break;
			}
			
		}

		//if ( K > ((int)pow((double)2,N)-1) ) //ON
		//	fprintf(ofp, "Case #%d: %s\n", i, "ON");
	}

	return 0;
}
