#include <vector>
#include <set>
#include <string>
#include <fstream>
 
using namespace std;

class CCase{
public:
	CCase(const set<string>& Engines, const vector<string>& Queries)
		:m_Engines(Engines), m_Queries(Queries)
	{
	}

	const set<string>& GetEngines() const { return m_Engines; }
	const vector<string>& GetQueries() const { return m_Queries; }

private:
	set<string>		m_Engines;
	vector<string>	m_Queries;
};

string SolveCase(const CCase& Case, vector<CCase>::size_type iCaseIndex);
void FindBestEngine(const CCase& Case, vector<string>::size_type* piCurrentQuery);
vector<string>::size_type FindFirst(string sEngine, const vector<string>& Queries, vector<string>::size_type iCurrentQuery);
void ParseInput(string sInput, vector<CCase>* pInput);
string IntToString(int i);

string SolveSavingTheUniverse()
{
	string
		sOutput;
	vector<CCase>
		Input;
	ParseInput("Input.txt", &Input);

	vector<CCase>::size_type
		i;
	for (i = 0; i < Input.size(); ++i)
		sOutput += SolveCase(Input[i], i) + "\n";

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
			iEngineCount, iQueryCount;
		is >> iEngineCount;
		set<string>
			Engines;
		for (int j = 0; j < iEngineCount; ++j){
			char
				arch[1024];
			is.getline(arch, 1024);
			string
				sEngine = arch;
			if (!sEngine.empty())
				Engines.insert(sEngine);
			else
				--j;
		}

		is >> iQueryCount;
		vector<string>
			Queries;
		for (int j = 0; j < iQueryCount; ++j){
			char
				arch[1024];
			is.getline(arch, 1024);
			string
				s = arch;
			if (!s.empty())
				Queries.push_back(s);
			else
				--j;
		}

		pInput->push_back(CCase(Engines, Queries));
	}
}

string SolveCase(const CCase& Case, vector<CCase>::size_type iCaseIndex)
{
	string
		sOutput;
	int
		iSwichCount = 0;
	vector<string>::size_type
		iCurrentQuery = 0;

	while (iCurrentQuery < Case.GetQueries().size()){
		FindBestEngine(Case, &iCurrentQuery);
		if (iCurrentQuery < Case.GetQueries().size())
			++iSwichCount;
	}

	sOutput = "Case #" + IntToString(iCaseIndex + 1) + ": " + IntToString(iSwichCount);

	return sOutput;
}

void FindBestEngine(const CCase& Case, vector<string>::size_type* piCurrentQuery)
{
	string
		sBestEngine;
	vector<string>::size_type
		iBestEnginePos = 0;
	set<string>::const_iterator
		it;
	for (it = Case.GetEngines().begin(); it != Case.GetEngines().end(); ++it){
		vector<string>::size_type
			iCurrentEnginePos = FindFirst(*it, Case.GetQueries(), *piCurrentQuery);
		if (iCurrentEnginePos > iBestEnginePos){
			sBestEngine = *it;
			iBestEnginePos = iCurrentEnginePos;
		}
	}

	*piCurrentQuery = iBestEnginePos;
}

vector<string>::size_type FindFirst(string sEngine, const vector<string>& Queries, vector<string>::size_type iCurrentQuery)
{
	vector<string>::size_type
		iCurrentPos;
	for (iCurrentPos = iCurrentQuery;
		iCurrentPos < Queries.size() && Queries[iCurrentPos] != sEngine;
		++iCurrentPos)
	{
	}

	return iCurrentPos;
}

string IntToString(int i)
{
	char
		arch[64];
	string
		s	= _itoa(i, arch, 10);

    return s;
}
