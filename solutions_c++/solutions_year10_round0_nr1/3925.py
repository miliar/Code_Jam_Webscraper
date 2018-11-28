// Q1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <vector>
#pragma warning (disable: 4996)
using namespace std;

#define INPUT_FILE "A-large.in"
#define OUTPUT_FILE "A-large.out"

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fptr = NULL;
	fopen_s(&fptr, INPUT_FILE, "r");
	FILE *fout = NULL;
	fopen_s(&fout, OUTPUT_FILE, "w");

	int nCase = 0;
	fscanf_s(fptr, "%d\n", &nCase);
	for(int i=0; i<nCase; i++)
	{
		int nDev, nOp;
		fscanf_s(fptr, "%d %d\n", &nDev, &nOp);
		unsigned __int64 nRound = 1 << nDev;
		
		if(nOp == 0) 
			fprintf(fout, "Case #%d: OFF\n", i+1);
		else
		{
			nOp = nOp % nRound;

			if(nOp == nRound - 1) 
			{
				fprintf(fout, "Case #%d: ON\n", i+1);
			}
			else
			{
				fprintf(fout, "Case #%d: OFF\n", i+1);
			}
		}
	}

	fclose(fptr);
	fclose(fout);
	

	return 0;
}

