#include <fstream>
#include <sstream>
#include <set>
#include <map>
#include <string>

using namespace std;

typedef map<char, char>		MAP_CHAR_CHAR;
typedef set<char>			SET_CHAR;
typedef map<char, SET_CHAR >	MAP_CHAR_SETCHAR;
typedef map<char, MAP_CHAR_CHAR >	MAP_CHAR_MAPCHARCHAR;

int main()
{
	ifstream ifs("B-large.in");
	ofstream ofs("output.txt");
	bool bFirstLineRead = false;
	string sLine = "";
	int iTestCaseCount = 0;
	int iTestCaseNo = 0;

	while(getline(ifs, sLine))
	{
		istringstream ss(sLine);
		if(!bFirstLineRead)
		{
			ss >> iTestCaseCount;
			bFirstLineRead = true;
		}
		else
		{
			++iTestCaseNo;
			int iPairs = 0;
			int iOpposedPairs = 0;
			MAP_CHAR_MAPCHARCHAR	mapPairs;
			MAP_CHAR_SETCHAR		mapOpposedPairs;

			ss >> iPairs;
			int iIndex = 0;
			for( ; iIndex < iPairs; ++iIndex)
			{
				string sPairStr = "";
				ss >> sPairStr;
				char cFirst = sPairStr.at(0);
				char cSecond = sPairStr.at(1);
				char cResult = sPairStr.at(2);
				mapPairs[cFirst];
				(mapPairs[cFirst])[cSecond] = cResult;
				mapPairs[cSecond];
				(mapPairs[cSecond])[cFirst] = cResult;
			}

			ss >> iOpposedPairs;
			iIndex = 0;
			for( ; iIndex < iOpposedPairs; ++iIndex)
			{
				string sOpposedPairStr = "";
				ss >> sOpposedPairStr;
				char cFirst = sOpposedPairStr.at(0);
				char cSecond = sOpposedPairStr.at(1);
				mapOpposedPairs[cFirst];
				(mapOpposedPairs[cFirst]).insert(cSecond);
				mapOpposedPairs[cSecond];
				(mapOpposedPairs[cSecond]).insert(cFirst);
			}

			int iStrLen = 0;
			string sStr = "";
			string sRes = "";

			ss >> iStrLen;
			ss >> sStr;

			iIndex = 0;
			for( ; iIndex < iStrLen; ++iIndex)
			{
				char cCurr = sStr.at(iIndex);
				if(sRes.empty())
				{
					sRes += cCurr;
					continue;
				}
				char cLast = sRes.at(sRes.length() - 1);
				MAP_CHAR_MAPCHARCHAR::iterator iteFind1 = mapPairs.find(cCurr);
				if(mapPairs.end() != iteFind1)
				{
					MAP_CHAR_CHAR::iterator iteFind2 = (*iteFind1).second.find(cLast);
					if((*iteFind1).second.end() != iteFind2)
					{
						sRes[sRes.length() - 1] = (*iteFind2).second;
						continue;
					}
				}

				// look for opposed char
				MAP_CHAR_SETCHAR::iterator iteFind3 = mapOpposedPairs.find(cCurr);
				if(mapOpposedPairs.end() != iteFind3)
				{
					int iPos = 0;
					int iResLen = sRes.length();
					for( ; iPos < iResLen; ++iPos)
					{
						char cc = sRes.at(iPos);
						SET_CHAR::iterator iteFind4 = (*iteFind3).second.find(cc);
						if((*iteFind3).second.end() != iteFind4)
						{
							sRes = "";
							break;
						}
					}
					if(sRes.empty())
					{
						continue;
					}
				}

				sRes += cCurr;
			}

			ofs << "Case #" << iTestCaseNo << ": [";
			int iLen = sRes.length();
			for(int i = 0; i < iLen; ++i)
			{
				if(i > 0)
				{
					ofs << ", ";
				}
				ofs << sRes.at(i);
			}
			ofs << "]" << endl;
		}
	}
}