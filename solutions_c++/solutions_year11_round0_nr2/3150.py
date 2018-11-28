#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

int main(int argc, char** argv)
{
	int tests;
	cin >> tests;
	for (int i = 0; i < tests; ++i)
	{
		map <string, char> reactions;
		map <char, set <char> > annihilations;
		string s = "", t;
		int C, D, N;
		cin >> C;
		for (int j = 0; j < C; ++j)
		{
			cin >> t;
			reactions[s + t[0] + t[1]] = t[2];
			reactions[s + t[1] + t[0]] = t[2];
		}
		cin >> D;
		for (int j = 0; j < D; ++j)
		{
			cin >> t;
			annihilations[t[0]].insert(t[1]);
			annihilations[t[1]].insert(t[0]);
		}
		cin >> N;
		cin >> t;
		map <char, int> reset;
		for (int j = 0; j < t.size(); ++j)
		{
			s += t[j];
			annihilations[t[j]];
			for (set <char>::iterator k = annihilations[t[j]].begin(); k != annihilations[t[j]].end(); ++k)
				++reset[*k];
			while (s.size() >= 2 && (reactions.count(string(s.end() - 2, s.end())) || reset[s[s.size() - 1]]))
			{
				if (reactions.count(string(s.end() - 2, s.end())))
				{
					annihilations[t[s[s.size() - 2]]];
					annihilations[t[s[s.size() - 1]]];
					for (int a = 1; a <= 2; ++a)
						for (set <char>::iterator k = annihilations[s[s.size() - a]].begin(); k != annihilations[s[s.size() - a]].end(); ++k)
							reset[*k] = max(0, reset[*k] - 1);
					s = string(s.begin(), s.end() - 2) + reactions[string(s.end() - 2, s.end())];
				}
				else
				{
					s = "";
					reset.clear();
				}
			}
		}
		cout << "Case #" << (i + 1) << ": [";
		for (int j = 0; j < s.size(); ++j)
			cout << s[j] << (j == s.size() - 1 ? "" : ", ");
		cout << "]" << endl;
	}
	return 0;
}
