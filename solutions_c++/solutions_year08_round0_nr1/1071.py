#include <stdlib.h>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>

using namespace std;

class SavingUniverse
{
public:
	static int GetSwitches(vector<string> engines, vector<string> queries)
	{
		int res = 0;
		set<string> used;
		for (size_t i = 0; i < queries.size(); ++i)
		{
			used.insert(queries[i]);
			if (used.size() == engines.size())
			{
				++res;
				used.clear();
				used.insert(queries[i]);
			}
		}
		return res;
	}
};

int main()
{
	ifstream ifstr("A-large.in");
	ofstream ofstr("A-large.out");
	char buf[256];
	ifstr.getline(buf, 256);
	int count = atoi(buf);
	for (int i = 1; i <= count; ++i)
	{
		vector<string> engines, queries;
		ifstr.getline(buf, 256);
		int ecount = atoi(buf);
		for (int j = 0; j < ecount; ++j)
		{
			ifstr.getline(buf, 256);
			engines.push_back(buf);
		}
		ifstr.getline(buf, 256);
		int qcount = atoi(buf);
		for (int j = 0; j < qcount; ++j)
		{
			ifstr.getline(buf, 256);
			queries.push_back(buf);
		}
		ofstr << "Case #" << i << ": " << SavingUniverse::GetSwitches(engines, queries) << "\n";
	}

	return 0;
}
