#include <cstdio>
#include <cstring>
#include <algorithm>
#include <sstream>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <stack>
#include <queue>
#define sys system("pause")
using namespace std;
const double eps = 1e-10;
struct NODE {
    int b, e, w;
    void init() {
        scanf("%d%d%d", &b, &e, &w);
    }
    bool operator < (const NODE &a) const {
        return b < a.b;
    }
} node[3010];

struct ITEM {
    int b, e, w;
    bool operator < (const ITEM &a) const {
        return w < a.w;
    }
} tmp;

int main() {
  //  freopen("a.in", "r", stdin);
  //  freopen("a.txt", "w", stdout);
    int T, cas = 1;
    scanf("%d", &T);
    while (T--) {
        int X, S, R, t, N;
        scanf("%d%d%d%d%d", &X, &S, &R, &t, &N);
        multiset<ITEM> st;
        for (int i = 0; i < N; ++i) {
            node[i].init();  
        }
        sort(node, node + N);
        int now = 0;
        for (int i = 0; i < N; ++i) {
            if (node[i].b != now) {
                tmp.b = now, tmp.e = node[i].b, tmp.w = 0;
                st.insert(tmp);
                now = tmp.e;
                --i;
            } else {
                tmp.b = node[i].b, tmp.e = node[i].e, tmp.w = node[i].w;
                st.insert(tmp);
                now = tmp.e;
            }
       //     printf("!!%d %d %d\n", tmp.b, tmp.e, tmp.w);
        }
        if (now != X) {
            tmp.b = now, tmp.e = X, tmp.w = 0;
            st.insert(tmp);
       //     printf("!!%d %d %d\n", tmp.b, tmp.e, tmp.w);
        }
        double tot = 0;
        double ans = 0;
        bool flag = 0;
        for (set<ITEM>::iterator it = st.begin(); it != st.end(); ++it) {
            tmp = *it;
       //     printf("%d %d %d\n", tmp.b, tmp.e, tmp.w);
            if (flag) {
                ans += 1.0*(tmp.e - tmp.b)/(tmp.w+S);
            } else {
                double tim = 1.0*(tmp.e - tmp.b)/(tmp.w+R);
                if (tim + tot + eps > t) {
                    ans += (1.0*t-tot);
                    ans += 1.0*(tmp.e - tmp.b - (tmp.w+R)*(1.0*t-tot))/(tmp.w+S);
                    flag = true;
                } else {
                    ans += tim;
                    tot += tim;
                }
            }
        //    cout << ans <<  "    " << tot << endl;
       //     cout << "flag is " << flag << endl;
        }
        printf("Case #%d: %.10lf\n", cas++, ans);
    }
   // sys;
    return 0;
}
