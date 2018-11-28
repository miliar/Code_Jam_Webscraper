#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int i,j;
void main()
{
	FILE *fp;
	if ((fp=fopen("B-large.in", "r+"))==NULL)
	{
		printf("cannot open this file\n");
		exit(0);
	}
	FILE *fp2;
	if ((fp2=fopen("out1.txt", "w+"))==NULL)
	{
		printf("cannot new this file\n");
		exit(0);
	}
	int t,c,x,y;
	unsigned long l,p;
	fscanf(fp,"%d",&t);
	for (i=0;i<t;i++)
	{
		fscanf(fp,"%d %d %d",&l,&p,&c);
		x=ceil(log((double)p/(double)l)/log((double)c))-1;
		if (x==0)
			y=0;
		else
			y=floor(log((double)x)/log(2.0))+1;
		fprintf(fp2,"Case #%d: %d\n",i+1,y);
	}
}
