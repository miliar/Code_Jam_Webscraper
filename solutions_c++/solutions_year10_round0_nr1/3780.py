#include "stdio.h"
#include "math.h"

int PowerOfTwo(int n)
{
	int i,tot=1;
	for(i=0;i<n;i++)
	{
		tot = tot*2;
	}
	return tot;
}

int main()
{
	int TestCase;
	FILE *fp2;
	FILE *fp1;
	fp2 = fopen("c:/codejaminput1.in","r");
	fp1 = fopen("c:/gocodejam1","w");
	fscanf(fp2,"%d",&TestCase);
	int i,K;
	int N;
	for( i = 1; i <= TestCase ; i++ )
	{
		fscanf(fp2,"%d %d",&N,&K);
		if(((K + 1)%(PowerOfTwo(N))) == 0 )
		{
			fprintf(fp1,"Case #%d: ON\n",i);
		}
		else
		{
			fprintf(fp1,"Case #%d: OFF\n",i);
		}
	}
	fclose(fp1);
	fclose(fp2);
	scanf("%d",&i);
}

