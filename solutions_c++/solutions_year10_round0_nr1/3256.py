#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int main (int argc, char * const argv[]) {
	FILE *fpi, *fpo;
	int num, n, k;
	double p, q;
	char home[512];
	
	strcpy(home, getenv("HOME"));
	if ((fpi = fopen(strcat(home, "/temp/A-large.in.txt"), "r")) == NULL){

		printf("error\n");
		exit(11);
	}

	strcpy(home, getenv("HOME"));
	if ((fpo = fopen(strcat(home, "/temp/out_A_large.txt"), "w")) == NULL){
		printf("error\n");
		exit(10);
	}
	
	fscanf(fpi, "%d", &num);
	for(int i=1; i<=num; i++){
		fscanf(fpi, "%d %d", &n, &k);
		
		p = k +  1.0;
		q = pow(2.0, n);
		
		if(fmod(p, q) == 0 && k != 0)
			fprintf(fpo, "Case #%d: ON\n", i);
		else
			fprintf(fpo, "Case #%d: OFF\n", i);
	}
	
    return 0;
}
