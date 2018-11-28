#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <vector>
#include <cmath>
#include <map>
using namespace std;

int main()
{
	int CN;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> CN;
	for (int tc = 0; tc < CN; ++tc)
	{
		int c, d, n;
		cin >> c;
		map < pair <char, char> , char > replacements;
		for (int i = 0; i < c; ++i)
		{
			char c1, c2, c3;
			cin >> c1 >> c2 >> c3;
			replacements[make_pair(c1, c2)] = c3;
			replacements[make_pair(c2, c1)] = c3;
		}
		cin >> d;
		vector < vector <char> > oppositions(26);
		for (int i = 0; i < d; ++i)
		{
			char c1, c2;
			cin >> c1 >> c2;
			oppositions[c1-'A'].push_back(c2);
			oppositions[c2-'A'].push_back(c1);
		}
		cin >> n;
		vector<char> l;
		vector<int> charCount(26);
		for (int i = 0; i < n; ++i)
		{
			char ch;
			cin >> ch;
			l.push_back(ch);
			charCount[ch-'A']++;
			if (l.size() >= 2 && replacements.find(make_pair(l[l.size()-1], l[l.size()-2])) != replacements.end())
			{
				charCount[l[l.size()-2]-'A']--;
				charCount[l[l.size()-1]-'A']--;
				l[l.size()-2] = replacements[make_pair(l[l.size()-1], l[l.size()-2])];
				charCount[l[l.size()-2]-'A']++;
				l.erase(l.end()-1);
			}
			for (int j = 0; j < oppositions[l[l.size()-1]-'A'].size(); ++j)
			{
				if (charCount[oppositions[l[l.size()-1]-'A'][j]-'A'] > 0)
				{
					l.clear();
					charCount.assign(26, 0);
					break;
				}
			}
		}
		cout << "Case #" << tc+1 << ": [";
		for (int i = 0; i < l.size(); ++i)
		{
			cout << l[i];
			if (i != l.size()-1)
				cout << ", ";
		}
		cout << "]" << endl;
	}
}