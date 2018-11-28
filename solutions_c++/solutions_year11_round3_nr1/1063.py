#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void transform(char a[50][50],int r,int c)
{
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
		{			
			if(a[i][j]=='#' && i!=r-1 && j!=c-1)
			{
				if(a[i][j+1]=='#' && a[i+1][j] == '#' && a[i+1][j+1] == '#')
				{
					a[i][j]='/';
					a[i][j+1]='\\';
					a[i+1][j]='\\';
					a[i+1][j+1]='/';
				}
			}
		}
	}
}
int main()
{
	FILE *fin,*fout;
	fin=fopen("input.txt","r");
	fout=fopen("output.txt","w");
	int t;
	fscanf(fin,"%d",&t);
	char a[50][50];
	int r,c;
	for(int i=0;i<t;i++)
	{
		fprintf(fout,"Case #%d:\n",i+1);
		fscanf(fin,"%d %d",&r,&c);
		fgetc(fin);
		for(int j=0;j<r;j++)
		{
			for(int k=0;k<c;k++)
			{
				a[j][k]=fgetc(fin);
			}
			fgetc(fin);
		}
		transform(a,r,c);
		int f=0;
		for(int j=0;j<r;j++)
		{
			for(int k=0;k<c;k++)
			{
				if(a[j][k]=='#')
				{
					f=1;
					break;
				}
			}
		}
		if(f)
			fprintf(fout,"Impossible");
		else
		{
			for(int j=0;j<r;j++)
			{
				for(int k=0;k<c;k++)
				{
					fprintf(fout,"%c",a[j][k]);
				}
				if(j!=r-1)
					fprintf(fout,"\n");
			}
		}
		if(i!=t-1)
			fprintf(fout,"\n");
	}
	return 0;
}