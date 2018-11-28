#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int nf[10000];

int main()
{
	FILE *fin,*fout;
	fin=fopen("input.txt","r");
	fout=fopen("output.txt","w");
	int t;
	int n;
	long long l,h;
	fscanf(fin,"%d",&t);
	for(int i=0;i<t;i++)
	{
		fprintf(fout,"Case #%d: ",i+1);
		fscanf(fin,"%d %lld %lld",&n,&l,&h);
	
		for(int j=0;j<n;j++)
		{
			fscanf(fin,"%d",&nf[j]);			
		}
		int done=0;
		for(long long k=l;k<=h;k++)
		{
			int f=1;
			for(int j=0;j<n;j++)
			{
				if(k % nf[j] != 0 && nf[j] % k != 0)
				{
					f=0;
					break;
				}
			}
			if(f)
			{
				fprintf(fout,"%lld",k);
				done = 1;
				break;
			}			
		}
		
		if(!done)
		{
			fprintf(fout,"NO");
		}
		if(i!=t-1)
			fprintf(fout,"\n");
	}
	return 0;
}