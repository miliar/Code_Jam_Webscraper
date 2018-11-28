#include <iostream>
#include <math.h>
#include <stdio.h>
#include <vector>
using namespace std;
int i;
bool snap[101][10];
void main()
{
//	int n,k,t,line;
	int line;
	unsigned long n,k,t;
	FILE *fp;
	if ((fp=fopen("A-large.in", "r+"))==NULL)
	{
		printf("cannot open this file\n");
		exit(0);
	}
	FILE *fp2;
	if ((fp2=fopen("A-large.txt", "w+"))==NULL)
	{
		printf("cannot new this file\n");
		exit(0);
	}
	fscanf(fp,"%d\n",&line);
	for (i=0;i<line;i++)
	{
		fscanf(fp,"%lu %lu\n", &n, &k);
		t=pow(2.0,n);
		if ((k+1)%t!=0)
			fprintf(fp2,"Case #%d: OFF\n", i+1);
		else
			fprintf(fp2,"Case #%d: ON\n", i+1);
	}
}
