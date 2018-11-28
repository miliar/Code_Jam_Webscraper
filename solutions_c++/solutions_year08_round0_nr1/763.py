#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <string>

using namespace std;

int main()
{
	int caseNum = 0;
	string str;
	int n;
	getline(cin, str);
	sscanf(str.c_str(), "%d", &n);
	// Read each test case
	for (int i = 0; i < n; ++i)
	{
		// Read search engines
		int s;
		getline(cin, str);
		sscanf(str.c_str(), "%d", &s);
		vector<string> searchEngines;
		for (int i = 0; i < s; ++i)
		{
			string name;
			getline(cin, name);
			searchEngines.push_back(name);
		}

		// Process queries
		int q;
		getline(cin, str);
		sscanf(str.c_str(), "%d", &q);
		int hit = 0;
		set<string> appeared;
		int ret = 0;
		for (int i = 0; i < q; ++i)
		{
			string query;
			getline(cin, query);
			if (appeared.find(query) == appeared.end())
			{
				++hit;
				if (hit == searchEngines.size())
				{
					hit = 1;
					++ret;
					appeared.clear();
				}
				appeared.insert(query);
			}
		}

		printf("Case #%d: %d\n", ++caseNum, ret);
	}

	return 0;
}
