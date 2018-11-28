// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
int a[100][100],b[100][100];
int H,W;
char dir(int x,int y)
{
	int min=a[x][y];
	if (x>0)
		if (a[x-1][y]<min) min=a[x-1][y];
	if (y>0)
		if (a[x][y-1]<min) min=a[x][y-1];
	if (y<W-1)
		if (a[x][y+1]<min) min=a[x][y+1];
	if (x<H-1)
		if (a[x+1][y]<min) min=a[x+1][y];
	if (a[x][y]==min) return 'X';
	if (x>0)
		if (a[x-1][y]==min) return 'N';
	if (y>0)
		if (a[x][y-1]==min) return 'W';
	if (y<W-1)
		if (a[x][y+1]==min) return 'E';
	if (x<H-1)
		if (a[x+1][y]==min) return 'S';	
	return 'X';
}
void paint(int x,int y, int color)
{
	b[x][y]=color;
	int min=a[x][y];
	if (x>0)
		if (a[x-1][y]<min) min=a[x-1][y];
	if (y>0)
		if (a[x][y-1]<min) min=a[x][y-1];
	if (y<W-1)
		if (a[x][y+1]<min) min=a[x][y+1];
	if (x<H-1)
		if (a[x+1][y]<min) min=a[x+1][y];
	if (a[x][y]==min) min--;
	if (x>0)
		if (a[x-1][y]==min) 
		{
			if (b[x-1][y]==-1) paint(x-1,y,color);
			min--;
		}
	if (y>0)
		if (a[x][y-1]==min) 
		{
			if (b[x][y-1]==-1) paint(x,y-1,color);
			min--;
		}
	if (y<W-1)
		if (a[x][y+1]==min) 
		{
			if (b[x][y+1]==-1) paint(x,y+1,color);
			min--;
		}
	if (x<H-1)
		if (a[x+1][y]==min) 
		{
			if (b[x+1][y]==-1) paint(x+1,y,color);
			min--;
		}

	if (x>0)
		if (b[x-1][y]==-1&& dir(x-1,y)=='S') paint(x-1,y,color);
	if (y>0)
		if (b[x][y-1]==-1&& dir(x,y-1)=='E') paint(x,y-1,color);
	if (y<W-1)
		if (b[x][y+1]==-1&& dir(x,y+1)=='W') paint(x,y+1,color);
	if (x<H-1)
		if (b[x+1][y]==-1&& dir(x+1,y)=='N') paint (x+1,y,color);
}

int _tmain(int argc, _TCHAR* argv[])
{
	int T,i,j,k,l,m,n,o;
	char s[27]="abcdefghijklmnopqrstuvwxyz";
	FILE* f=fopen("..\\input.txt","r");
	FILE* fo=fopen("output.txt","w");
	fscanf(f,"%d",&T);
	for (i=0;i<T;i++)
	{
		fscanf(f,"%d %d",&H,&W);
		for (j=0;j<H;j++)
			for (k=0;k<W;k++)
			{
				fscanf(f,"%d",&a[j][k]);
				b[j][k]=-1;
			}
		l=1;
		m=0;
		while (l)
		{
			l=0;
			j=0;
			k=0;
			while (b[j][k]!=-1&&j<H&&k<W)
			{
				k++;
				if (k==W) 
				{
					k=0;
					j++;
				}
			}
			if (b[j][k]==-1)
			{
				l=1;
				paint(j,k,m);
				m++;
			}
		}
		fprintf(fo,"Case #%d:\n",i+1);
		for (j=0;j<H;j++)
		{
			for (k=0;k<W;k++)
				fprintf(fo,"%c ",s[b[j][k]]);
			fprintf(fo,"\n");
		}
	}
	fclose(f);
	fclose(fo);
	return 0;
}

