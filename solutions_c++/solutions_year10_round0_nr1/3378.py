#include<stdio.h>

int main()
{
	FILE *fin=fopen("input.txt","rt");
	FILE *fout=fopen("output.txt","wt");
	int T,K,N;
	fscanf(fin,"%d",&T);
	for(int i=1;i<=T;i++)
	{
		fscanf(fin,"%d%d",&K,&N);
		if((N+1) % (1<<K) == 0) fprintf(fout,"Case #%d: ON\n",i);
		else fprintf(fout,"Case #%d: OFF\n",i);
	}
	return 0;
}
