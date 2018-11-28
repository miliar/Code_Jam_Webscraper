#include "stdio.h"
#include "string.h"
#define T 1000
#define N 10

int main()
{
	FILE * fr,* fw;
	int v1[N],v2[N],temp,sum;
	int t,n;
	int i,j,k,l;

	if((fr=fopen("file.in","r"))==NULL)
	{
		printf("Can't open the file.in\n");
	}
	if((fw=fopen("file.txt","w+"))==NULL)
	{
		printf("Can't open the file.txt\n");
	}
	fscanf(fr,"%d",&t);
	for(i=0;i<=t-1;i++)
	{
		fscanf(fr,"%d",&n);
		for(j=0;j<=n-1;j++)
		{
			fscanf(fr,"%d",&v1[j]);
		}
		for(j=0;j<=n-1;j++)
		{
			fscanf(fr,"%d",&v2[j]);
		}
		for(j=0;j<n-1;j++)
		{
			k=j;
			for(l=j+1;l<n;l++)
			{
				if(v1[k]>v1[l])
				{
					k=l;
				}
			}
			if(k!=j)
			{
				temp=v1[k];
				v1[k]=v1[j];
				v1[j]=temp;
			}
		}
		for(j=0;j<n-1;j++)
		{
			k=j;
			for(l=j+1;l<n;l++)
			{
				if(v2[k]<v2[l])
				{
					k=l;
				}
			}
			if(k!=j)
			{
				temp=v2[k];
				v2[k]=v2[j];
				v2[j]=temp;
			}
		}
		sum=0;
		for(j=0;j<=n-1;j++)
		{
			sum=sum+v1[j]*v2[j];
		}
		if(i<t-1)
		{
			fprintf(fw,"Case #%d: %d\n",i+1,sum);
		}
		else if(i==t-1)
		{
			fprintf(fw,"Case #%d: %d",i+1,sum);
		}
	}
	fclose(fr);
	fclose(fw);
	return 0;
}
