#include <cstdio>

char mappings[128];

char buf[200],out[200];

const char * cipher =
"ejp mysljylc kd kxveddknmc re jsicpdrysi"
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
"de kr kd eoya kw aej tysr re ujdr lkgc jv"
"qz";

const char * plain =
"our language is impossible to understand"
"there are twenty six factorial possibilities"
"so it is okay if you want to just give up"
"zq";

int main() {
    for (int c = 0; c <= 127; ++c)
        mappings[c] = c;

    // find the mappings
    for (int i = 0; cipher[i] != '\0'; ++i)
        mappings[cipher[i]] = plain[i];

    int T;
    scanf("%d", &T); getchar();
    for (int t = 0; t < T; ++t) {
        gets(buf);
        int i = 0;
        for (; buf[i] != '\0'; ++i)
            out[i] = mappings[buf[i]];
        out[i] = '\0';
        printf("Case #%d: %s\n", t+1, out);
    }

    return 0;
}

