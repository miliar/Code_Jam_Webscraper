#include <stdio.h>
#include <memory.h>
#include <iostream>

using namespace std;

int c[30];
bool dx[30];

void decrypt(const char* a, const char* b) {
	for (int i=0; i<strlen(a); i++) {
		if (a[i] != ' ') { c[ a[i]-'a' ] = b[i]; dx[ b[i]-'a' ] = true; }
	}
}

int main() {
	//
	memset(c, -1, sizeof(c));
    memset(dx, false, sizeof(dx));
	decrypt("y qee", "a zoo");
	decrypt("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
	decrypt("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
	decrypt("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");
    for (int i='a'; i<='z'; i++) if (c[i-'a'] == -1) {
        for (int j='a'; j<='z'; j++) if (!dx[j-'a']) c[i-'a'] = j;
    }
    

	//
	int num_test;
	char s[200];

	scanf("%d\n", &num_test);
	for (int i=1; i<=num_test; i++) {
		gets(s);
		for (int j=0; j<strlen(s); j++) if (s[j] != ' ') s[j] = c[s[j]-'a'];
		printf("Case #%d: %s\n", i, s);
	}

	return 0;
}
