#include <stdio.h>
#include <memory.h>
#include <string.h>

unsigned long grup[1000];
int main()
{

	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	unsigned long T,R,k,N,i,j,m;

	fscanf(fp, "%li", &T);
	for(i=1;i<=T;i++) 
	{
		fscanf(fp, "%li%li%li", &R,&k,&N);
		unsigned long long sum=0;
		for(j=0;j<N;j++)
			{
				fscanf(fp,"%li",&grup[j]);
			}
		
		unsigned  long x=0;
		for(j=1;j<=R;j++)
		{	
			unsigned long on_boad=0;
			for(m=1;(m<=N )and (on_boad+grup[x]<=k);m++)
				{  
				on_boad=on_boad+grup[x];
				x=x+1;
				if(x==N) {x=0;}
				}	
			sum+=on_boad;
			
		}
					
	 fprintf(ofp, "Case #%li: %lli\n", i,sum);
			
	}
	return 0;
}
