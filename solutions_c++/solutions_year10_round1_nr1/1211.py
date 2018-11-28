#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <math.h>
#define infile "a.in"

FILE *fin=fopen(infile,"r"),
	*fout=fopen("a.out","w");

int n,ge;
char yuan[100][100],a[100][100];

bool yes(int x, int y,char c)
{
	if ((x>=1)&&(x<=n)&&(y>=1)&&(y<=n))
		return (a[x][y]==c);
	else return false;
}

bool ky(int x,int y, int dx,int dy, char c)
{
	int i;
	for (i=0; i<ge; ++i)
		if (!yes(x+dx*i,y+dy*i,c))
			return false;
	return true;
}

int main()
{
	int t,w,i,j, p;
	char s[100];
	fscanf(fin,"%d",&t);
	for (w=1; w<=t; ++w)
	{
		fscanf(fin,"%d%d",&n,&ge);
		for (i=1; i<=n; ++i)
		{
			fscanf(fin,"%s",s);
			for (j=1; j<=n; ++j)
			{
				yuan[i][j]=s[j-1];
				a[i][j]=' ';
			}
		}
		for (i=1; i<=n; ++i)
		{
			j=n;
			for (p=n; p>=1; --p)
				if (yuan[n-i+1][p]=='.')
				{}
				else {
					a[j--][i]=yuan[n-i+1][p];
				}
		}

		bool b=false,r=false;

		for (i=1; i<=n; ++i)
			for (j=1; j<=n; ++j)
				if (a[i][j]=='B')
				{
					if (ky(i,j,0,1,'B'))
						b=true;
					if (ky(i,j,1,0,'B'))
						b=true;
					if (ky(i,j,1,1,'B'))
						b=true;
					if (ky(i,j,-10,1,'B'))
						b=true;
				}
				else if (a[i][j]=='R')
				{
					if (ky(i,j,0,1,'R'))
						r=true;
					if (ky(i,j,1,0,'R'))
						r=true;
					if (ky(i,j,1,1,'R'))
						r=true;
					if (ky(i,j,-1,1,'R'))
						r=true;
					
				}

		fprintf(fout,"Case #%d: ", w);
		if ((!b)&&(!r))
			fprintf(fout,"Neither\n");
		if ((b)&&(!r))
			fprintf(fout,"Blue\n");
		if ((!b)&&(r))
			fprintf(fout,"Red\n");
		if ((b)&&(r))
			fprintf(fout,"Both\n");
	}
	fclose(fin);
	fclose(fout);
	return 0;
}