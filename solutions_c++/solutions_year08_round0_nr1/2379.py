#include "stdio.h"
#include "string.h"
#define N 102
#define M 1002

int main()
{
	FILE * fr,* fw;
	char engine[N][N],sear[M][N];
	int in_engine[N],sum,num,task,temp_num,need;
	int i,j,k,l;

	if((fr=fopen("file.in","r"))==NULL)
	{
		printf("Can't open the file.in\n");
	}
	if((fw=fopen("file.txt","w+"))==NULL)
	{
		printf("Can't open the file.txt\n");
	}
	for(i=0;i<=N-1;i++)
	{
		for(j=0;j<=N-1;j++)
		{
			engine[i][j]='\0';
		}
	}
	for(i=0;i<=M-1;i++)
	{
		for(j=0;j<=N-1;j++)
		{
			sear[i][j]='\0';
		}
	}

	fscanf(fr,"%d",&sum);
	for(i=0;i<=sum-1;i++)
	{
		for(j=0;j<=N-1;j++)
		{
			in_engine[j]=0;
		}
		need=0;
		fscanf(fr,"%d",&num);
		
		for(j=0;j<=num;j++)
		{
			fgets(engine[j],N,fr);        //从1开始有效
		}
		fscanf(fr,"%d",&task);

		for(j=0;j<=task;j++)
		{
			fgets(sear[j],N,fr);         //从1开始有效
		}
		temp_num=num;
		for(j=1;j<=task;j++)
		{
			for(k=1;k<=num;k++)
			{
				if(strcmp(sear[j],engine[k])==0)
				{
					if(in_engine[k]==0)
					{
						in_engine[k]=1;
					    temp_num--;
					}
					break;
				}
			}
			if(temp_num==0)
			{
				need++;
				for(l=0;l<=N-1;l++)
				{
					in_engine[l]=0;
				}
				in_engine[k]=1;
				temp_num=num-1;
			}
		}
		if(i<sum-1)
		{
			fprintf(fw,"Case #%d: %d\n",i+1,need);
		}
		else if(i==sum-1)
		{
			fprintf(fw,"Case #%d: %d",i+1,need);
		}

	}
	fclose(fr);
	fclose(fw);
	return 0;
}
