// cgj2012-1.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <map>
#include <algorithm>
#include <string>
#include <iterator>
#include <vector>

using namespace std;

void process(map<char, char> &m, string s1, string s2) {
	for (int i = 0; i < s1.size(); ++i) {
		if (s1[i] != ' ') {
			m[s1[i]] = s2[i];
		}
	}
}

int main(int argc, char* argv[])
{
	map<char, char> m;
	map<char, char> m1;
	m['a'] = 'y';
	m['o'] = 'e';
	m['z'] = 'q';
	m[' '] = ' ';
	m['q'] = 'z';
	process(m, "our language is impossible to understand", "ejp mysljylc kd kxveddknmc re jsicpdrysi");
	process(m, "there are twenty six factorial possibilities", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
	process(m, "so it is okay if you want to just give up", "de kr kd eoya kw aej tysr re ujdr lkgc jv");

	for_each(m.begin(), m.end(), [&] (pair<char, char> p) { m1[p.second] = p.first;});

	char buf[555];

	int T;
	cin >> T; 
	cin.getline(buf, 500);
	for (int i = 1; i <= T; ++i) {
		string s;
		cin.getline(buf, 500);
		s = buf;
		cout << "Case #" << i << ": ";
		transform(s.begin(), s.end(), ostream_iterator<char>(cout), [&](char c) { return m1[c]; });
		cout << endl;
	}
	return 0;
}

