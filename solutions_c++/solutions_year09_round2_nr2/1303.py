#include <stdio.h>
#include <memory.h>
#include <string.h>
#include <malloc.h>


int main()
{
	FILE *fp=fopen("1.txt", "r");
	int nRound;
	int i, j, k;
	int pList[10];
	int pList1[10];

	fscanf(fp, "%d", &nRound);
	for(i=0; i<nRound; i++)
	{
		int nVal;
		fscanf(fp, "%d", &nVal);
		memset(pList, 0, 10*sizeof(int));
		j = nVal;
		while(j>0)
		{
			pList[j%10]++;
			j/=10;
		}
		
		for(j=nVal+1;;j++)
		{
			memset(pList1, 0, 10*sizeof(int));
			k = j;
			while(k>0)
			{
				pList1[k%10]++;
				k/=10;
			}
			for(k=1; k<10; k++)
			{
				
				{
					if(pList1[k]!=pList[k]) break;
				}
			}
			if(k==10) break;
		}

		printf("Case #%d: %d\n", i+1, j);
	}

	
	fclose(fp);
}
