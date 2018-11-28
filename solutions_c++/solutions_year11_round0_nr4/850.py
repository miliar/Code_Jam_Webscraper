#include <stdio.h>
#include <string.h>
#include <stdlib.h>

FILE *fin,*fout;

int main(void)
{
	int i,j,N,T,t;
	int ori[1005];
	fin=fopen("d.in","r");
	fout=fopen("d.out","w+");
	fscanf(fin,"%d",&T);
	for(i=1;i<=T;i++)
	{
		fscanf(fin,"%d",&N);
		t=0;
		for(j=1;j<=N;j++)
			fscanf(fin,"%d",ori+j);
		for(j=1;j<=N;j++)
			if(ori[j]!=j)
				t++;
		fprintf(fout,"Case #%d: %.6f\n",i,(float)t);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
