#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
const int maxn = 100000 + 5;
int t, n, m;

char line[maxn], to[maxn];
int main() {
	char s[] = " ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv ";
	char t[] = " our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up ";
	int hash[300];
	for (int i = 0, len = strlen(s); i < len; ++i)
		hash[s[i]] = t[i];
	hash['q'] = 'z';
	hash['z'] = 'q';
//	for (int i = 'a'; i <= 'z'; ++i)
//		printf("%c -> %c\n", hash[i], i);
	int T;
	scanf("%d", &T);
	getchar();
	for (int index = 1; index <= T; ++index) {
		gets(line);
		for (int i = 0, len = strlen(line); i <= len; ++i)
			if ('a' <= line[i] && line[i] <= 'z') {
				to[i] = hash[line[i]];
			} else {
				to[i] = line[i];
			}
		printf("Case #%d: %s\n", index, to);
	}
	return 0;
}
