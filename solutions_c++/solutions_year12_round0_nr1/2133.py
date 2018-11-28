/*
 * by purple
 * at 12-04-14 11:15:35
 */

#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <map>

using namespace std;

#define sz(x) ((int)((x).size()))
#define out(x) printf(#x" %d\n", x)
#define rep(i,n) for(int i=0;i<(n);++i)
#define repf(i,a,b) for(int i=(a);i<=(b);++i)

const char *ori[3] = {
    "our language is impossible to understand",
    "there are twenty six factorial possibilities",
    "so it is okay if you want to just give up"
};

const char *dec[3] = {
    "ejp mysljylc kd kxveddknmc re jsicpdrysi",
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
    "de kr kd eoya kw aej tysr re ujdr lkgc jv"
};

map<char, char> mp;
char s[128];

int main() {
    freopen ("A.in", "r", stdin);
    freopen ("A.out", "w", stdout);
    
    rep (i, 3) {
        for (int j = 0; ori[i][j]; ++j) {
            mp[dec[i][j]] = ori[i][j];
        }
    }
    mp['z'] = 'q';
    mp['q'] = 'z';
    
    int t, Case = 1;
    for (scanf ("%d\n", &t); t; --t) {
        gets(s);
        printf ("Case #%d: ", Case++);
        for (int i = 0; s[i]; ++i) {
            putchar (mp[s[i]]);
        }
        puts ("");
    }
    return 0;
}

