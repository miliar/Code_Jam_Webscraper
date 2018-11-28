#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <map>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
using namespace std;

char s[] = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
char d[] = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
char m[256];
char buf[1000];
    
int main() {
    freopen("A-small-attempt5.in", "r", stdin);
    freopen("A-small-attempt5.out", "w", stdout);
    for (int i = 0; s[i]; i++) if (s[i] >= 'a' && s[i] <= 'z') 
        m[d[i]] = s[i]; 
    m['z'] = 'q';
    m['q'] = 'z';
    int T;
    scanf("%d", &T);
    getchar();
    for (int k = 1; k <= T; k++) {
        gets(buf);
        for (int i = 0; buf[i]; i++) if (buf[i] >= 'a' && buf[i] <= 'z') 
            buf[i] = m[buf[i]];
        printf("Case #%d: %s\n", k, buf);
    }
//    while(1);
    return 0;
}
