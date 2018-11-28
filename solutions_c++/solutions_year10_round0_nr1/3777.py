#include<stdio.h>
#include<stdlib.h>
#include<math.h>

long K;
int T,N,i;
FILE*f;
FILE*g;

void main()
{
f=fopen("input.txt", "r");
g=fopen("output.txt", "w");
fscanf(f,"%d", &T);
for(i=1;i<=T;i++)
	{
		fscanf(f,"%d %ld", &N, &K);
		if(K>=pow(2.0,N)-1 && (K+1)%(long)pow(2.0,N)==0)
			fprintf(g,"Case #%d: ON\n", i);
		else
			fprintf(g,"Case #%d: OFF\n", i);
	}
fcloseall();
}