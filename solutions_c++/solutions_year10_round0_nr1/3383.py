// codejam_Q1_qualification.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <math.h>
#include <string.h>


long m;
long N;
long K;

int main()
{

char filename[32];
char infile[32], outfile[32];
//scanf("%s", filename);
sprintf(filename,"%s", "A-large");

strcpy(infile, filename); strcpy(outfile, filename);
strcat(infile, ".in"); strcat(outfile, ".out");
FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

int i, j;
int cnt;
fscanf(fp, "%d", &m);
for(i=1;i<=m;i++) {
fscanf(fp, "%d %d", &N, &K);
if ( (K+1)%((long)pow((double)2,N)) == 0) //ON
//if ( K > ((int)pow((double)2,N)-1) ) //ON
fprintf(ofp, "Case #%d: %s\n", i, "ON");
else
fprintf(ofp, "Case #%d: %s\n", i, "OFF");
}

return 0;
}

