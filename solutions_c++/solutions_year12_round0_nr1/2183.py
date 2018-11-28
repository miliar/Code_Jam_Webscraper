#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <utility>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <cmath>

using namespace std;

char replacement['z'+1];

void learn() {
	const char *a = "ejp mysljylc kd kxveddknmc re jsicpdrysi	rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	const char *b = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	replacement['y'] = 'a';
	replacement['e'] = 'o';
	replacement['q'] = 'z';
	replacement['z'] = 'q';
	for (int i=0; a[i]; ++i) {
		replacement[(int)a[i]] = b[i];
	}
}

int main(void) {
	learn();
	int t;
	scanf("%d\n", &t);
	char buffer[200];
	for (int i=1; i<=t; ++i) {
		fgets(buffer, 200, stdin);
		for (int j=0; buffer[j]; ++j) {
			buffer[j] = replacement[(int)buffer[j]];
		}
		printf("Case #%d: %s\n", i, buffer);
	}
	return 0;
}
