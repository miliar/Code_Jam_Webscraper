#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>

using namespace std;

typedef unsigned int uint;

int main(int argc, char *argv[])
{
	//ifstream in("test.in");
	//ofstream out("out.in");
	ifstream in("A-small-attempt1.in");
	ofstream out("A-small-attempt1.out");
	int caseCount;
	in>>caseCount;
	for(int caseIndex=0; caseIndex<caseCount; caseIndex++)
	{
		string digitStr;
		in>>digitStr;
		if(digitStr.length() == 1)
		{
			cout<<"Case #"<<caseIndex+1<<": 1"<<endl;
			out<<"Case #"<<caseIndex+1<<": 1"<<endl;
			continue;
		}
		int currentBase = 2, nextEarthDigit = 0;
		map<char, uint> digitMap;
		vector<uint> earthDigits;
		digitMap.insert(map<char, uint>::value_type(digitStr[0], 1));
		earthDigits.push_back(1);
		for(uint i=1; i<digitStr.length(); i++)
		{
			char & digit = digitStr[i];
			if(digitMap.count(digit))
			{
				earthDigits.push_back(digitMap[digit]);
			}
			else
			{
				digitMap.insert(map<char, uint>::value_type(digit, nextEarthDigit));
				earthDigits.push_back(nextEarthDigit);
				nextEarthDigit++;
				if(nextEarthDigit == 1)
				{
					nextEarthDigit++;
				}
				else if(nextEarthDigit > 1)
				{
					currentBase = nextEarthDigit;
				}
			}
		}
		uint b=1,earthNum=0;
		for(int i=earthDigits.size()-1; i>=0; i--)
		{
			earthNum += b * earthDigits[i];
			b *= currentBase;
		}
		cout<<"Case #"<<caseIndex+1<<": "<<earthNum<<endl;
		out<<"Case #"<<caseIndex+1<<": "<<earthNum<<endl;
	}
	system("pause");
	return 0;
}