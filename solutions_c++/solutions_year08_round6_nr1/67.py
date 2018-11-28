#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cctype>
#include <vector>

using namespace std;

#define rep(i,n) for(int i=0;i<(n);i++)
#define foru(i,a,b) for(int i=(a);i<=(b);i++)
#define ford(i,a,b) for (int i=(a);i>=(b);i--)

const int maxn = 10000, MAX = 1000000000;

int cas;

int n, m, px[maxn], py[maxn], a, b, chk[maxn], la, lb, ra, rb, ok, ax, ay, bx, by;
char nm[maxn][50];

int check(int a, int b) {
    ax = la; ay = lb; bx = ra; by = rb;
    ax = min(ax, a);
    bx = max(bx, a);
    ay = min(ay, b);
    by = max(by, b);
    
    if (ok == 0) {
        if (la <= a && a <= ra && lb <= b && b <= rb) return 1;
        rep(i, n) if (chk[i] == 1 && a == px[i] && b == py[i]) return 1;
        rep(i, n) if (chk[i] == 0 && a == px[i] && b == py[i]) return 2;
        rep(i, n) if (chk[i] == 0 && ax <= px[i] && px[i] <= bx && ay <= py[i] && py[i] <= by) return 2;
    } else {
           rep(i, n) if (px[i] == a && py[i] == b) return 2;
           return 0;
    }
    return 0;    
}



int main() {
    scanf("%d", &cas);
    rep(tt, cas) {
            scanf("%d", &n);
            la = MAX; ra = 0;
            lb = MAX; rb = 0;
            rep(i, n) {
                   scanf("%d%d", &px[i], &py[i]);
                   scanf(" %s", nm[i]);
                   if (strcmp(nm[i], "BIRD") == 0) chk[i] = 1; else chk[i] = 0;                   
                   gets(nm[i]);
                   if (chk[i] == 1) {
                       la <?= px[i];
                       lb <?= py[i];
                       ra >?= px[i];
                       rb >?= py[i];
                   } else {                         
                   }

            }
            if (la > ra) ok = 1; else ok = 0;
//            printf("%d %d %d %d\n", la, lb, ra, rb);
            scanf("%d", &m);
            printf("Case #%d:\n", tt + 1);
            rep(i, m) {
                   scanf("%d%d", &a, &b);
                   int ans = check(a, b);
                   if (ans == 0) printf("UNKNOWN\n");
                   if (ans == 1) printf("BIRD\n");
                   if (ans == 2) printf("NOT BIRD\n");                   
            }
            
    }
    return 0;
}
