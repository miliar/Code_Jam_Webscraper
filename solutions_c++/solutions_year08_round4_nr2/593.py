#include <stdio.h>
#include <string.h>

int n, m, a;

void input() {
    scanf("%d%d%d", &n, &m, &a);
}

void solve() {
    int x1, y1 = 0, x2, y2, x3 = 0, y3;
    
    for(int x1 = 0;x1 <= n;x1 ++) {
        for(int y2 = 0;y2 <= m;y2 ++) {
            for(int x2 = 0;x2 <= n;x2 ++) {
                int ta = a - x1*y2, tb = x2-x1;
                if(tb == 0&&ta == 0) {
                    y3 = 0;
                    printf("%d %d %d %d %d %d\n", x1, y1, x2, y2, x3, y3);
                    return ;
                }
                if(tb == 0) continue;
                if(ta/tb >= 0&&ta/tb <= m&&ta == tb*(ta/tb)) {
                    y3 = ta/tb;
                    printf("%d %d %d %d %d %d\n", x1, y1, x2, y2, x3, y3);
                    return ;
                }
                ta = a + x1*y2, tb = x1-x2;
                if(ta/tb >= 0&&ta/tb <= m&&ta == tb*(ta/tb)) {
                    y3 = ta/tb;
                    printf("%d %d %d %d %d %d\n", x1, y1, x2, y2, x3, y3);
                    return ;
                }
            }
        }
    }
    
    printf("IMPOSSIBLE\n");
}

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int cas = 1;cas <= t;cas ++) {
        input();
        printf("Case #%d: ", cas);
        solve();
    }
    getchar(); getchar();
    return 0;
}
