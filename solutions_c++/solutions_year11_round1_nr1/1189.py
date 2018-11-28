#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main()
{
	FILE *fin,*fout;
	fin=fopen("input.txt","r");
	fout=fopen("output.txt","w");
	int t;
	long long unsigned n,d;
	int pg,pd;
	fscanf(fin,"%d",&t);
	for(int i=0;i<t;i++)
	{
		fprintf(fout,"Case #%d: ",i+1);
		fscanf(fin,"%llu %d %d",&n,&pd,&pg);
		if(pg == 100 && pd != 100)
		{
			fprintf(fout,"Broken");			
		}
		else if(pg == 0  && pd != 0)
		{
			fprintf(fout,"Broken");
		}
		else if(pg == 0 && pd == 0)
		{
			fprintf(fout,"Possible");
		}		
		else
		{
			long long unsigned j;
             			for(j=n;j>=1;j--)
			{
				if((j*pd) % 100 == 0)
					break;
			}
			if(j!=0)
				fprintf(fout,"Possible");
			else
				fprintf(fout,"Broken");
		}
		if(i!=t-1)
			fprintf(fout,"\n");
	}
	return 0;
}