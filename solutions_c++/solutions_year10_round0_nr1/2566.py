// prelim_a.cpp : Defines the entry point for the console application.
//

#include<stdio.h>
#include<memory.h>
#include<string.h>

int n, k;

int powerOfTwo(int power){
	if(power == 0) return 1;
	int result = 1;
	int i;
	for(i=1; i<=power; i++){
		result = result * 2;
	}
	return result;
}

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int tc, i, j, p2, on, rem;
	fscanf(fp, "%d", &tc);

	for(i=1; i<=tc; i++){
		fscanf(fp, "%d %d", &n, &k);
		p2 = powerOfTwo(n);
		rem = k % p2;
		if(rem == p2 -1) fprintf(ofp, "Case #%d: ON\n", i);
		else fprintf(ofp, "Case #%d: OFF\n", i);

	}

	return 0;
}

