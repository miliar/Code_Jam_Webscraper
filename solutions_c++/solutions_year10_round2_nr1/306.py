#include <stdio.h>
#include <set>
#include <string>
#include <string.h>
#include <algorithm>
using namespace std;

int i, j, k, m, n,t,tt;
set<string> ex;
set<string> need;
set<string>::iterator it;
char s[100000];

int main() {
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++) {
		printf("Case #%d: ", tt);
		ex.clear();
		need.clear();
		scanf("%d%d", &m, &n);
		for (i = 0; i < m; i++) {
			scanf("%s", s);
			ex.insert(s);
		}
		for (i = 0; i < n; i++) {
			scanf("%s", s);
			need.insert(s);
		}
		int res = 0;
		for (it = need.begin(); it != need.end(); ++it) {
			strcpy(s, it->c_str());
			for (i = 1; s[i]; i++) {
				if (s[i] == '/') {
					s[i] = '\0';
					res += ex.insert(s).second;
					s[i] = '/';
				}
			}
			res += ex.insert(s).second;
		}
		printf("%d\n", res);
	}
	return 0;
}
