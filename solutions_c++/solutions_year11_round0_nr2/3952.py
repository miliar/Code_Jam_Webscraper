#include <cassert>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;


int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int testn;
	cin >> testn;

	char combo[256][256];
	bool opp[256][256];

	for (int testi = 0; testi < testn; ++testi)
	{
		memset(combo, 0, sizeof(combo));
		memset(opp, 0, sizeof(opp));

		string str;

		int combon;
		cin >> combon;

		for (int i = 0; i < combon; ++i)
		{
			cin >> str;

			assert(str.length() == 3);
			combo[str[0]][str[1]] = combo[str[1]][str[0]] = str[2];
		}

		int oppn;
		cin >> oppn;

		for (int i = 0; i < oppn; ++i)
		{
			cin >> str;

			assert(str.length() == 2);
			opp[str[0]][str[1]] = opp[str[1]][str[0]] = true;
		}

		int charn;
		cin >> charn;
		cin >> str;

		vector<char> res;

		if (!str.empty())
		{
			res.push_back(str[0]);
		}

		for (int i = 1; i < str.size(); ++i)
		{
			char comb;

			if (!res.empty() && (comb = combo[res.back()][str[i]]) != 0)
			{
				res.pop_back();
				res.push_back(comb);
			}
			else
			{
				res.push_back(str[i]);
			}

			char cur = res.back();

			if (find_if(res.cbegin(), res.cend(), [&opp, &cur](char c) { return opp[c][cur]; }) != res.cend())
			{
				res.clear();
			}
		}

		cout << "Case #" << testi + 1 << ": [";

		if (!res.empty())
		{
			for (int i = 0; i < res.size() - 1; ++i)
			{
				cout << res[i] << ", ";
			}

			cout << res[res.size() - 1];
		}

		cout << "]" << endl;
	}
}