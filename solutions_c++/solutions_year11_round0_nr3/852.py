#include <stdio.h>
#include <string.h>
#include <stdlib.h>

FILE *fin,*fout;

int main(void)
{
	int i,j,N,sum,min,t,T,m;
	fin=fopen("c.in","r");
	fout=fopen("c.out","w+");
	fscanf(fin,"%d",&T);
	for(i=1;i<=T;i++)
	{
		fscanf(fin,"%d",&N);
		sum=0;
		min=10000005;
		t=0;
		for(j=1;j<=N;j++)
		{
			fscanf(fin,"%d",&m);
			t^=m;
			sum+=m;
			if(m<min)	min=m;
		}
		if(t!=0)
			fprintf(fout,"Case #%d: NO\n",i);
		else
			fprintf(fout,"Case #%d: %d\n",i,sum-min);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
