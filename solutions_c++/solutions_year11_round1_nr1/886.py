#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <string>
#include <algorithm>
#include <iterator>
#include <functional>
#include <stdlib.h>

using namespace std;

#define repp(I, Start, End)		for(I = Start; I < End; ++I)
#define rep(I, End)				for( ; I < End; ++I)
#define irep(I, End)			for( ; I != End; ++I)
#define idef(Typ, No, Var)		Typ::const_iterator ite##No = Var.begin();	Typ::const_iterator iteEnd##No = Var.end();
#define it(Typ, No, Var)		idef(Typ, No, Var)	irep(ite##No, iteEnd##No)

int gcd(int x, int y)
{
	int z = x % y;
	if(z)
		return gcd(y, z);
	return y;
}

bool posib(unsigned long long n, int pd, int pg)
{
	if((pg == 100) && (pd != 100))
		return false;
	if((pg == 100) && (pd == 100))
		return true;
	if((pd > 0) && (pg == 0))
		return false;
	if((pd == 0) && (pg == 0))
		return true;
	int g = gcd(100, pd);
	if((100 / g) > n)
		return false;
	
	return true;
}

int main()
{
	ifstream ifs("A-large (1).in");
	ofstream ofs("output.txt");
	string sLine = "";
	bool bFirstLineRead = false;
	int iTestCaseCount = 0;
	int iTestCaseNo = 0;
	while(getline(ifs, sLine))
	{
		istringstream ss(sLine);
		if(!bFirstLineRead)
		{
			ss >> iTestCaseCount;
			bFirstLineRead = true;
			continue;
		}
		++iTestCaseNo;
		if(iTestCaseNo > iTestCaseCount)
			break;

		unsigned long long n;
		int pd, pg;
		ss>>n;
		ss>>pd;
		ss>>pg;

		string str = posib(n, pd, pg) ? "Possible" : "Broken";

		ofs << "Case #" << iTestCaseNo << ": " << str << endl;
	}
}