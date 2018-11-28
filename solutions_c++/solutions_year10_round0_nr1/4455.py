#include <iostream.h>
#include <conio.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
long unsigned int K,N,one=1L,n;

int main()
{
	FILE *in,*out;
	int ncases,c,i,j,k;
	in=fopen("as.in","r+");
	out=fopen("out.txt","w+");
	fscanf(in,"%d",&ncases);
	for(c=0;c<ncases;c++)
	{
		fscanf(in,"%ld\n",&N);
		fscanf(in,"%d\n",&n);
		K=0;
		for(i=0;i<N;i++)
			K|=(one<<i);
		printf("%ld %ld",K,N);
		if((n&K)==K)
			fprintf(out,"Case #%d: ON\n",c+1);
		else
			fprintf(out,"Case #%d: OFF\n",c+1);
	}
	fclose(in);
	fclose(out);
	clrscr();
	return 0;
}