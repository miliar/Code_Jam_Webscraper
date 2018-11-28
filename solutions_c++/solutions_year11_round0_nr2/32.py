#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <numeric>
#include <algorithm>
using namespace std;
#ifdef DEBUGRUN
#define LOG(a) (cerr<<__LINE__<<": "#a" = "<<(a)<<endl)
#define DBG(...) (__VA_ARGS__)
#else
#define LOG(...) ((void)0)
#define DBG(...) ((void)0)
#endif
#define rep(i, n) for(int i=0; i<(int)(n); i++)
#define mp make_pair
#define foreach(it, c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++)
typedef long long Int;
#define INF MY_INFINITY

int C, D, N;
char g[128][128];
bool op[128][128];
char p[16], s[256];

int main() {
    int T;
    scanf("%d", &T);
    rep(q, T) {
        memset(g, 0, sizeof(g));
        memset(op, 0, sizeof(op));
        scanf("%d", &C);
        rep(i, C) {
            scanf("%s", p);
            g[p[0]][p[1]]=g[p[1]][p[0]]=p[2];
        }
        scanf("%d", &D);
        rep(i, D) {
            scanf("%s", p);
            op[p[0]][p[1]]=op[p[1]][p[0]]=true;
        }
        scanf("%d %s", &N, s);
        vector<char> r;
        rep(i, N) {
            if(!r.empty() && g[r.back()][s[i]]>0) {
                r.back() = g[r.back()][s[i]];
            }
            else {
                bool ok = true;
                rep(j, r.size()) if(op[r[j]][s[i]]) ok=false;
                if(ok) r.push_back(s[i]);
                else r.clear();
            }
        }
        printf("Case #%d: [", q+1);
        rep(i, r.size()) {
            if(i>0) printf(", ");
            printf("%c", r[i]);
        }
        printf("]\n");
    }
    return 0;
}


