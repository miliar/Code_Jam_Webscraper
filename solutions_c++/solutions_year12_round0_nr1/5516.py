#include <string>
#include <map>
#include <iostream>
#include <set>
#include <cstdio>
using namespace std;

map<char, char> decoded;

void upd(const string& a, const string&b) {
	for (size_t i = 0; i < a.size(); ++i)
		decoded[a[i]] = b[i];
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	upd("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
	upd("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
	upd("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");
	upd("qz", "zq");
//	for (char c = 'a'; c <= 'z'; ++c)
//		cerr << c << " -> " << decoded[c] << endl;

	int t;
	cin >> t;
	string curr;
	getline(cin, curr);

	for (int tst = 0; tst < t; ++tst) {
		getline(cin, curr);
		//		cerr << curr << endl;
		cout << "Case #" << (tst + 1) << ": ";
		for (size_t i = 0; i < curr.size(); ++i)
			if (decoded.find(curr[i]) != decoded.end())
				cout << decoded[curr[i]];
			else
				cerr << "!!!" << curr << endl;
		cout << endl;
	}
	return 0;
}
