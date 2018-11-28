// prjQ2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <iostream>
#pragma warning (disable: 4996)
using namespace std;

int nLine;
vector<string> SampleList;
string target = "welcome to code jam";

int lookupTable[512][20] = {0};

int generate(int sample_index)
{
	string curSample = SampleList[sample_index];

	for(size_t i=0; i<curSample.length(); ++i)
	{
		int tableX = i+1;
		for(int j=0; j<20; j++)
		{
			int tableY = j+1;
			lookupTable[tableX][tableY] = lookupTable[tableX-1][tableY];
			if(curSample[i] == target[j])
			{
				if(j==0) 
				{
					lookupTable[tableX][tableY]++;
				}
				lookupTable[tableX][tableY] += lookupTable[tableX-1][tableY-1];
			}
		}
	}

	int h = curSample.length();
	return lookupTable[h][19];
}

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fptr = NULL;
	fopen_s(&fptr, "D:\\C-small-attempt0.in", "r");

	fscanf(fptr, "%d\n", &nLine);
	for(int i=0; i<nLine; i++)
	{
		char buf[512] = {0};
		fscanf(fptr, "%[^\n]\n", buf);
		string tmp = buf;
		SampleList.push_back(tmp);
	}		
	fclose(fptr);

	FILE *optr = NULL;
	fopen_s(&optr, "D:\\output.out", "w");
	for(int index=0; index < nLine; ++index)
	{
		int ans = generate(index);
		fprintf(optr, "Case #%d: %04d\n", index+1, ans);		
	}
	
	fclose(optr);

	return 0;
}

