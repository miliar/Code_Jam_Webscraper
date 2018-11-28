#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

int c;

set<char> break_string(const string& str)
{
	set<char> sc;
	int i;

	for (i = 0; i < str.size(); i++)
		sc.insert(str[i]);

	return sc;
}

void backtrack(const vector<string>& dic, const map<int, set<char> >& misc,
			  string make, int p, int L)
{
	int i;

	if (p == L)
	{
		if (find(dic.begin(), dic.end(), make) != dic.end())
			c++;
		return;
	}

	for (i = 0; i < dic.size() && make.size(); i++)
		if (dic[i].substr(0, make.size()) == make)
			break;
	if (i == dic.size())
		return;

	set<char>::const_iterator siter = misc.find(p)->second.begin();
	set<char>::const_iterator siter_end = misc.find(p)->second.end();
	while(siter != siter_end)
	{
		backtrack(dic, misc, make + *siter, p+1, L);
		siter++;
	}
}

int main()
{
	int L, D, N, i, j, k, p;
	string pattern;

	while(cin >> L >> D >> N)
	{
		vector<string> dic(D);

		for (i = 0; i < D; i++)
			cin >> dic[i];

		for (i = 0; i < N; i++)
		{
			cin >> pattern;

			map<int, set<char> > misc;
			map<int, set<char> >::iterator miter;

			for (j = p = 0; j < pattern.size(); j++, p++)
			{
				if (pattern[j] == '(')
				{
					k = pattern.find(')', j+1);
					misc.insert(make_pair(p, break_string(pattern.substr(j+1, k-(j+1)))));
					j = k;
				}
				else
					misc.insert(make_pair(p, break_string(pattern.substr(j, 1))));
			}

			/*
			for (miter = misc.begin(); miter != misc.end(); miter++)
			{
				cout << miter->first << ":::::::\n";
				set<char>::iterator siter;
				for (siter = miter->second.begin(); siter != miter->second.end(); siter++)
					cout << *siter << ' ';
				cout << "\n-------------\n";
			}
			*/

			c = 0;
			miter = misc.begin();
			backtrack(dic, misc, "", 0, L);

			cout << "Case #" << i+1 << ": " << c << endl;
		}
	}

	return 0;
}
