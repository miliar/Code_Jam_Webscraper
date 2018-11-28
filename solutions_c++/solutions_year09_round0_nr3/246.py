#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <math.h>
#define infile "a3.in"
#define outfile "a3.out"

const char yao[100]="welcome to code jam";

char s[1000];
long f[19],sum[19];

FILE *fin=fopen(infile,"r"),
	*fout=fopen(outfile,"w");

void init()
{	
}

void work()
{
	long w,i,j,k,testnum,len;
	fscanf(fin,"%ld", &testnum);
	fgets(s,1000,fin);
	for (w=1; w<=testnum; ++w)
	{
		fgets(s,1000,fin);
		for (i=0; i<19; ++i)
			sum[i]=0;
		len=strlen(s);
		for (i=0; i<len; ++i)
			if (((s[i]>='a')&&(s[i]<='z'))||(s[i]==' '))
			{
				for (j=0; j<19; ++j)
				{
					f[j]=0;
					if (yao[j]==s[i])
					{
						if (j==0)
							f[j]=1;
						else f[j]=sum[j-1];
					}
				}
				for (j=0; j<19; ++j)
					sum[j]=(sum[j]+f[j])%10000;
			}
			else break;
		fprintf(fout,"Case #%ld: ",w);
		if (sum[18]<10)
			fprintf(fout,"000");
		else if (sum[18]<100)
			fprintf(fout,"00");
		else if (sum[18]<1000)
			fprintf(fout,"0");
		fprintf(fout,"%ld\n",sum[18]);
	}
	fclose(fin);
	fclose(fout);
}

void output()
{

}

int main()
{
	init();
	work();
	output();	
	return 0;
}