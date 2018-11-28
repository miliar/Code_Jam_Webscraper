#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <math.h>
#define infile "b.in"

FILE *fin=fopen(infile,"r"),
	*fout=fopen("b.out","w");

int money[2100];
int f[2100][12], p,n, result;

void dp()
{
	int i,j,k,t;
	for (i=(1<<p)-1; i>=1; --i)
	{
		for (j=0; j<=p; ++j)
		{
			f[i][j]=-1;
			if (i>=(1<<(p-1))) //father of leaves
			{
				if ((p-money[i*2]<=j)&&(p-money[i*2+1]<=j))
					f[i][j]=0;
				else if ((p-money[i*2]<=j+1)&&(p-money[i*2+1]<=j+1))
					f[i][j]=money[i];
			}
			else {
				if ((f[i*2][j]!=-1)&&(f[i*2+1][j]!=-1))
					f[i][j]=f[i*2][j]+f[i*2+1][j];
				if ((f[i*2][j+1]!=-1)&&(f[i*2+1][j+1]!=-1))
				{
					t=f[i*2][j+1]+f[i*2+1][j+1]+money[i];
					if ((f[i][j]==-1)||(t<f[i][j]))
						f[i][j]=t;
				}
			}
		}
	}
	result=f[1][0];
}


int main()
{
	int i,j,w,t,k;
	fscanf(fin,"%d",&t);
	for (w=1; w<=t; ++w)
	{
		fscanf(fin,"%d",&p);
		for (i=p; i>=0; --i)
		{
			k=(1<<i);
			for (j=1; j<=(1<<i); ++j)
			{	
				fscanf(fin,"%d",&money[k]);
				++k;
			}
		}
		dp();
		fprintf(fout,"Case #%d: %d\n",w,result);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}