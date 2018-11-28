// prjQ3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <iostream>
#pragma warning (disable: 4996)
using namespace std;

#define Nlink 0x01
#define Wlink 0x02
#define Elink 0x04
#define Slink 0x08

int mapAry[100][100] = {0};
char vecAry[100][100] = {0};
char ansAry[100][100] = {0};

int H, W;
char curLabel;

void extending(int x, int y)
{
	if(ansAry[y][x] <= curLabel && ansAry[y][x] >= 'a')
		return;
	else
	{
		ansAry[y][x] = curLabel;
		if(vecAry[y][x] & Nlink) extending(x, y-1);
		if(vecAry[y][x] & Slink) extending(x, y+1);
		if(vecAry[y][x] & Wlink) extending(x-1, y);
		if(vecAry[y][x] & Elink) extending(x+1, y);
	}
}

int findWay(int x, int y)
{
	int compare[4] = {65535, 65535, 65535, 65535};

	if(y-1>=0)
		compare[0] = mapAry[y-1][x];
	if(x-1>=0)
		compare[1] = mapAry[y][x-1];
	if(x+1<W)
		compare[2] = mapAry[y][x+1];
	if(y+1<H)
		compare[3] = mapAry[y+1][x];

	int way, cur = 65535;
	for(int i=3; i>=0; i--)
	{
		if(compare[i] <= cur)
		{
			way = i+1;
			cur = compare[i];
		}
	}

	if(mapAry[y][x] > cur) 
		return way;
	else 
		return 0;
}

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *ifptr = NULL;
	FILE *ofptr = NULL;
	fopen_s(&ifptr, "D:\\B-large.in", "r");
	fopen_s(&ofptr, "D:\\output.Qb", "w");

	int nRound = 0;
	fscanf(ifptr, "%d\n", &nRound);
	for(int r=0; r<nRound; r++)
	{
		memset(mapAry, 0, sizeof(int) * 100 * 100);
		memset(vecAry, 0, sizeof(char) * 100 * 100);
		memset(ansAry, 0, sizeof(char) * 100 * 100);
		curLabel = 'a';

		fscanf(ifptr, "%d %d\n", &H, &W);
		for(int i=0; i<H; i++)
		{
			for(int j=0; j<W; j++)
			{
				fscanf(ifptr, "%d ", &mapAry[i][j]);
			}
			char dump;
			fscanf(ifptr, "\n", &dump);
		}

		for(int m = 0; m<H; m++)
		{
			for(int n=0; n<W; n++)
			{
				int way = findWay(n, m);
				switch(way)
				{
				case 0:
					break;
				case 1:
					vecAry[m][n] |= Nlink;
					vecAry[m-1][n] |= Slink;
					break;
				case 2:
					vecAry[m][n] |= Wlink;
					vecAry[m][n-1] |= Elink;
					break;
				case 3:
					vecAry[m][n] |= Elink;
					vecAry[m][n+1] |= Wlink;
					break;
				case 4:
					vecAry[m][n] |= Slink;
					vecAry[m+1][n] |= Nlink;
					break;
				}
			}
		}

		for(int p=0; p<H; p++)
		{
			for(int q=0; q<W; q++)
			{
				if(ansAry[p][q] == 0)
				{
					extending(q, p);
					curLabel++;
				}
			}
		}

		fprintf(ofptr, "Case #%d:\n", r+1);
		for(int h = 0; h<H; h++)
		{
			string tmp = ansAry[h];
			for(int w=0; w<W; w++)
			{
				fprintf(ofptr, "%c ", tmp.c_str()[w]);
			}
			fprintf(ofptr, "\n");			
		}
	}
	fclose(ifptr);
	fclose(ofptr);

	return 0;
}

