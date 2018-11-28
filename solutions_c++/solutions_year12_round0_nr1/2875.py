#include <iostream>
#include <fstream>

using namespace std;

int main() {
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);

	string l[3] = {"zqejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
	string c[3] = {"qzour language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"};

	int m[26]; for (int i = 0; i < 26; i++) m[i] = -1;
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < l[i].size(); j++) {
			if (l[i][j] == ' ') continue;
			int ol = l[i][j] - 'a';
			int cl = c[i][j] - 'a';
			m[ol] = cl;
		}
	}

	int T;
	cin >> T;
	string t;
	getline(cin, t);
	for (int x = 1; x <= T; x++) {
		string s;
		getline(cin, s);
		string res = s;
		for (int i = 0; i < s.size(); i++) {
			if (s[i] == ' ') continue;
			res[i] = m[s[i] - 'a'] + 'a';
		}
		cout << "Case #" << x << ": " << res << endl;
	}
}
