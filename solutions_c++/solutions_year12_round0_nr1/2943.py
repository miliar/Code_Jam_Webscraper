#include <iostream>
#include <string>
#include <cstdio>
using namespace std;

char a[256];

void Init(const string &s1, const string &s2) {
	if (s1.size() != s2.size()) {
		cerr << "error\n";
		return;
	}
	for (size_t i = 0; i < s1.size(); ++i) {
		if (a[s1[i]] == 0) {
			a[s1[i]] = s2[i];
		} else {
			if (a[s1[i]] != s2[i]) {
				cerr << "error\n";
				return;
			}
		}
	}
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	Init("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
	Init("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
	Init("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");
	// just guessing
	a['q'] = 'z';
	a['z'] = 'q';
	
	char buf[1000];
	gets(buf);
	int n = atoi(buf);
	for (int i = 0; i < n; ++i) {
		gets(buf);
		printf("Case #%d: ", i + 1);
		int len = strlen(buf);
		for (int j = 0; j < len; ++j) {
			printf("%c", a[buf[j]]);
		}
		printf("\n");
	}
	return 0;
}