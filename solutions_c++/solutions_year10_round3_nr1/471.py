#include <stdio.h>
#include <stdlib.h>
int i,j,p,q;
void main()
{
	FILE *fp;
	if ((fp=fopen("A-large.in", "r+"))==NULL)
	{
		printf("cannot open this file\n");
		exit(0);
	}
	FILE *fp2;
	if ((fp2=fopen("out.txt", "w+"))==NULL)
	{
		printf("cannot new this file\n");
		exit(0);
	}
	int t,n,temp1,temp2;
	int a[1000],b[1000];
	int sum=0;
	fscanf(fp,"%d",&t);
	for (i=0;i<t;i++)
	{
		sum=0;
		fscanf(fp,"%d",&n);
		if (n==1)
		{
			sum=0;
			fscanf(fp,"%d %d",&temp1,&temp2);
		}
		else
		{
			for (j=0;j<n;j++)
				fscanf(fp,"%d %d",&a[j],&b[j]);
			for (p=0;p<n;p++)
				for (q=p+1;q<n;q++)
				{
					if (a[p]-a[q]>0 && b[p]-b[q]<0 || a[p]-a[q]<0 && b[p]-b[q]>0)
						sum++;
				}
		}
		fprintf(fp2,"Case #%d: %d\n",i+1,sum);
	}
}
