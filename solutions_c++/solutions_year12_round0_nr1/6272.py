#include <iostream>
using namespace std;


int n;
string s;
char mapping[256];
char what[3][45] = {
	"our language is impossible to understand    ",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up   "
};
char into[3][45] = {
	"ejp mysljylc kd kxveddknmc re jsicpdrysi    ",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv   "
};

int main() {
	mapping['q'] = 'z';
	mapping['z'] = 'q';
	for (int q = 0; q < 3; ++q)
		for (int i = 0; i < 44; ++i)
			mapping[into[q][i]] = what[q][i];
	ios_base::sync_with_stdio(0);

	cin >> n;
	cin.ignore();
	for (int q = 1; q <= n; ++q) {
		getline(cin, s);
		for (int i = 0; i < s.length(); ++i)
			s[i] = mapping[s[i]];
		cout << "Case #" << q << ": " << s << endl;
	}
}
