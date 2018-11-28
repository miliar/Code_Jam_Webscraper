#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
using namespace std;
#define de(a) cout << #a << ':' << (a) << endl
#define For(i,x) for (int i=0; i<(int)(x); i++)

int main() {
    const char* src[] = {
        "ejp mysljylc kd kxveddknmc re jsicpdrysi",
        "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
        "de kr kd eoya kw aej tysr re ujdr lkgc jv",
    };

    const char* dst[] = {
        "our language is impossible to understand",
        "there are twenty six factorial possibilities",
        "so it is okay if you want to just give up",
    };

    map<char, char> m;
    for (int i = 0; i < 3; i++) {
        const int n = strlen(src[i]);
        for (int j = 0; j < n; j++) {
            m[src[i][j]] = dst[i][j];
        }
    }

    m['q'] = 'z';
    m['z'] = 'q';

    char s[1000];
    gets(s);
    int ncases = atoi(s);
    For(cc, ncases) {
        gets(s);
        printf("Case #%d: ", cc+1);
        int n = strlen(s);
        For(i, n) putchar(m[s[i]]);
        putchar('\n');
    }
}




