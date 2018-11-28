#include "stdafx.h"

#include <vector>
#include <set>
#include <string>
#include <fstream>
#include <algorithm>
 
using namespace std;

struct CCase{
	int P, K, L;
	vector<int> Freqs;
};

string SolveCase(CCase& Case, vector<CCase>::size_type iCaseIndex);
void ParseInput(string sInput, vector<CCase>* pInput);
string IntToString(int i);



string Solve()
{
	string
		sOutput;
	vector<CCase >
		Input;
	ParseInput("Input.txt", &Input);

	vector<CCase>::size_type
		i;
	for (i = 0; i < Input.size(); ++i)
		sOutput += SolveCase(Input[i], i) + "\n";

	ofstream
		ofs("Output.txt");
	ofs << sOutput;

	return sOutput;
}

void ParseInput(string sInputFile, vector<CCase>* pInput)
{
	ifstream
		is(sInputFile.c_str());
	int
		iCaseCount;
	is >> iCaseCount;

	for (int i = 0; i < iCaseCount; ++i){
		int
			P, K, L;
		is >> P >> K >> L;
		
		CCase
			Case = {P, K, L};
		Case.Freqs.resize(L);

		for (int i = 0; i < L; ++i){
			int
				iFreq;
			is >> iFreq;
			Case.Freqs.push_back(iFreq);
		}

		pInput->push_back(Case);
	}
}

string SolveCase(CCase& Case, vector<CCase>::size_type iCaseIndex)
{
	string
		sOutput;

	std::sort(Case.Freqs.rbegin(), Case.Freqs.rend());
	int
		iPressCount = 0;
	int
		iCurLetter = 0,
		iCurPlace = 1;

	while (iCurLetter < Case.L){
		for (int i = iCurLetter; i < iCurLetter + Case.K && i < Case.L; ++i)
		{
			iPressCount += iCurPlace * Case.Freqs[i];
		}
		++iCurPlace;
		iCurLetter += Case.K;
	}

	sOutput = "Case #" + IntToString(iCaseIndex + 1) + ": " + IntToString(iPressCount);

	return sOutput;
}

string IntToString(int i)
{
	char
		arch[64];
	string
		s	= _itoa(i, arch, 10);

    return s;
}