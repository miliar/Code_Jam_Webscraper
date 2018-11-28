#include <iostream>
using namespace std;

string 
s1 = "qaoz ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv",
s2 = "zyeq our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

char eq[256];

#define FOR(i, x) for(int i = 0; i < (x); i++)
#define SZ(x) (int)x.size()

int main() {
	FOR(i, 256)
		eq[i] = '$';

	eq[' '] = ' ';
	FOR(i, SZ(s1)) {
		eq[s1[i]] = s2[i];
	}

	ios::sync_with_stdio(false);
	int TC;
	cin >> TC;
	string tmp;
	getline(cin, tmp);
	FOR(T, TC) {
		cout << "Case #" << T + 1 << ": ";
		string p;
		getline(cin, p);
		FOR(i, SZ(p))
			cout << eq[p[i]];
		cout << endl;
	}
	return 0;
}
