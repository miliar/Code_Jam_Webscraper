#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <cstring>
using namespace std;

#define LET(x, a) __typeof(a) x = (a)
#define FOR(x, a, b) for(LET(x, a); x != (b); x++)
#define TR(cnt, it) FOR(it, (cnt).begin(), (cnt).end())
#define ISIN(x, cnt) ((cnt).find(x) != (cnt).end())

char MAP[255][255];

int main () {
    int T, numcase;
    scanf("%d", &T);
    for(numcase=1;numcase<=T; numcase++){
        memset(MAP, -1, sizeof(MAP));
        int C, D;
        map<char, vector<char> > X;
        X.clear();
        scanf("%d", &C);
#ifdef DEBUG
        printf("CASE %d\n", numcase);
        printf("C is %d\n", C);
#endif
        for(int i=0; i<C; i++){
            char s[4];
            scanf("%s", s);
            MAP[s[0]][s[1]] = s[2];
            MAP[s[1]][s[0]] = s[2];
#ifdef DEBUG
            printf("mapping %c%c to %c\n", s[0], s[1], s[2]);
#endif
        }
        scanf("%d", &D);
#ifdef DEBUG
        printf("D is %d\n", D);
#endif
        for(int i=0; i<D; i++){
            char s[3];
            scanf("%s", s);
            X[s[0]].push_back(s[1]);
            X[s[1]].push_back(s[0]);
#ifdef DEBUG
            printf("making opposed %c and %c\n", s[0], s[1]);
#endif
        }
        int len;
        char str[200];
        scanf("%d %s", &len, str);

        vector<char> L;

        for(int i=0; i<len; i++) {
            int n = L.size();
            char aux;
            bool ok = true;
            if (n > 0 && MAP[str[i]][aux = L[n-1]] != -1) {
                L.pop_back();
                L.push_back(MAP[str[i]][aux]);
                continue;
            }
            TR(X[str[i]], it){
                set<char> LS(L.begin(), L.end());
                if (ISIN(*it, LS)) {
                    L.clear();
                    ok = false;
                    break;
                }
            }
            if (ok) L.push_back(str[i]);
        }

        printf("Case #%d: [", numcase);
        for(int i=0; i<L.size(); i++){
            if (i>0) printf(", ");
            printf("%c", L[i]);
        }
        printf("]\n");
    }
    return 0;
}
