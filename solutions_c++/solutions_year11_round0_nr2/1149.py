#include <cstdio>
#include <algorithm>
#include <vector>
#include <cassert>
#include <cmath>
#include <sstream>
#include <string>
#include <map>
using namespace std;

map<string, string> nonBaseElements;
map<char, char> opposed;
string sList;

void readTestCase()
{
	nonBaseElements.clear();
	opposed.clear();
	
	int iNonBaseElements;
	scanf("%d", &iNonBaseElements);
	char acCombination[4];
	for(int i=0; i<iNonBaseElements; i++)
	{
		scanf("%s", acCombination);
		const string sComb(acCombination);
		string s = sComb.substr(0,2);
		nonBaseElements[s] = sComb.substr(2);
		swap(s[0], s[1]);
		nonBaseElements[s] = sComb.substr(2);
	}
	
	int iOpposed;
	scanf("%d", &iOpposed);
	for(int i=0; i<iOpposed; i++)
	{
		scanf("%s", acCombination);
		opposed[acCombination[0]] = acCombination[1];
		opposed[acCombination[1]] = acCombination[0];
	}
	
	scanf("%d", &iOpposed);
	char acList[101];
	scanf("%s", acList);
	sList = acList;
	assert(sList.size() == iOpposed);
}

void compute()
{
	assert( sList.size() );
	string sRes = sList.substr(0,1);
	for(int iCurrChar = 1; iCurrChar < sList.size(); iCurrChar++)
	{
		if (sRes.size())
		{
			string sLastTwo = sRes.substr(sRes.size()-1); 
			sLastTwo += sList[iCurrChar];
			
			map<string,string>::iterator it = nonBaseElements.find(sLastTwo);
			if (it!=nonBaseElements.end())
			{
				sRes = sRes.substr(0, sRes.size()-1) + it->second;
			}
			else
			{
				if (find(sRes.begin(), sRes.end(), opposed[sList[iCurrChar]])
					!=sRes.end())
					sRes.clear();
				else
					sRes += sList[iCurrChar];
			}
		}
		else
			sRes += sList[iCurrChar];
	}
	
	sList = sRes;
}

void writeAnswer()
{
	printf("[");
	for(int i=0; i+1<sList.size(); i++)
		printf("%c, ", sList[i]);
	if (sList.size())
		printf("%c", sList[sList.size()-1]);
	printf("]\n");
}

int main()
{
	int iTests;
	scanf("%d", &iTests);
	for(int iTestCase = 1; iTestCase <= iTests; iTestCase++)
	{
		readTestCase();
		compute();
		printf("Case #%d: ", iTestCase);
		writeAnswer();
	}
	
	return 0;
}
 
