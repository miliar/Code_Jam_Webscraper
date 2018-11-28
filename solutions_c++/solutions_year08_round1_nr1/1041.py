#include <stdio.h>
#include <string.h>

int x[8],y[8],z[8];

int work(int n)
{
	int i,sum=0;
	for (i=0;i<n;i++) sum+=x[i]*y[i];
	return sum;
}

void sort(int s,int n)
{
	int i,j,temp;
	for (i=s;i<n-1;i++)
		for (j=i+1;j<n;j++)
			if (z[i]>z[j])
			{
				temp=y[i];y[i]=y[j];y[j]=temp;
				temp=z[i];z[i]=z[j];z[j]=temp;
			}
}

void swap(int n)
{
	int i,j,min=10000,p,temp;
	i=n-1;
	while ((i>0)&&(z[i]<z[i-1])) i--;
	for (j=i;j<n;j++) if ((z[j]<min) && (z[j]>z[i-1]))
	{
		min=z[j];
		p=j;
	}
	temp=z[i-1];z[i-1]=z[p];z[p]=temp;
	temp=y[i-1];y[i-1]=y[p];y[p]=temp;
	sort(i,n);
}

void main()
{
	int t,min,i,j,n,nn;
	FILE *fin,*fout;
	fin=fopen("A-small-attempt1.in","r");
	fscanf(fin,"%d\n",&t);
	fout=fopen("A-small.out","w");
	for (i=0;i<t;i++)
	{
		fscanf(fin,"%d\n",&n);
		nn=1;
		for (j=n;j>1;j--) nn*=j;
		for (j=0;j<n;j++) fscanf(fin,"%d",&x[j]);
		for (j=0;j<n;j++) fscanf(fin,"%d",&y[j]);
		for (j=0;j<n;j++) z[j]=j;
		min=work(n);
		for (j=1;j<nn;j++)
		{
			swap(n);
			if (min>work(n)) min=work(n);
		}
		fprintf(fout,"Case #%d: %d\n",i+1,min);
	}
}