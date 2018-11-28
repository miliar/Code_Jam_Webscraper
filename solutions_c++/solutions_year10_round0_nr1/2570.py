#include<vector>
#include<string>
#include<iostream>
#include <stdio.h>
#include <iostream.h>
using namespace std;
int calt(int n);
void main()
{
	FILE *fp = fopen("A-large.in.txt","r");
	FILE *fp2 = fopen("A-large.out.txt","w");
	if(!fp)
	{
		printf("cannot open file\n");
		exit(0);
	}
	int tt;
	fscanf(fp,"%d",&tt);
	for(int i=1;i<=tt;i++)
	{
		int n,k,t;
		fscanf(fp,"%d%d",&n,&k);
		t = calt(n);
		if( (k+1)%(t+1) == 0 )
			fprintf(fp2,"Case #%d: ON",i);
		else
			fprintf(fp2,"Case #%d: OFF",i);
		if(i!=tt)
			fprintf(fp2,"\n");

	}
	fclose(fp);
	fclose(fp2);
}
int calt(int n)
{
	int t;
	if(n == 1)
		return 1;
	else
		return 2*calt(n-1) +1;
}