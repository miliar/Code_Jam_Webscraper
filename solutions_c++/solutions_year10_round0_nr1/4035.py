#include<stdio.h>
#include<string.h>
#include <math.h>
unsigned long t, n;
unsigned long k;
int main()
{
 	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename);
    strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	
	fscanf(fp, "%d", &t);
	for(int tc=1;tc<=t;tc++)
	{
        fscanf(fp, "%d %ld", &n, &k);
        fprintf(ofp, "Case #%d: %s\n", tc,  ( (k+1)% ((long)(pow(2,n))) == 0) ? "ON" : "OFF" );
	}
	return 0;
}
