#include <iostream>
#include <string>
#include <map>
using namespace std;

string s[] = {
	"ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv",
	"qz"
};
string t[] = {
	"our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up",
	"zq"
};

map<char, char> f;

void translate(string & ln) {
	for (int i = 0; i < ln.size(); i++) {
		ln[i] = f[ln[i]];
	}
}

int main() {
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < s[i].size(); j++) {
			f[s[i][j]] = t[i][j];
		}
	}

	int t; cin >> t; cin.ignore(1);
	for (int i = 1; i <= t; i++) {
		string ln;
		getline(cin, ln);

		translate(ln);

		cout << "Case #" << i << ": " << ln << endl;
	}
	return 0;
}

