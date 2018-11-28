#include<stdio.h>
#include<memory.h>
#include<string.h>
#include<math.h>
long long int n, m;
long int r;

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");

	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
 
	long int i, j, tc;
	fscanf(fp, "%ld", &r);
	
	for(i=1;i<=r;i++) 
{

           fscanf(fp, "%Ld%d", &n,&m);

long long int zo = pow(2,n);

long long int sd = (m+1)%zo;

	if(sd == 0)
		fprintf(ofp, "Case #%d: %s\n", i, "ON");
     else
           fprintf(ofp, "Case #%d: %s\n", i, "OFF");
	}
	return 0;
}
