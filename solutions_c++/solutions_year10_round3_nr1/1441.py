#include <stdio.h>
#include <memory.h>
#include <string.h>

int main()
{

	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");


	unsigned int T,N,i,j,k;

	fscanf(fp, "%u", &T);
	for(i=1;i<=T;i++) 
	{
		fscanf(fp, "%u", &N);
		int A[N] ,B[N];
		for(j=1;j<=N;j++)
		{fscanf(fp, "%u%u", &A[j-1],&B[j-1]);
		}
		int sum=0;
		for(j=1;j<N;j++)
		{ for(k=j+1;k<=N;k++)
			{if((A[k-1]-A[j-1])*(B[k-1]-B[j-1])<0) 
				sum=sum+1;}
                }
		if(N==1) fprintf(ofp, "Case #%u: 0\n",i);
		else {fprintf(ofp, "Case #%u: %d\n",i,sum);}
	}
	return 0;
}
