#include <iostream>
#include <map>
#include <string>
#include <cassert>
#include <algorithm>

using namespace std;

map<char, char> build_index()
{
	string encoded = 
		"ejp mysljylc kd kxveddknmc re jsicpdrysi"
		"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
		"de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string decoded =
		"our language is impossible to understand"
		"there are twenty six factorial possibilities"
		"so it is okay if you want to just give up";
	
	map<char, char> m;
	for (int i = 0; i < encoded.size(); ++i) {
		m[encoded[i]] = decoded[i];
	}
	m['q'] = 'z';
	m['z'] = 'q';
	
	/*
	for (char c = 'a'; c <= 'z'; ++c) {
		if (m.find(c) == m.end()) {
			cout << c << endl;
		}
	}
	cout << endl;
	for (char c = 'a'; c <= 'z'; ++c) {
		bool found = false;
		for (auto it = m.begin(); it != m.end(); ++it) {
			if (it->second == c) {
				found = true;
				break;
			}
		}
		if (!found) cout << c << endl;
	}
	*/
	return m;
}

int main()
{
	map<char, char> m = build_index();
	int ntc;
	cin >> ntc;
	cin.get();
	for (int tc = 1; tc <= ntc; ++tc) {
		string input_line;
		getline(cin, input_line);
		for (auto it = input_line.begin(); it != input_line.end(); ++it) {
			*it = m[*it];
		}
		cout << "Case #" << tc << ": ";
		cout << input_line << endl;

	}
}
