#include "stdafx.h"

#include <vector>
#include <set>
#include <string>
#include <fstream>
 
using namespace std;

struct STree{
	STree(__int64 x_, __int64 y_): x(x_), y(y_) {}
	__int64 x, y;
};

// class CCase{
// public:
// 	CCase(const set<string>& Engines, const vector<string>& Queries)
// 		:m_Engines(Engines), m_Queries(Queries)
// 	{
// 	}
// 
// 	vector<STree>	m_Tries;
// };

typedef vector<STree> CCase;

string SolveCase(const CCase& Case, vector<CCase>::size_type iCaseIndex);
void ParseInput(string sInput, vector<CCase>* pInput);
string IntToString(__int64 i);


string SolveCropTriangles()
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
	__int64
		iCaseCount;
	is >> iCaseCount;

	for (__int64 i = 0; i < iCaseCount; ++i){
		__int64
			n, A, B, C, D, x0, y0, M;
		is >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		
		__int64
			X = x0, Y = y0;
		CCase
			Case;
		Case.push_back(STree(X, Y));

		for (__int64 i = 1; i < n; ++i)
		{
			X = (A*X+B)%M;			
			Y = (C*Y+D)%M;
			Case.push_back(STree(X, Y));
		}

		pInput->push_back(Case);
	}
}

string SolveCase(const CCase& Case, vector<CCase>::size_type iCaseIndex)
{
	string
		sOutput;
	__int64
		iResult = 0;

	for (__int64 i = 0; i < Case.size(); ++i)
		for (__int64 j = 0; j < Case.size(); ++j)
			for (__int64 k = 0; k < Case.size(); ++k)
				if (i > j && j > k){
					if (((Case[i].x + Case[j].x + Case[k].x) / 3ll) * 3ll == Case[i].x + Case[j].x + Case[k].x
							&& ((Case[i].y + Case[j].y + Case[k].y) / 3ll) * 3ll == Case[i].y + Case[j].y + Case[k].y)
						++iResult;
				}

	sOutput = "Case #" + IntToString(iCaseIndex + 1) + ": " + IntToString(iResult);

	return sOutput;
}

string IntToString(__int64 i)
{
	char
		arch[64];
	string
		s	= _itoa(i, arch, 10);

    return s;
}