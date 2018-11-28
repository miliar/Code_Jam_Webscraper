#include <cstdio>
#include <cmath>
#include <iostream>
#include <cstring>
using namespace std;
struct ORDER {
    char col[20];
    int pos;
    void init() {
        scanf("%s%d", col, &pos);
    }  
} order[110];

inline int abs(int x) {
    return x < 0 ? -x : x;
}
int main() {
 //   freopen("A-large.in", "r", stdin);
//    freopen("a.out", "w", stdout);
    int T, n, cas = 1;
    scanf("%d", &T);
    while (T--) {
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            order[i].init();
        }
        int pos1 = 1, pos2 = 1, ans = 0, d1 = 0, d2 = 0, d = 0;
        for (int i = 0; i < n; ++i) {
            if (order[i].col[0] == 'B') {
                d = abs(order[i].pos - pos1) - d1;
                d1 = 0;
                if (d > 0) {
                    ans += (d + 1);
                    d2 += (d + 1);
                } else {
                    ans++;
                    d2++;
                }
                pos1 = order[i].pos;
            } else {
                d = abs(order[i].pos - pos2) - d2;
                d2 = 0;
                if (d > 0) {
                    ans += (d + 1);
                    d1 += (d + 1);
                } else {
                    ans++;
                    d1++;
                }
                pos2 = order[i].pos;
            }
        }
        printf("Case #%d: %d\n", cas++, ans);
    }
   // system("pause");
    return 0;
}
