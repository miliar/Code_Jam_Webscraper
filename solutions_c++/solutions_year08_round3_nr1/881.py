#include<stdio.h>
#include <stdlib.h>
#include<algorithm>
FILE *fin,*fout;
int main()
{
	fin = fopen("A-small-attempt1.in","r");
	fout = fopen("A1.out","w");
	int test;
	fscanf(fin,"%d\n",&test);
	for(int z=1;z<=test;z++)
	{
		unsigned long int p,k,l,*fre;
		unsigned int keys[1000][1000];
		fscanf(fin,"%lu %lu %lu\n",&p,&k,&l);
		fre = (unsigned long int *)malloc(sizeof(unsigned long int)*l);
		for(int i =0;i<l;i++)
			fscanf(fin,"%lu%*c",&fre[i]);
		sort(&fre[0],&fre[l]);
		//for(int i =0;i<l;i++)
			//printf("%d\n",fre[i]);
		unsigned long int max = 0;
		int freq=l-1;
		for(int i=0;i<p;i++)
		{
			for(int j =0;j<k;j++)
			{
				if(freq<l)
				{
				max+=(fre[freq]*(i+1));
				//printf("%d %d\n",i+1,max);
				}
				freq--;
			}
		}
		fprintf(fout,"Case #%d: %lu\n",z,max);
		free(fre);
		//getchar();
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
