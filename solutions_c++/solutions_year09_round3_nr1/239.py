#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
using namespace std;

long long ipow(int base, int e)
{
	long long result = 1;
	for(int i = 0; i < e; ++i)
		result *= base;
	return result;
}

int main()
{
	ifstream ifs("A-large.in");
	ofstream ofs("res.out");

	int T, caseNo;
	long long result;
	int i;
	set<char> cs;
	map<char, int> cm;
	string str;
	ifs >> T;
	for(int caseNo = 1; caseNo <= T; ++caseNo)
	{
		ifs >> str;
		cs.clear();
		cm.clear();
		for(i = 0; i < str.length(); ++i)
			cs.insert(str[i]);
		int base = cs.size();
		if(base == 1)
			base = 2;
		int len = str.length();
		result = 1 * ipow(base,len-1); 
		cm[str[0]] = 1;
		int tbase = 0;
		for(i = 1; i < len; ++i)
		{
			if(cm.count(str[i]) <= 0)
			{
				cm[str[i]] = tbase;
				tbase++;
				if(tbase == 1)
					++tbase;
			}
			result += cm[str[i]] * ipow(base, len-i-1);
		}

		ofs << "Case #" << caseNo<< ": " << result << endl;
	}

	ifs.close();
	ofs.close();
	
	return 0;
}