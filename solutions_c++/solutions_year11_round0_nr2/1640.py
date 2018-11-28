#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <list>
#include <bitset>
using namespace std;

typedef pair<int, int> pii;

const bool DEBAG_OUTPUT = false;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;

	for (int t = 0; t < T; ++ t)
	{
		int D;
		cin >> D;

		vector< vector<char> > combine(257, vector<char>(257, 0));
		vector< vector<bool> > opposed(257, vector<bool>(257, false));

		for (int i = 0; i < D; ++ i)
		{
			string s;
			cin >> s;

			combine[s[0]][s[1]] = s[2];
			combine[s[1]][s[0]] = s[2];
		}

		cin >> D;

		for (int i = 0; i < D; ++ i)
		{
			string s;
			cin >> s;

			opposed[s[0]][s[1]] = true;
			opposed[s[1]][s[0]] = true;
		}

		list<char> l;

		int n;
		cin >> n;

		string s;
		cin >> s;
		if (n != s.size())
		{
			cout << "FAIL LENGTH OF STRING!!!!!!";
			exit(0);
		}
		for (int i = 0; i < n; ++ i)
		{
			if (l.empty())
			{
				l.push_back(s[i]);
				continue;
			}

			char c = l.back();
			if (combine[c][s[i]] != 0)
			{
				l.pop_back();
				l.push_back(combine[c][s[i]]);
				continue;
			}
			for (list<char>::iterator it = l.begin(); it != l.end(); ++ it)
			{
				if (opposed[*it][s[i]])
				{
					l.clear();
					break;
				}
			}
			if (!l.empty())
				l.push_back(s[i]);
		}

		cout << "Case #" << t + 1 << ": [";

		for (list<char>::iterator it = l.begin(); it != l.end(); ++ it)
		{
			if (it != l.begin())
				cout << ", ";
			cout << *it;
		}

		cout << "]\n";
	}
	return 0;
}
