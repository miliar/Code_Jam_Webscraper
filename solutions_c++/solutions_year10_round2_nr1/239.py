#include <stdio.h>
#include <set>
#include <string>

using namespace std;

set<string> has;

int add(string s) {
	int ret = 0;
	for (int i = 1; i <= s.size(); ++i) if (i == s.size() || s[i] == '/') {
		string p = s.substr(0, i);
		if (has.count(p) == 0) {
			has.insert(p);
			++ret;
		}
	}
	return ret;
}

int go() {
	char s[1000];
	int n, m;
	scanf("%d%d\n", &n, &m);
	has.clear();
	for (int i = 0; i < n; ++i) {
		gets(s);
		add(s);
	}
	int ret = 0;
	for (int i = 0; i < m; ++i) {
		gets(s);
		ret += add(s);
	}
	return ret;
}

int main() {
	freopen("A-large (1).in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i=  0; i < t; ++i)
		printf("Case #%d: %d\n", i+1, go());
}