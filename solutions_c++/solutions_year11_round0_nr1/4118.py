#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cstdlib>
using namespace std;

struct node {
    bool ob; // o = 0, b = 1
    int dist;
};

node f[110];

int main()
{
    freopen("l.in", "r", stdin);
    freopen("l.out", "w", stdout);

    int i, n, t, d;
    char c;
    scanf("%d", &t);
    for (int cas = 1; cas <= t; cas++) {
        int preo = 1, preb = 1, ans = 0;
        scanf("%d", &n);
        for (i = 0; i < n; i++) {
            getchar();
            scanf("%c", &c);
            if (c == 'O') f[i].ob = 0;
            else f[i].ob = 1;
            scanf("%d", &d);
            if (f[i].ob) {
                f[i].dist = abs(d - preb) + 1;
                preb = d;
            } else {
                f[i].dist = abs(d - preo) + 1;
                preo = d;
            }
        }
        preo = preb = 0;
        bool pre;
        if (f[0].ob) pre = 1;
        else pre = 0;
        for (i = 0; i < n; i++) {
            if (f[i].ob == pre) {
                ans += f[i].dist;
                if (pre) preb = ans;
                else preo = ans;
            } else if (f[i].ob) {
                ans = ans + 1 > preb + f[i].dist ? ans + 1 : preb + f[i].dist;
                preb = ans;
                pre = 1;
            } else {
                ans = ans + 1 > preo + f[i].dist ? ans + 1 : preo + f[i].dist;
                preo = ans;
                pre = 0;
            }
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
