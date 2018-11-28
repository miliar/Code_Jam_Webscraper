#include <iostream>
#include <cassert>
#include <string>
#include <cstdio>

using namespace std;

string from =
		"ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvqz";
string to =
		"our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upzq";
char r[256];

void solve(int test) {
	string ans;
	getline(cin, ans);
	for (int i = 0; i < (int) ans.size(); ++i)
		ans[i] = r[ans[i]];
	cout << "Case #" << test << ": " << ans << endl;
}

void pre() {
	for (int i = 0; i < (int) from.size(); ++i)
		r[from[i]] = to[i];
}

int main() {
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	pre();
	int n;
	cin >> n;
	string tmp;
	getline(cin, tmp);
	for (int i = 1; i <= n; ++i) {
		solve(i);
	}
	return 0;
}
