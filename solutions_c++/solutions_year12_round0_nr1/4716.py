#include <vector>
#include <cstdio>
#include <iostream>
#include <map>
using namespace std;
char s[10000];
int main() {
    freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	string a[3][2] = {
		"ejp mysljylc kd kxveddknmc re jsicpdrysi",
		"our language is impossible to understand",
		"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
		"there are twenty six factorial possibilities",
		"de kr kd eoya kw aej tysr re ujdr lkgc jv",
		"so it is okay if you want to just give up",
	};
	map<char, char> mp;
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < a[i][0].size(); j++) {
			mp[a[i][0][j]] = a[i][1][j];
        }
    }
	mp['z'] = 'q';
	mp['q'] = 'z';
	int T;
	scanf("%d", &T);
	getchar();
	for (int cas = 1; cas <= T; cas++) {
		gets(s);
		for (int i = 0; s[i]; i++) {
			s[i] = mp[s[i]];
        }
		printf("Case #%d: ", cas);
		puts(s);
	}
}

