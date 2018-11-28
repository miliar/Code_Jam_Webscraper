#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <functional>
#include <sstream>
#include <cassert>
using namespace std;

#pragma comment(linker, "/STACK:56777216")

typedef long long LL;

#define rep(i, n) for (int i = 0; i < n; i++)
#define sz(v) (int) ((v).size())

const char* inp = "qaoz ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
const char* out = "zyeq our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

int main() {
#ifndef ONLINE_JUDGE
//    freopen("../DefaultProject/1.txt", "rb", stdin);
    freopen("../DefaultProject/A-small-attempt1.in", "rb", stdin);
    freopen("../DefaultProject/A-small-attempt1.out", "wb", stdout);
#endif

    int inpLen = strlen(inp);
    static char m[256];

    rep(i, inpLen) {
        m[inp[i]] = out[i];
    }

    static char s[1000];

    gets(s);
    int T;
    sscanf(s, "%d", &T);
    rep(tc, T) {
        printf("Case #%d: ", tc + 1);

        gets(s);
        int sl = strlen(s);
        rep(i, sl) {
            if (m[s[i]] != 0) {
                putchar(m[s[i]]);
            } else {
                fprintf(stderr, "Unknown symbol %c on test %d\n", s[i], tc + 1);
            }
        }
        putchar('\n');
    }

    return 0;
}
