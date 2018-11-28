#include <stdio.h>
#include <cstring>
#include <cmath>

char str1[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi\
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\
de kr kd eoya kw aej tysr re ujdr lkgc jv";

char str2[] = "our language is impossible to understand\
there are twenty six factorial possibilities\
so it is okay if you want to just give up";

char mapping[30];

int main() {
    for (int i=0; i<strlen(str1); i++) {
        mapping[str1[i]-'a'] = str2[i];
    }

	int T;
	scanf("%d\n",&T);

	for (int t=1; t<=T; t++) {
		char s[105];
		scanf("%[^\n]\n",s);

        printf("Case #%d: ", t);
        for (int i=0; i<strlen(s); i++) {
            printf("%c", mapping[s[i]-'a']);
        }
        printf("\n");

	}
}
