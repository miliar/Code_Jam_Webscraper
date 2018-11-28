#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<math.h>

#define MAXN 10
#define MAXQ 100

int flag[MAXN],noseen,noquer;

void main()
{
	FILE *fp,*fp2;
	void find_min_max(int,int *,int *);

	int n=0,d,i=0,j,k,m,switches=0,occurence=0,max=0,min=9999,minse,maxse,flags[MAXN];
	char senames[MAXN][100],queries[MAXQ+1][100],currentse[100],str[100];

	fp=fopen("E:\\Amol\\CodeJam\\Universe\\A-small.txt","r");
	fscanf(fp,"%d",&n);
	fp2=fopen("E:\\Amol\\CodeJam\\Universe\\A-small-out.txt","w");

	for(i=0;i<n;i++)
	{
		switches=0;
		occurence=0;
		max=0;
		maxse=0;
		min=9999;
		minse=9999;

		fscanf(fp,"%d",&noseen);
		fgetc(fp);
		for(j=0;j<noseen;j++)
		{
			fgets(str,100,fp);
			strcpy(senames[j],str);
		}

		fscanf(fp,"%d",&noquer);
		fgetc(fp);
		for(j=0;j<noquer;j++)
		{
			fgets(str,100,fp);
			strcpy(queries[j],str);
		}

		for(j=0;j<noquer;j++)
		{
			for(k=0;k<noseen;k++)
			{
				if(strcmp(senames[k],queries[j])==0)
					flag[k]=flag[k]+1;
			}
		}

		for(j=0;j<noseen;j++)
		{
			if(flag[j]!=0)
				occurence++;
		}

		if(occurence==0)
			switches=0;
		else
		{
			switches=0;
			strcpy(currentse,queries[0]);

			for(j=0;j<noquer;j++)
			{
				if(strcmp(queries[j],currentse)==0)
				{
					for(k=0;k<noseen;k++)
					{
						flags[k]=9999;
						for(m=j;m<noquer;m++)
						{
							if(strcmp(senames[k],queries[m])==0)
							{
								flags[k]=flags[k]-9999;
								break;
							}
							else
							{
								flags[k]++;
							}
						}
					}

					maxse=0;
					max=0;

					for(k=0;k<noseen;k++)
					{
						if(flags[k]>max)
						{
							max=flags[k];
							maxse=k;
						}
					}

					strcpy(currentse,senames[maxse]);
					if(j!=0)
						switches++;
				}
			}
		}
		fprintf(fp2,"Case #%d: %d\n",i+1,switches);
	}

}
