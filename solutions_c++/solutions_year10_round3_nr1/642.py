// cjr3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{
	int total,n;
	int a[1000];int b[1000];
	FILE *fp=fopen("large","r");
	FILE *fout=fopen("out","w");
	fscanf(fp,"%d",&total);
	for(int i=0;i<total;i++)
	{
		fscanf(fp,"%d",&n);
		for(int j=0;j<n;j++)
			fscanf(fp,"%d %d",&a[j],&b[j]);
		for(int j=0;j<n-1;j++)
		{
			for(int k=0;k<n-j-1;k++)
			{
				if(a[k+1]<a[k])
				{
					int temp=a[k+1];
					a[k+1]=a[k];
					a[k]=temp;
					temp=b[k+1];
					b[k+1]=b[k];
					b[k]=temp;
				}
			}
		}
		for(int j=0;j<n;j++)
		{
//			printf("%d ",a[j]);
		}
//		printf("\n");
		int inter=0;
		for(int j=0;j<n;j++)
		{
			for(int k=j;k<n;k++)
			{
				if(b[k]<b[j])
					inter++;
			}
		}
		printf("Case #%d: %d\n",i+1,inter);
		fprintf(fout,"Case #%d: %d\n",i+1,inter);
	}
	return 0;
}

