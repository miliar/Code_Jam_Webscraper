#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
using namespace std;

string str;
char map[32];

inline void read() {
	getline(cin, str);
}

inline void get() {
	string input  = "zqejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string output = "qzour language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	for (int i=0; i < 30; ++i) map[i] = '-';
	for (int i=0; i < input.size(); ++i) if (input[i] != ' ') {
		if (map[input[i] - 'a'] == '-')
			map[input[i] - 'a'] = output[i];
	}
}

inline void solve() {
	for (int i=0; i < str.size(); ++i) if (str[i] != ' ') {
		str[i] = map[str[i]-'a'];
	}
}

int main() {
	get();

	int brt, testNo = 0;
	cin >> brt; getc(stdin);
	while (brt --) {
		read();
		solve();
		cout << "Case #" << ++testNo << ": " << str << endl;
	}
	return 0;
}
