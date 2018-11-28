#include <iostream>
#include <utility>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <functional>
#include <iomanip>
#include <math.h>
#include <sstream>
#include <locale>
#include <fstream>

using namespace std;


vector<string> vs, vq;

int main()
{
	string str;
	int n,s,q;
	set<string> strset;
	ifstream iFile("A-large.in");
	ofstream oFile("A-large.out");

    int cases = 1;

	getline(iFile,str,'\n');
	istringstream strIn(str.c_str());
	strIn >> n;

	for (;cases<=n;cases++)
	{
		int i;

		vs.resize(0);
		getline(iFile,str,'\n');
		istringstream strs(str.c_str());
		strs >> s;
		for (i=0;i<s;i++)
		{
			getline(iFile,str,'\n');
			vs.push_back(str);
		}

		vq.resize(0);
		getline(iFile,str,'\n');
		istringstream strq(str.c_str());
		strq >> q;
		for (i=0;i<q;i++)
		{
			getline(iFile,str,'\n');
			vq.push_back(str);
		}

		strset.clear();
		string se;
		int res = 0;
		for (i=0;i<q;i++)
		{
			se = vq[i];
			if (!strset.count(se))
			{
				strset.insert(se);
			}

			if (strset.size()==s)
			{
				res++;
				strset.clear();
				strset.insert(se);
			}
		}

		oFile << "Case #" << cases << ": " << res << endl;
	}

	

	return 0;
}

