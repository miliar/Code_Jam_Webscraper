#include <iostream>
#include <math.h>
#include <stdio.h>
#include <vector>
using namespace std;
int i;
int amount(int queue[], int n)
{
	int res=0;
	for (int jj=0;jj<n;jj++)
		res+=queue[jj];
	return res;
}
void main()
{
	int earning,tc,r,k,n,count;
	int queue[10];
	int pointer;
	FILE *fp;
	if ((fp=fopen("C-small-attempt0.in", "r+"))==NULL)
	{
		printf("cannot open this file\n");
		exit(0);
	}
	FILE *fp2;
	if ((fp2=fopen("C-small.txt", "w+"))==NULL)
	{
		printf("cannot new this file\n");
		exit(0);
	}
	fscanf(fp,"%d\n",&tc);
	for (i=0;i<tc;i++)
	{
		earning=0;
		pointer=0;
		fscanf(fp,"%d %d %d\n",&r,&k,&n);
		for (int j=0;j<n;j++)
			fscanf(fp,"%d",&queue[j]);
		if (amount(queue,n)<=k)
			earning=r*amount(queue,n);
		else
		{
			for (int a=0;a<r;a++)//Íær´Î
			{
				count=0;
				while (k-count>=queue[pointer])//ÈÔÓÐ¿Õ×ù
				{
					count+=queue[pointer];
					pointer=(pointer+1)%n;
				}
				earning+=count;
			}
		}
		fprintf(fp2,"Case #%d: %d\n",i+1,earning);
	}
}
