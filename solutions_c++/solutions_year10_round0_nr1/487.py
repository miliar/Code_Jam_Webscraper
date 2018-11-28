#include<stdio.h>
#include<memory.h>
#include<string.h>
int TestNo;
int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int i, N;
    long K, pattern , result;
	int cnt;
	fscanf(fp, "%d", &TestNo);
	for(i=1;i<=TestNo;i++)
    {
       fscanf(fp, "%d%d", &N,&K);
       pattern = (((long)1 << N) - 1 );
       result = K & pattern;
       if (result == pattern)
       {
           fprintf(ofp, "Case #%d: ON\n", i);
       }
       else
       {
           fprintf(ofp, "Case #%d: OFF\n", i);
       }
    }
	return 0;
}
