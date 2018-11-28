#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
using namespace std;
#define SZ(v) ((int)(v).size())
#define REP(i, n) for (int i = 0; i < (n); ++i)
#define REPF(i, a, b) for (int i = (a); i <= (b); ++i)
#define REPD(i, a, b) for (int i = (a); i >= (b); --i)
const int maxint = -1u>>1;

char s1[] = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
char s2[] = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
char s[102];
char mm[27];

int main() {
    freopen("a.out", "w", stdout);
    int n = strlen(s1);
    for (int i = 0; i < 26; ++i) mm[i] = '0';
    for (int i = 0; i < n; ++i) {
        if (s1[i] >= 'a' && s1[i] <= 'z') {
            mm[s1[i] - 'a'] = s2[i];
        }
    }
    mm['q' - 'a'] = 'z';
    mm['z' - 'a'] = 'q';
    int t, ca = 0;
    scanf("%d", &t);
    gets(s);
    while (t--) {
        printf("Case #%d: ", ++ca);
        gets(s);
        n = strlen(s);
        for (int i = 0; i < n; ++i) {
            if (s[i] >= 'a' && s[i] <= 'z') printf("%c", mm[s[i] - 'a']);
            else printf("%c", s[i]);
        }
        printf("\n");
    }
    return 0;
}

