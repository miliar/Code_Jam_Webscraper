#include <iostream>
#include <cstdio>
#include <map>
#include <string>
#include <set>

using namespace std;

map<char, char> m;
set<char> key;
set<char> value;

void add(string a, string b) {
	for (int i = 0; i < (int)a.length(); ++i) {
		key.erase(a[i]);
		value.erase(b[i]);
		m[a[i]] = b[i];
	}
}

string trans(string s) {
	for (int i = 0; i < (int)s.length(); ++i)
		s[i] = m[ s[i] ];

	return s;
}

void solve() {
	for (char c = 'a'; c <= 'z'; c++)
	{
		key.insert(c);
		value.insert(c);
	}
	add("y qee", "a zoo");
	add("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
	add("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
	add("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");

	m[*key.begin()] = *value.begin();
	cerr << m.size() << endl;	

	string s;
	while (s == "")
		getline(cin, s);

	static int testID;
	cout << "Case #" << ++testID << ": " << trans(s) << endl;
}

int main() {
	int t;
	cin >> t;
	while (t--)
		solve();
	return 0;
}
