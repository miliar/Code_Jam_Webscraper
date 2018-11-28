#include <stdio.h>
#include <stdlib.h>
#include <string.h>




void main()
{
	FILE * fileIn = NULL,* fileOut = NULL;
	if (NULL == (fileIn = fopen("d:\\small.in","r")))
	{
		return;
	}
	if (NULL == (fileOut = fopen("d:\\small.out","w")))
	{
		return;
	}

	int nCase = 0;	
	char line[10000];

	int P = 0,K = 0,L = 0;
	double aL[1200];
	
	fgets(line,200,fileIn);
	sscanf(line,"%d",&nCase);
	for (int i = 0;i<nCase;i++)
	{	
		fgets(line,10000,fileIn);
		sscanf(line,"%d %d %d",&P,&K,&L);
		fgets(line,10000,fileIn);
		char * pLine = line;
		char num[20];
		int j = 0,k = 0;
		for ( j = 0;j<L;j++)
		{
			sscanf(pLine,"%s",num);
			pLine += strlen(num)+1;
			aL[j] = atoi(num);			
		}
		bool bchange = false;

		for (j = 0;j<L-1;j++)
		{
			for(k = j+1;k<L;k++)
			{
				double temp = 0;
				if(aL[j] < aL[k])
				{
					bchange = true;
					temp = aL[k];
					aL[k]  = aL[j];
					aL[j] = temp;
				}
			}
		}
		if(false == bchange)
		{
			printf("\nCase #%d: Impossible\n",i+1);
			fprintf(fileOut,"Case #%d: Impossible\n",i+1);
			continue;
		}

		int n = 0;
		double sum = 0;
		for (j = 0;j<P;j++)
		{
			for (k = 0;k<K;k++)
			{
				sum += aL[n]*(j+1);
				n++;
				if (n>=L)
				{
					j = P;
					break;
				}
			}

		}

			
		printf("\nCase #%d: %.0f\n",i+1,sum);
		fprintf(fileOut,"Case #%d: %.0f\n",i+1,sum);
	}

	fclose(fileIn);
	fclose(fileOut);

}