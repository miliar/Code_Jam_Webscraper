#include <iostream>
#include <map>
#include <set>
#include <string>
using namespace std;

int main()
{
	string s[] = {"y qee",
		"ejp mysljylc kd kxveddknmc re jsicpdrysi", 
		"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
		"de kr kd eoya kw aej tysr re ujdr lkgc jv"};

	string t[] = {"a zoo",
		"our language is impossible to understand",
		"there are twenty six factorial possibilities",
		"so it is okay if you want to just give up"};

	map<char, char> m;
	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < s[i].length(); ++j) {
			if (isalpha(s[i][j])) {
				if (m.find(s[i][j]) != m.end() && m[s[i][j]] != t[i][j]) {
					throw 42;
				}
				m[s[i][j]] = t[i][j];
			}
		}
	}
	set<int> remchar1, remchar2;
	for (char c = 'a'; c <= 'z'; ++c) {
		remchar1.insert(c);
		remchar2.insert(c);
	}
	for (map<char, char>::iterator i = m.begin(), iend = m.end(); i != iend; ++i) {
		remchar1.erase(i->first);
		remchar2.erase(i->second);
	}
	m[*remchar1.begin()] = *remchar2.begin();

	{
		int tests;
		string s;
		cin >> tests;
		getline(cin, s);
		for (int test = 1; test <= tests; ++test) {
			getline(cin, s);
			string result;
			for (size_t i = 0, ilen = s.length(); i < ilen; ++i) {
				result.push_back(s[i] == ' ' ? ' ' : m[s[i]]);
			}
			cout << "Case #" << test << ": " << result << endl;
		}
	}

}
