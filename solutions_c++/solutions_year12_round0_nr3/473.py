#include <cstdio>
#include <cstring>
#include <string>
#include <set>
using namespace std;

int t, a, b, len;
char sa[10], sb[10], sn[10], sm[10];
set<string> s;

bool gt(char sm[10], char sn[10]) {
    for (int i = 0; i < len; i++) {
        if (sm[i] > sn[i])
            return 1;
        if (sm[i] < sn[i])
            return 0;
    }
    return 0;
}

bool lte(char sm[10], char sb[10]) {
    for (int i = 0; i < len; i++) {
        if (sm[i] < sb[i])
            return 1;
        if (sm[i] > sb[i])
            return 0;
    }
    return 1;
}

int main() {
    scanf("%d ", &t);
    for (int x = 1; x <= t; x++) {
        scanf("%d %d", &a, &b);
        sprintf(sa, "%d", a);
        sprintf(sb, "%d", b);
        int y = 0;
        for (int i = a; i <= b; i++) {
            sprintf(sn, "%d", i);
            strcpy(sm, sn);
            len = strlen(sn);
            s.clear();
            for (int j = 1; j < len; j++) {
                char tmp = sm[0];
                for (int k = 0; k < len-1; k++) {
                    sm[k] = sm[k+1];
                }
                sm[len-1] = tmp;
                
                if (gt(sm, sn) && lte(sm, sb)) {
                    s.insert(sm);
                }
            }
            y += s.size();
        }
        printf("Case #%d: %d\n", x, y);
    }
}
