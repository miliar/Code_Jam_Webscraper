#include "stdio.h"
#include "stdlib.h"
#include "memory.h"

#define FILE_NAME "C-small-attempt0"

#define INPUT_FILE(x) x##".in"
#define OUTPUT_FILE(x) x##".out"

FILE *fi,*fo;

void problem()
{
	int n,K;
	int res=0;
	int *x,*p;
	int i,j,l;
	fscanf(fi,"%d\n",&K);
	fscanf(fi,"%d ",&n);
	x=new int[n];
	p=new int[K];
	for (i=0;i<K;++i)
		p[i]=0;
	for (i=0;i<n;++i)
	{
		fscanf(fi,"%d",&(x[i]));
	}
	l=0;
	for (i=1;i<=K;++i)
	{
		for (j=1;j<i;++j)
		{
			++l;
			l%=K;
			while (p[l]!=0)
			{
				++l;
				l%=K;
			}
		}
		p[l]=i;
		if (i<K)
		while (p[l]!=0)
		{
			++l;
			l%=K;
		}
	}
	for (i=0;i<n;++i)
	{
		if(i>0)
			fprintf(fo," ");
		fprintf(fo,"%d", p[x[i]-1]);
	}
	delete []x;
	delete []p;
}

void main()
{
	int N,i;
	fi = fopen(INPUT_FILE(FILE_NAME),"rt");
	fo = fopen(OUTPUT_FILE(FILE_NAME),"wt");
	fscanf(fi,"%d\n",&N);
	for (i=0;i<N;++i)
	{
		fprintf(fo,"Case #%d: ",i+1);
		problem();
		fprintf(fo,"\n");
	}
	fclose(fo);
	fclose(fi);
}