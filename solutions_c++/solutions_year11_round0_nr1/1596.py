#include <cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
using namespace std;

struct {
    int v, i;
} o[120], b[120];
int t, tt, k;

int main() {
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
    scanf("%d", &t);
    for (tt = 1; tt <= t; ++tt) {
        scanf("%d", &k);
        char ch[5];
        int m = 0, n = 0, time = 0;
        int q = 1, p = 1;
        for (int i = 1; i <= k; ++i) {
            scanf("%s", ch);
            if (ch[0] == 'O') {
                o[m].i = i;
                scanf("%d", &o[m++].v);
            } else if (ch[0] == 'B') {
                b[n].i = i;
                scanf("%d", &b[n++].v);
            }
        }
        o[m].i = b[n].i = 99999;
        o[m].v = b[n].v = 99999;
        for (int i = 0, j = 0;;) {
            if (o[i].i < b[j].i) {
                time += abs(o[i].v - p) + 1;
                if (q < b[j].v) {
                    if (abs(o[i].v - p) + 1 + q > b[j].v) q = b[j].v;
                    else q += abs(o[i].v - p) + 1;
                } else {
                    if (q - (abs(o[i].v - p) + 1) < b[j].v) q = b[j].v;
                    else q -= abs(o[i].v - p) + 1;
                }
                p = o[i].v;
                i++;
            } else {
                time += abs(b[j].v - q) + 1;
                if (p < o[i].v) {
                    if (abs(b[j].v - q) + 1 + p > o[i].v) p = o[i].v;
                    else p += abs(b[j].v - q) + 1;
                }
                else{
                    if(p-(abs(b[j].v - q) + 1)<o[i].v) p=o[i].v;
                    else p-=abs(b[j].v - q) + 1;
                }
                q = b[j].v;
                j++;
            }
            if (i >= m && j >= n) break;
        }
        printf("Case #%d: %d\n", tt, time);
    }
    return 0;
}

