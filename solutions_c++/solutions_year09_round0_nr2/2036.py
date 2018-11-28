// G-Task-Watersheld-02.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
 
using namespace std;

#define INPUT_FILE  "c:/Algorithms/G-Task-Watersheld-02/data_02_03.txt" 
#define OUTPUT_FILE "c:/Algorithms/G-Task-Watersheld-02/out_02_03.txt" 

#define MAX_H 100
#define MAX_W 100

int  inMap[MAX_W][MAX_H]  = {0};
char outMap[MAX_W][MAX_H] = {0};
 
int W;
int H;
 
char chLabel = 'a';
 
int processCell(int r, int c)
{
	if (outMap[r][c] != 0)
	{
		return outMap[r][c];
	}

	int iUp    = -1;
	int iLeft  = -1;
	int iRight = -1;
	int iDown  = -1;
	
	if (r > 0)       iUp    = inMap[r][c] - inMap[r-1][c];
	if (c > 0)       iLeft  = inMap[r][c] - inMap[r][c-1];
	if (c < (W - 1)) iRight = inMap[r][c] - inMap[r][c+1];
	if (r < (H - 1)) iDown  = inMap[r][c] - inMap[r+1][c];

	if ((iUp <= 0) && (iLeft <= 0) && (iRight <= 0) && (iDown <= 0))
	{
		outMap[r][c] = chLabel;
		chLabel++;
	}
	else
	{
		int max_diff = iUp;
		int dr = -1; 
		int dc = 0;

		if (iLeft > max_diff)
		{
			max_diff = iLeft;
			dr = 0; 
			dc = -1;
		}

		if (iRight > max_diff)
		{
			max_diff = iRight;
			dr = 0; 
			dc = 1;
		}

		if (iDown > max_diff)
		{
			dr = 1; 
			dc = 0;
		}

		outMap[r][c] = outMap[r + dr][c + dc] != 0 ? outMap[r + dr][c + dc] : processCell(r + dr, c + dc);
	}

	return outMap[r][c];
}

int main()
{
	ifstream fileIn(INPUT_FILE);
	ofstream fileOut(OUTPUT_FILE);

	int iLines;
	fileIn >> iLines;
 
	for (int n = 0; n < iLines; n++)
	{
		chLabel = 'a';
		int a;

		fileIn >> H >> W;

		for (int i = 0; i < H; i++)
		{
			for (int j = 0; j < W; j++)
			{
				fileIn >> a;
				inMap[i][j]  = a;
				outMap[i][j] = 0;
			}
		}

		for (int i = 0; i < H; i++)
		{
			for (int j = 0; j < W; j++)
				if (outMap[i][j] == 0) 
					processCell(i, j);
		}

		fileOut << "Case #" << (n + 1) << ":" << endl;
		for (int i = 0; i < H; i++)
		{
			for (int j = 0; j < W; j++)	
				fileOut << outMap[i][j] << ' ';

			fileOut << endl;
		}
	}

	fileOut.close();
	fileIn.close();

	return 0;
}

