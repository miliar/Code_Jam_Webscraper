// GoogleCodeJam-cpp.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <conio.h>
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	// test case 1 reconstructs the example:
	//	2 char typed of a 5 char pass
	// "yy"		"yn"	"ny"	"nn"
	// .6*.6	.6*.4	.4*.6	.4*.4
	//
	//	y[] = {.6,.6}
	//	n[] = {.4,.4}
	//	yn[] = {.6*.6	.6*.4	.4*.6	.4*.4} (sort of)
	//	2 bits of options
	//	11 10 01 11
	//	5 total, 3 remaining
	//	A) keep typing => 5-2=3+<cr>=4 if 11 else 4+5+<cr>=10
	//	B) bs 1ce => 1+5-1=5+<cr>=6 if 11 or 10 else 6+5+<cr>=12
	//	C) bs 2ce => 2+5-0=7+<cr>=8 if any
	//	D) <cr> => 1+5+1=7
	//

	string line;
	ifstream myfile ("a-sample.in");
	if (myfile.is_open())
	{
		bool bSkippedFirstLine = false;
		int caseNum = 1;
		while ( myfile.good() )
		{
			if (!bSkippedFirstLine)
			{
				getline(myfile,line);
				bSkippedFirstLine = true;
			}

			getline(myfile,line);
			stringstream stream1(line);
			string word;

			getline(stream1, word, ' ');
			int nBeenTyped = atoi(word.c_str());
			float *aProbabilities = new float[nBeenTyped];
			float *aImprobabilities = new float[nBeenTyped];
			getline(stream1, word, ' ');
			int nPassLen = atoi(word.c_str());

			getline(myfile,line);
			stringstream stream2(line);
			int nInputCount = 0;
			while( getline(stream2, word, ' ') )
			{
				aProbabilities[nInputCount] = float(atof(word.c_str()));
				aImprobabilities[nInputCount] = 1 - aProbabilities[nInputCount];
				nInputCount++;
			}

			int nRemainingCost = nPassLen - nBeenTyped + 1;	// +1 for <cr>
			// A) uses nRemainingCost
			// B...n) uses nRemainingCost + n
			// Z) always 1 + nPassLen + 1

			float fOptimal = float(1 + nPassLen + 1);
			
			// run through all n digit values. if bit is set then multiply by aProbabilities[n] else by (1-aProbabilities[n])
			// must determine if the error has been corrected.
			//
			// 11 10 01 00 => 1bs corrects the error in 10 only, 2 in all 3
			// 111 110 101 100 011 010 001 000 => 1bs in 110, 2bs in 110 101 100, 3bs in all
			// If the error is corrected then #bs*2 + remaining + <cr>
			// If error is not corrected then #bs*2 + remaining + <cr> + length + <cr>
			// max bs = beentyped
			//
			// if 2 been typed then 1bs corrects only 1. (if n been typed the same goes)
			// if 2 been typed then 2bs corrects 3.
			// if 3 been typed then 1bs corrects only 1. (if n been typed the same goes)
			// if 3 been typed then 2bs corrects 3.
			// if 3 been typed then 3bs corrects 7.
			// if n been typed then mbs corrects 2^m-1.
			// therefore 2^m are correct, 2^n-2^m are incorrect.
			// correct is product of aProbabilities

			float *afProducts = new float[1<<nBeenTyped];
			for (int nIndex = 0; nIndex < 1<<nBeenTyped; nIndex++)
			{
				afProducts[nIndex] = 1.0f;
				for (int nProbIndex = 0; nProbIndex < nBeenTyped; nProbIndex++)
				{
					afProducts[nIndex] *= (nIndex&(1<<nProbIndex))?aProbabilities[nBeenTyped-nProbIndex-1]:aImprobabilities[nBeenTyped-nProbIndex-1];
				}
			}

			// If a prob is 0% then should that method be normalized without it?
			// 3 4
			// 1 .9 .1
			//	yyy		yyn		yny		ynn		nyy		nyn		nny		nnn
			//	0.09	0.81	0.01	0.09	0.00	0.00	0.00	0.00
			// with 1bs: 
			//	4		4		9		9		9		9		9		9
			//	


			for (int nBackSpaces = 0; nBackSpaces <= nBeenTyped; nBackSpaces++)
			{
				float fSum = 0.0f;
				for (int nIndex = 0; nIndex < 1<<nBeenTyped; nIndex++)
				{
					if (nIndex>>nBackSpaces != ((1<<nBeenTyped)-1)>>nBackSpaces)
					{
						fSum += afProducts[nIndex] * (2*nBackSpaces + nRemainingCost + nPassLen+1);
					}
					else
					{
						fSum += afProducts[nIndex] * (2*nBackSpaces + nRemainingCost);
					}
				}
				if (fSum < fOptimal)
				{
					fOptimal = fSum;
				}
			}

			printf("Case #%d: %f\n", caseNum++, fOptimal);

			delete[] aProbabilities;
			delete[] aImprobabilities;
		}

		myfile.close();
	}

	else cout << "Unable to open file"; 


	_getch();

	return 0;
}
