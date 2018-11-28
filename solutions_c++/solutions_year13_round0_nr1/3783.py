#include <stdio.h>
#include <math.h>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <string.h>

using namespace std;

char grid[5][5];
FILE *in,*out;

void checkgame(int n)
{
	int i,j;
	int cntX,cntT,cntO,is_draw;

	fprintf(out,"Case #%d: ",n);

	is_draw=1;
	for(i=0;i<4;i++)
	{
		cntX=0;
		cntO=0;
		cntT=0;
		for(j=0;j<4;j++)
		{
			if(grid[i][j]=='X')
				cntX++;
			if(grid[i][j]=='O')
				cntO++;
			if(grid[i][j]=='T')
				cntT++;
			if(grid[i][j]=='.')
				is_draw=0;
		}
		if(cntX==4 || (cntX==3 && cntT==1))
		{
			fprintf(out,"X won\n");
			return;
		}
		if(cntO==4 || (cntO==3 && cntT==1))
		{
			fprintf(out,"O won\n");
			return;
		}
	}

	for(j=0;j<4;j++)
	{
		cntX=0;
		cntO=0;
		cntT=0;
		for(i=0;i<4;i++)
		{
			if(grid[i][j]=='X')
				cntX++;
			if(grid[i][j]=='O')
				cntO++;
			if(grid[i][j]=='T')
				cntT++;
		}
		if(cntX==4 || (cntX==3 && cntT==1))
		{
			fprintf(out,"X won\n");
			return;
		}
		if(cntO==4 || (cntO==3 && cntT==1))
		{
			fprintf(out,"O won\n");
			return;
		}
	}
	cntX=0;
	cntO=0;
	cntT=0;
	for(i=0;i<4;i++)
	{
		if(grid[i][i]=='X')
			cntX++;
		if(grid[i][i]=='O')
			cntO++;
		if(grid[i][i]=='T')
			cntT++;
	}
	if(cntX==4 || (cntX==3 && cntT==1))
	{
		fprintf(out,"X won\n");
		return;
	}
	if(cntO==4 || (cntO==3 && cntT==1))
	{
		fprintf(out,"O won\n");
		return;
	}

	cntX=0;
	cntO=0;
	cntT=0;
	for(i=0;i<4;i++)
	{
		if(grid[i][3-i]=='X')
			cntX++;
		if(grid[i][3-i]=='O')
			cntO++;
		if(grid[i][3-i]=='T')
			cntT++;
	}
	if(cntX==4 || (cntX==3 && cntT==1))
	{
		fprintf(out,"X won\n");
		return;
	}
	if(cntO==4 || (cntO==3 && cntT==1))
	{
		fprintf(out,"O won\n");
		return;
	}

	if(is_draw)
		fprintf(out,"Draw\n");
	else
		fprintf(out,"Game has not completed\n");
}

int main()
{
	int i;
	int t,tcase;

	in=fopen("A-large.in","r");
	out=fopen("output.out","w");

	fscanf(in,"%d",&tcase);

	for(t=0;t<tcase;t++)
	{
		for(i=0;i<4;i++)
			fscanf(in,"%s",grid[i]);
		checkgame(t+1);
	}
	return 0;
}