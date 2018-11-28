#include <iostream>
#include <math.h>
#include <stdio.h>
int i,j;
void mysort(long t[],int n)
{
	for (int ii=0;ii<n;ii++)
		for (int jj=0;jj<n-ii-1;jj++)
		{
			long a=t[jj];
			long b=t[jj+1];
			if (a<b)
			{
				t[jj]=b;
				t[jj+1]=a;
			}
		}
}
long gcm(long a, long b)
{
	long aa=a;
	long bb=b;
	while (aa!=bb)
	{
		if (aa>bb)
			aa=aa-bb;
		else
			bb=bb-aa;
	}
	return aa;
}
void main()
{
	int line,n;
	long t[3],base,last;
	FILE *fp;
	if ((fp=fopen("B-small-attempt1.in", "r+"))==NULL)
	{
		printf("cannot open this file\n");
		exit(0);
	}
	FILE *fp2;
	if ((fp2=fopen("B-small.txt", "w+"))==NULL)
	{
		printf("cannot new this file\n");
		exit(0);
	}
	fscanf(fp,"%d\n",&line);
	for (i=0;i<line;i++)
	{
		fscanf(fp,"%d ",&n);
		for (j=0;j<n;j++)
			fscanf(fp,"%d ",&t[j]);
		mysort(t,n);
		if (n==3 && (t[0]==t[1] || t[1]==t[2]) )
		{
			if (t[0]==t[1])
				t[1]=t[2];
			n=2;
		}
		if (n==2)
		{
			base=t[0]-t[1];
			last=t[1];
		}
		else if (n==3)
		{
			base=gcm(t[0]-t[1],t[1]-t[2]);
			last=t[2];
		}
		while (last>0)
		{
			last=last-base;
		}
		last=-last;
		fprintf(fp2,"Case #%d: %d\n", i+1, last);
	}
}
