#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

char code[26];

void translate(int t, string line) {
	cout << "Case #" << t << ": ";
	for (int i = 0; i < line.length(); i++)
		if (line[i] != ' ') cout << code['z' - line[i]];
		else cout << ' ';
	cout << endl;
}

void analyze(string a, string b) {
	for (int i = 0; i < a.length(); i++)
		if (a[i] != ' ') code['z' - a[i]] = b[i];
}

int main() {
	for (int i = 0; i < 26; i++) code[i] = 0;
	analyze("y qee", "a zoo");
	analyze("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
	analyze("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
	analyze("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");
    code[0] = 'q';

	int tc; cin >> tc;
	string dummy; getline(cin, dummy);
	for (int i = 0; i < tc; i++) {
		string line;
		getline(cin, line);
		translate(i + 1, line);
	}

	return 0;
}

