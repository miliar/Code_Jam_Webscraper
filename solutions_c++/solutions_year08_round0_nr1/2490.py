#include <iostream>
#include <string>
#include <vector>

using namespace std;

typedef unsigned int uint;

struct Srch
{
	string strName;
	bool bFound;
};

uint uiNos;
Srch *pS;

uint uiNoq;
vector<string> vecQ;

int geti()
{
	char p[110];
	gets_s(p, 110);
	return atoi(p);
}

void input()
{
	char p[110];
	uiNos = geti();
	pS = new Srch[uiNos];
	for(uint i = 0; i < uiNos; ++i)
	{
		gets_s(p, 110);
		pS[i].strName = p;
	}
	uiNoq = geti();
	for(uint i = 0; i < uiNoq; ++i)
	{
		gets_s(p, 110);
		vecQ.push_back(p);
	}
}

void reset(string strQ)
{
	for(uint i = 0; i < uiNos; ++i)
		if(strQ == pS[i].strName)
			pS[i].bFound = true;
		else
			pS[i].bFound = false;
}

bool lastFound(string strQ)
{
	uint uiR = 0;
	for(uint i = 0; i < uiNos; ++i)
		if(pS[i].bFound == false)
			if(pS[i].strName != strQ)
				++uiR;
			else
				pS[i].bFound = true;

	return(uiR == 0)? true : false;
}

int main()
{
	int iN = geti();
	vector<uint> vecO;
	for(int i = 0; i < iN; ++i)
	{
		input();
		string strCur = "";
		uint uiSwitch = 0;
		vector<string>::iterator itrQ;
		bool bProc = false;
		for(itrQ = vecQ.begin(); itrQ != vecQ.end(); )
		{
			if(strCur == "")
			{
				strCur = *itrQ;
				reset(strCur);
				itrQ++;
				if(itrQ == vecQ.end())
					break;
			}
			if(lastFound(*itrQ))
			{
				++uiSwitch;
				strCur = "";
				continue;
			}
			itrQ++;
		}
		vecO.push_back(uiSwitch);
		delete []pS;
		vecQ.clear();
	}
	cout << endl;
	vector<uint>::iterator itrO = vecO.begin();
	for(int i = 0; i < iN; )
	{
		cout << "Case #" << ++i << ": " << *itrO << endl;
		itrO++;
	}
	return 0;
}