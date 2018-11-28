#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<cassert>
#include<cstdio>
#include<cstring>
#include<ctime>

#define DEBUGLEVEL
#ifdef DEBUGLEVEL
#define printf_debug(fmt, args...) fprintf(stderr, fmt, ##args)
#else
#define printf_debug(fmt, args...)
#endif

typedef long long llong;

using namespace std;

char d[26];

int main() {
    /* a */d[0] = 'y';
    /* b */d[1] = 'h';
    /* c */d[2] = 'e';
    /* d */d[3] = 's';
    /* e */d[4] = 'o';
    /* f */d[5] = 'c';
    /* g */d[6] = 'v';
    /* h */d[7] = 'x';
    /* i */d[8] = 'd';
    /* j */d[9] = 'u';
    /* k */d[10] = 'i';
    /* l */d[11] = 'g';
    /* m */d[12] = 'l';
    /* n */d[13] = 'b';
    /* o */d[14] = 'k';
    /* p */d[15] = 'r';
    /* q */d[16] = 'z';
    /* r */d[17] = 't';
    /* s */d[18] = 'n';
    /* t */d[19] = 'w';
    /* u */d[20] = 'j';
    /* v */d[21] = 'p';
    /* w */d[22] = 'f';
    /* x */d[23] = 'm';
    /* y */d[24] = 'a';
    /* z */d[25] = 'q';
    freopen("solve.in", "r", stdin);
    freopen("solve.out", "w", stdout);
    int T;
    scanf("%d\n", &T);
    for(int t = 0; t < T; t++) {
        string s, news;
        getline(cin, s);
        news = s;
        for(int i = 0; i < news.size(); i++) {
            if('a' <= news[i] && news[i] <= 'z') {
                news[i] = d[news[i] - 'a'];
            }
        }
        cout << "Case #" << t + 1 << ": " << news << endl;
    }
    return 0;
}
