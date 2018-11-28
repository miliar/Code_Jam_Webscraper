#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);	
	freopen("output.txt", "w", stdout);

	int cntTest;
	cin >> cntTest;

	for (int test = 0; test < cntTest; ++test)
	{
		int k, d, n;
		map < pair <char, char> , char > trans;
		vector < pair < char, char > > oppos;
		vector <int> st(256);
		vector <char> res;
		string s;

		cin >> k;
		for (int i = 0; i < k; ++i)
		{
			cin >> s; 
			if (s[0] > s[1]) swap(s[0], s[1]);
			trans[ make_pair(s[0], s[1]) ] = s[2];
		}

		cin >> d;
		for (int i = 0; i < d; ++i)
		{
			cin >> s;
			if (s[0] > s[1]) swap(s[0], s[1]);
			oppos.push_back( make_pair(s[0], s[1]) );
		}

		cin >> n >> s;
		for (int i = 0; i < n; ++i)
		{
			res.push_back(s[i]);
			++st[s[i]];

			if (res.size() >= 2)
			{
				char ch1 = res[(int)res.size() - 1], ch2 = res[(int)res.size() - 2];
				if (ch1 > ch2) swap(ch1, ch2);

				if (trans.find( make_pair(ch1, ch2) ) != trans.end())
				{
					--st[ res[(int)res.size() - 1] ]; res.pop_back();
					--st[ res[(int)res.size() - 1] ]; res.pop_back();
					++st[ trans[ make_pair(ch1, ch2) ] ]; res.push_back( trans[ make_pair(ch1, ch2) ] );
				}
				else
				{
					for (int j = 0; j < d; ++j)
						if (oppos[j].first == s[i] && st[oppos[j].second] || oppos[j].second == s[i] && st[oppos[j].first])
						{
							st = vector <int> (256, 0);
							res.clear();
							break;
						}
				}
			}
		}

		cout << "Case #" << test + 1 << ": [";
		for (int i = 0; i < res.size(); ++i)
			cout << res[i] << (i < (int)res.size() - 1 ? ", " : "");
		cout << "]" << endl;		
	}
}