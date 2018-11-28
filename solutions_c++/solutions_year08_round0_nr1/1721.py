#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void main ()
{
	FILE *fp,*fp0;
	char casenumc[100];
	int casenum;
	char searchnumc[100];
	int searchnum;
	//int i;
	char searchen[100][101];
	char incomqnumc[100];
	int incomqnum;
	char incomq[101];
	char fincomq[101]="\n";

	int enflag[100];
	int flag;

	if((fp=fopen("A-large.in","r"))==NULL)
	{
		if((fp=fopen("A-large.in","r"))==NULL)
		{
			printf("file open error!!\n");
			exit(EXIT_FAILURE);

		}
	}
	if((fp0=fopen("A-large.out","w"))==NULL)
	{
		printf("file open error!!\n");
		exit(EXIT_FAILURE);

	}
	fgets(casenumc,99,fp);
	casenum = atoi(casenumc);
	for (int i=0;i<casenum;i)
	{
		flag=0;
		fgets(searchnumc,99,fp);
		searchnum = atoi(searchnumc);

		for(int a=0;a<searchnum;a++)
		{
			fgets(searchen[a],101,fp);
			enflag[a]=0;
		}

		fgets(incomqnumc,99,fp);
		incomqnum = atoi(incomqnumc);
		int zoro=0;
		for (int a=0;a<incomqnum;a++)
		{
			fgets(incomq,101,fp);

			for(int n=0;n<searchnum;n++)
			{
				if(strcmp(incomq,searchen[n])==0)
				{
					enflag[n]++;
					for(int m=0;m<searchnum;m++)
					{
						if(enflag[m]>=1)zoro++;
					}
					if(zoro==searchnum)
					{
						flag++;
						for(int l=0;l<searchnum;l++)
						{
							enflag[l]=0;
						}
					}
					zoro=0;
					enflag[n]++;
					break;
				}
			}

		}
		i++;
		fprintf(fp0,"Case #%d: %d\n",i,flag);

	}

	fclose(fp);
	fclose(fp0);

}
