#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

ifstream myin("A-large.in");		//A-small-attempt0.in");
ofstream myout("1.out");


int main()
{
	int T;
	myin >> T;
	for(int i=1; i<=T; ++i)
	{
		string instr;
		set<char> letterSet;
		int base;
		myin >> instr;
		for(int pos=0; pos<instr.size(); pos++)
		{
 			letterSet.insert(instr[pos]);
		}
		base = letterSet.size();
		if(base == 1)
			base = 2;
		
		map<char, int> auxMap;
		string resStr;
		auxMap[instr[0]] = 1;
		int lastNum = 1;
		resStr += '0' + 1;
		map<char, int>::iterator it;
		for(int pos=1; pos<instr.size(); pos++)
		{
			it = auxMap.find(instr[pos]);
			if(it == auxMap.end())
			{
				if(lastNum == 1)
				{
					auxMap[instr[pos]] = 0;
					lastNum = 0;
				}
				else if(lastNum == 0)
				{
					auxMap[instr[pos]] = 2;
					lastNum = 2;
				}
				else
				{
					auxMap[instr[pos]] = ++lastNum;
				}
			}
			resStr += '0' + auxMap[instr[pos]];
		}

		long long res=0, w=1;
		for(int pos=instr.size()-1; pos>=0; --pos)
		{
			res += (long long)(resStr[pos]-'0') * (long long)w;
			w *= (long long)base;
		}

		myout << "Case #" << i << ": " << res << endl;
	}
	return 0;
}