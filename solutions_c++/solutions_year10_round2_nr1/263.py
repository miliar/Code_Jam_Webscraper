#include <iostream>
#include <cstdio>
#include <cstring>
#include <set>
using namespace std;

set<string> table;
char str[1024];

void makepath(char * s) {
	int n = strlen(s);
	s[n] = '/';
	for (int i = n; i > 0; --i) {
		if (s[i] == '/') {
			s[i] = 0;
			if (table.find(s) != table.end()) return;
			table.insert(s);
		}
	}
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, tc = 0;
	scanf("%d", &T);
	while (T -- > 0) {
		int n, m;
		table.clear();
		scanf("%d%d\n",&n,&m);
		while (n -- > 0) {
			scanf("%s\n", str);
			makepath(str);
		}
		int t = table.size();
		while (m -- > 0) {
			scanf("%s\n", str);
			makepath(str);
		}
		printf("Case #%d: %d\n",++tc, table.size() - t);
	}

	return 0;
}
