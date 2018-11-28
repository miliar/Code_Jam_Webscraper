#include <stdio.h>
#include <stdlib.h>
#include <list>
#include <string>
#include <vector>


using namespace std;

int T,H,W;
char startChar;
unsigned int elevationMap[102][102];
char resultMap[102][102];

bool findMix(int& x,int& y)
{
	int tmpX=x,tmpY=y;
	if((tmpY-1) > 0 && elevationMap[y][x] > elevationMap[tmpY-1][tmpX])
		y=tmpY-1,x=tmpX;
	if((tmpX-1) > 0 && elevationMap[y][x] > elevationMap[tmpY][tmpX-1])
		y=tmpY,x=tmpX-1;
	if((tmpX+1) <= W && elevationMap[y][x] > elevationMap[tmpY][tmpX+1])
		y=tmpY,x=tmpX+1;
	if((tmpY+1) <= H && elevationMap[y][x] > elevationMap[tmpY+1][tmpX])
		y=tmpY+1,x=tmpX;

	if(tmpX==x && tmpY==y)
		return false;

	return true;
}


void fillSinkWith(int x,int y,char c)
{
	if(findMix(x,y))
	{
		if(resultMap[y][x] > 0)
			return;

		resultMap[y][x] = c;
		fillSinkWith(x,y,c);
	}
}

void fillSink(int x,int y)
{
	int tmpX=x,tmpY=y;
	if(findMix(x,y))
	{
		if(resultMap[y][x] == 0)
			fillSink(x,y);
		resultMap[tmpY][tmpX] = resultMap[y][x];
	}else
	{
		startChar = startChar + 1;
		resultMap[y][x] = startChar;
	}
}

int main()
{
	freopen("..\\B-large.in","r",stdin);
	freopen("..\\B-large.out","w",stdout);

	scanf("%d",&T);

	for(int caseNum=0;caseNum<T;caseNum++)
	{
		startChar = 'a';

		scanf("%d %d",&H,&W);

		for(int hIdx=1;hIdx<=H;hIdx++)
		{
			for(int wIdx=1;wIdx<=W;wIdx++)
			{
				scanf("%d",&elevationMap[hIdx][wIdx]);
			}
		}

		for(int wIdx=1;wIdx<=W;wIdx++)
		{
			elevationMap[0][wIdx] = elevationMap[1][wIdx];
			elevationMap[H+1][wIdx] = elevationMap[H][wIdx];
		}
		for(int hIdx=0;hIdx<=H+1;hIdx++)
		{
			elevationMap[hIdx][0] = elevationMap[hIdx][1];
			elevationMap[hIdx][W+1] = elevationMap[hIdx][W];
		}

		for(int hIdx=1;hIdx<=H;hIdx++)
		{
			for(int wIdx=1;wIdx<=W;wIdx++)
				resultMap[hIdx][wIdx] = 0;
		}

		resultMap[1][1] = startChar;

		fillSinkWith(1,1,'a');

		for(int hIdx=1;hIdx<=H;hIdx++)
		{
			for(int wIdx=1;wIdx<=W;wIdx++)
			{
				if(resultMap[hIdx][wIdx] == 0)
					fillSink(wIdx,hIdx);
			}
		}

		printf("Case #%d:\n",caseNum+1);
		for(int hIdx=1;hIdx<=H;hIdx++)
		{
			for(int wIdx=1;wIdx<=W;wIdx++)
				printf("%c ",resultMap[hIdx][wIdx]);
			printf("\n");
		}
	}

	fflush(stdout);

	return 0;
}
