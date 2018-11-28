#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <functional>
#include <iostream>

const int cT=100;
const int cH=15;
const int cW=15;

int nH[cT], nW[cT];
int nWaterData[cH][cW];
int nCaseNumber;
char cWaterResult[cT][cH][cW];
char cLine, cString;
bool compare(int argv1, int argv2);
char checkLine(int i, int y, int x);
void fillLine(int i, int y, int x);

int main()
{
	using namespace std;
	vector <int> nPos;
	vector <int>::iterator nPosIter;
	FILE *fpopen, *fpout;

	int nT, nY, nX;
	int i, j, k;

	fpopen=fopen("B-small.in", "r");
	fpout=fopen("B-small.out", "w");

	fscanf(fpopen, "%d", &nT);
	for(i=0;i<nT;i++)
	{
		nPos.clear();
		cLine='a';

		for(j=0;j<cH;j++)
			for(k=0;k<cW;k++)
				cWaterResult[i][j][k]=0;

		cWaterResult[i][0][0]='a';

		fscanf(fpopen, "%d %d", &nH[i], &nW[i]);
		for(j=0;j<nH[i];j++)
			for(k=0;k<nW[i];k++)
			{
				fscanf(fpopen, "%d", &nWaterData[j][k]);
				nPos.push_back(j*nW[i]+k);
			}

		nCaseNumber=i;
		std::stable_sort(nPos.begin(), nPos.end(), compare);
		//std::stable_sort((void *)nPos, (size_t)nH[i]*nW[i], sizeof(int *), compare);

		cString='a';
		fillLine(i, 0, 0);

		for(nPosIter=nPos.begin();nPosIter!=nPos.end();nPosIter++)
		{
			nY=*nPosIter/nW[i];
			nX=*nPosIter%nW[i];

			// 체크 안된부분이면
			if(cWaterResult[i][nY][nX]==0)
			{
				cString=checkLine(i, nY, nX);
				if(cString==0)
				{
					cLine+=1;
					cString=cLine;
				}

				fillLine(i, nY, nX);
			}
		}
	}

	for(i=0;i<nT;i++)
	{
		fprintf(fpout, "Case #%d:\n", i+1);
		for(j=0;j<nH[i];j++)
		{
			for(k=0;k<nW[i];k++)
				fprintf(fpout, "%c ", cWaterResult[i][j][k]);
			fprintf(fpout, "\n");
		}
	}

	fclose(fpopen);
	fclose(fpout);
	return 0;
}

char checkLine(int i, int y, int x)
{
	int nDir=0;
	int nNum=10001;
	char cType;
	
	cType=cWaterResult[i][y][x];

	if(y-1>=0 && nWaterData[y-1][x]<nWaterData[y][x] && nWaterData[y-1][x]<nNum)
	{
		nNum=nWaterData[y-1][x];
		nDir=1;
	}
	if(x-1>=0 && nWaterData[y][x-1]<nWaterData[y][x] && nWaterData[y][x-1]<nNum)
	{
		nNum=nWaterData[y][x-1];
		nDir=2;
	}
	if(x+1<nW[i] && nWaterData[y][x+1]<nWaterData[y][x] && nWaterData[y][x+1]<nNum)
	{
		nNum=nWaterData[y][x+1];
		nDir=3;
	}
	if(y+1<nH[i] && nWaterData[y+1][x]<nWaterData[y][x] && nWaterData[y+1][x]<nNum)
	{
		nNum=nWaterData[y+1][x];
		nDir=4;
	}

	switch(nDir)
	{
	case 1:
		cType=checkLine(i, y-1, x);
		break;
	case 2:
		cType=checkLine(i, y, x-1);
		break;
	case 3:
		cType=checkLine(i, y, x+1);
		break;
	case 4:
		cType=checkLine(i, y+1, x);
		break;
	}

	return cType;
}

void fillLine(int i, int y, int x)
{
	int nDir=0;
	int nNum=10001;

	if(cWaterResult[i][y][x]<='z' && cWaterResult[i][y][x]>='a')
	{
		if(y!=0 || x!=0)
			return;
	}

	cWaterResult[i][y][x]=cString;

	if(y-1>=0 && nWaterData[y-1][x]<nWaterData[y][x] && nWaterData[y-1][x]<nNum)
	{
		nNum=nWaterData[y-1][x];
		nDir=1;
	}
	if(x-1>=0 && nWaterData[y][x-1]<nWaterData[y][x] && nWaterData[y][x-1]<nNum)
	{
		nNum=nWaterData[y][x-1];
		nDir=2;
	}
	if(x+1<nW[i] && nWaterData[y][x+1]<nWaterData[y][x] && nWaterData[y][x+1]<nNum)
	{
		nNum=nWaterData[y][x+1];
		nDir=3;
	}
	if(y+1<nH[i] && nWaterData[y+1][x]<nWaterData[y][x] && nWaterData[y+1][x]<nNum)
	{
		nNum=nWaterData[y+1][x];
		nDir=4;
	}

	switch(nDir)
	{
	case 1:
		fillLine(i, y-1, x);
		break;
	case 2:
		fillLine(i, y, x-1);
		break;
	case 3:
		fillLine(i, y, x+1);
		break;
	case 4:
		fillLine(i, y+1, x);
		break;
	}
}

/*
int compare(const void *argv1, const void *argv2)
{
	int a1, a2, b1, b2;
	
	a1=*(int *)argv1/nW[nCaseNumber];
	b1=*(int *)argv1%nW[nCaseNumber];
	a2=*(int *)argv2/nW[nCaseNumber];
	b2=*(int *)argv2%nW[nCaseNumber];

	return -nWaterData[a1][b1]+nWaterData[a2][b2];
}
*/

bool compare(int argv1, int argv2)
{
	int a1, a2, b1, b2;

	a1=argv1/nW[nCaseNumber];
	b1=argv1%nW[nCaseNumber];
	a2=argv2/nW[nCaseNumber];
	b2=argv2%nW[nCaseNumber];

	return nWaterData[a1][b1]>nWaterData[a2][b2];
}