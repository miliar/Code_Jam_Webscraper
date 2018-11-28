// G-Task-Welcome-02.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>
 
using namespace std;

#define INPUT_FILE   "c:\\Algorithms\\G-Task-Welcome-02\\data_03_02.txt"
#define OUTPUT_FILE  "c:\\Algorithms\\G-Task-Welcome-02\\out_03_02.txt"
#define NUMBER_FORMATER 10000;
 
int    n_src;
string src;

const int    n_ptrn = 19;
const string ptrn = "welcome to code jam";

int bufTable[500][19];
 
int findSubStr(const int s_src, const int s_ptrn)
{
	if (bufTable[s_src][s_ptrn] != -1){
		return bufTable[s_src][s_ptrn];
	}
	
	int iSrcDiff  = n_src  - s_src;
	int iPtrnDiff = n_ptrn - s_ptrn;
	if (iSrcDiff < iPtrnDiff){
		bufTable[s_src][s_ptrn] = 0;
		return 0;
	}
	
	if (iSrcDiff == iPtrnDiff){
		string sub_src  = src.substr(s_src, iSrcDiff);
		string sub_ptrn = ptrn.substr(s_ptrn, iPtrnDiff);

		bufTable[s_src][s_ptrn] = (sub_src == sub_ptrn) ? 1 : 0;

		return bufTable[s_src][s_ptrn];
	}

	int iCount = 0;
	iCount += findSubStr(s_src+1, s_ptrn);
	iCount %= NUMBER_FORMATER;

	if (src[s_src] == ptrn[s_ptrn]){
		iCount += findSubStr(s_src+1, s_ptrn+1);
		iCount %= NUMBER_FORMATER;
	}

	bufTable[s_src][s_ptrn] = iCount;

	return iCount;
}
 
int main()
{
	ifstream fileIn(INPUT_FILE, ifstream::in);
	FILE* fileOut = fopen(OUTPUT_FILE, "w");

	int iLines;
	fileIn >> iLines;
	getline(fileIn, src);

	for (int i = 0; i < iLines; i++)
	{
		getline(fileIn, src);
		memset(bufTable, -1, 500 * 19);
		n_src = src.length();
		int cnt = findSubStr(0, 0);

		fprintf(fileOut, "Case #%d: %04d\n", i+1, cnt);
	}

	fclose(fileOut);
	fileIn.close();

	return 0;
}

