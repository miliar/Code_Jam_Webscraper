#include<stdio.h>
#include<memory.h>
#include<string.h>
#include<math.h>
#define MAX_TEST_CASES 50
#define MAX_NUM_GRP 1000
unsigned long int R[MAX_TEST_CASES],k[MAX_TEST_CASES],g[MAX_TEST_CASES][MAX_NUM_GRP];
int N[MAX_TEST_CASES];
int main()
{
	char filename[32];
	char infile[32], outfile[32];
	printf("Enter input filename(excluding the .in extension)\n");
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	int t,i;
	fscanf(fp, "%d", &t);
	for(i=0;i<t;i++) {
		unsigned long int income=0,total=0,triptotal=0;
		fscanf(fp, "%ld%ld%d", &R[i],&k[i],&N[i]);
		int j;
		for(j=0;j<N[i];j++) {
			fscanf(fp, "%ld", &g[i][j]);
			total+=g[i][j];
		}
		int c=0;
		for(j=0;j<R[i];j++) {
			if(total<k[i]) {
				triptotal=total;
				income=income+triptotal;
			} else { 	
				while(1) {
					if(c>=N[i])c=0;
					if((triptotal+g[i][c])>k[i])break;
					triptotal=triptotal+g[i][c];
				//	printf("%ld  ", g[i][c]);
					c++;
				}
				income=income+triptotal;
				//printf("\nTripTotal=%ld\n", triptotal);
				triptotal=0;
			}
		}
//		printf("Income=%ld\n", income);
		fprintf(ofp, "Case #%d: %ld\n", i+1, income);
	}
	fclose(fp);
	fclose(ofp);
	return 0;
}
