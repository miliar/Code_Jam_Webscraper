#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <fstream>
#include <map>
#include <set>
using namespace std;

int main()
{
	string sstr;

	getline(cin, sstr);
	int N = atoi(sstr.c_str());

	for(int i = 1; i <= N; ++i)
	{
		getline(cin, sstr);
		int S = atoi(sstr.c_str());

		set<string> engines;
		for(int j = 0; j < S; ++j)
		{
			string str;
			getline(cin, str);
			engines.insert(str);
		}

		getline(cin, sstr);
		int Q = atoi(sstr.c_str());

		set<string> possible = engines;
		int answer = 0;

		for(int j=0; j < Q; ++j)
		{
			string query;
			getline(cin, query);

			possible.erase(query);
			if (possible.empty())
			{
				possible = engines;
				possible.erase(query);
				++answer;
			}
		}

		cout << "Case #" << i << ": " << answer << endl;
	}

	return 0;
}