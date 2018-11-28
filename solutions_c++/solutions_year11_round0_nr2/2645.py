#include <iostream>
#include <string>
#include <set>
#include <map>
#include <vector>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t)
	{
		int C, D, N;

		map<pair<char, char>, char> cmb;
		cin >> C;
		while (C--)
		{
			string s;
			cin >> s;
			cmb[make_pair(s[0], s[1])] = s[2];
			cmb[make_pair(s[1], s[0])] = s[2];
		}

		set<pair<char, char>> opp;
		cin >> D;
		while (D--)
		{
			string s;
			cin >> s;
			opp.insert(make_pair(s[0], s[1]));
			opp.insert(make_pair(s[1], s[0]));
		}

		cin >> N;
		string cmd;
		cin >> cmd;
		vector<char> elem;
		for (int i = 0; i < N; ++i)
		{
			char c = cmd[i];

			bool reaction = false;
			if (elem.size() > 0)
			{
				// check combi
				auto it = cmb.find(make_pair(elem.back(), c));
				if (it != cmb.end())
				{
					elem.back() = it->second;
					reaction = true;
				}
				else
				{
					// check opp
					for (auto it = elem.begin(); it != elem.end(); ++it)
					{
						if (opp.count(make_pair(*it, c)) > 0)
						{
							elem.clear();
							reaction = true;
							break;
						}
					}
				}
			}

			// none
			if (!reaction)
				elem.push_back(c);
		}

		cout << "Case #" << t << ": [";
		if (elem.size() > 0)
		{
			for (int i = 0; i < elem.size() - 1; ++i)
				cout << elem[i] << ", ";
			cout << elem.back();
		}
		cout << "]" << endl;
	}

	return 0;
}
