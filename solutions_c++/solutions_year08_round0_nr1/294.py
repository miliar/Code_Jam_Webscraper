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
	int nQ = 0;
	int nS = 0;
	int s[100];
	char str[100][120];
	char line[200];
	int nSwitch = 0;
	int iChoice = -1;
	int iFar = -1;
	fgets(line,200,fileIn);
	sscanf(line,"%d",&nCase);
	for (int i = 0;i<nCase;i++)
	{		
		printf("-----Case %d: -----\n",i+1);
		nSwitch = 0;
		fgets(line,200,fileIn);
		sscanf(line,"%d",&nS);
		printf("Search : \n");
		for (int j = 0;j<nS;j++)
		{
			fgets(line,200,fileIn);
			strcpy(str[j],line);
			printf("\t%s",line);
		}
		printf("\n");
		fgets(line,200,fileIn);
		sscanf(line,"%d",&nQ);
		int sum = 0;
		iChoice = -1;
		memset(s,0,sizeof(int)*100);
		printf("Query : \n");
		for (j = 0;j<nQ;j++)
		{
			fgets(line,200,fileIn);
			

			for (int k = 0;k<nS;k++)
			{
				if (strcmp(str[k],line) == 0)
				{
					if (s[k] == 0)
					{
						s[k] = 1;
						sum ++;
						if (iChoice != k )
						{
							iFar = k;
						}						
					}
					break;
				}
			}
			printf("\t");
			if (sum >= nS)
			{
				sum = 1;
				memset(s,0,sizeof(int)*100);
				iChoice = iFar;
				s[iChoice] = 1;
				nSwitch++;
				printf("**switch**");
			}
			printf("%s",line);
		}		
		printf("\nCase #%d: %d\n",i+1,nSwitch);
		fprintf(fileOut,"Case #%d: %d\n",i+1,nSwitch);
	}
	
	




	fclose(fileIn);
	fclose(fileOut);

}