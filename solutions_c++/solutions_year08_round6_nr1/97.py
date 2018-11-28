#include<stdio.h>
#include<string>
using namespace std;
const int inf = 2000000;
const int maxn = 1005;
int left, right, top, bot;
struct CP {
    int x, y;
    CP(int xx = 0, int yy = 0) : x(xx), y(yy) {}
}pnt[maxn];
struct MM {
    int left, right, bot, top;   
}mm[10];
int cnt;
int ll, rr, bb, tt;
int getpos(const CP &p) {
    if (p.x < left) {
        if (p.y > top) {
            return 1;
        } else if (p.y >= bot) {
            return 4;
        } else {
            return 7;
        }
    } else if (p.x <= right) {
        if (p.y > top) {
            return 2;
        } else {
            return 8;
        }
    } else {
        if (p.y > top) {
            return 3;
        } else if (p.y >= bot) {
            return 6;
        } else {
            return 9;
        }
    }
}
void proc() {
    ll = 0, rr = 1000001;
    bb = 0, tt = 1000001;
    
    for (int i = 0; i < cnt; i++) {
        int k = getpos(pnt[i]);
        switch(k) {
            case 1:
                mm[0].right = max(mm[0].right, pnt[i].x);
                mm[0].bot = min(mm[0].bot, pnt[i].y);                
                break;
            case 2:
                tt = min(tt, pnt[i].y);
                break;
            case 3:
                mm[1].left = min(mm[1].left, pnt[i].x);
                mm[1].bot = min(mm[1].bot, pnt[i].y);
                break;
            case 4:
                ll = max(ll, pnt[i].x);
                break;
            case 6:
                rr = min(rr, pnt[i].x);
                break;
            case 7:
                mm[2].right = max(mm[2].right, pnt[i].x);
                mm[2].top = max(mm[2].top, pnt[i].y);
                break;
            case 8:
                bb = max(bb, pnt[i].y);
                break;
            case 9:
                mm[3].left = min(mm[3].left, pnt[i].x);
                mm[3].top = max(mm[3].top, pnt[i].y);
                break;
        }
    }
}
bool inside(int x, int y, MM mm) {
    return x >= mm.left && x <= mm.right && y >= mm.bot && y <= mm.top;
}
bool check(int x, int y) {
    if (x <= ll || x >= rr || y <= bb || y >= tt)
        return 1;
    for (int i = 0; i < 4; i++) {
        if (inside(x, y, mm[i]))
            return 1;
    }
    return 0;
}
int main() {
    //freopen("a.in", "r", stdin);
    //freopen("a.out", "w", stdout);
    
    mm[0].left = 0, mm[0].top = 1000001;
    mm[1].right = 1000001, mm[1].top = 1000001;
    mm[2].left = 0, mm[2].bot = 0;
    mm[3].right = 1000001, mm[3].bot = 0;
    
    int T;
    scanf("%d", &T);
    for (int casen = 1; casen <= T; casen++) {
        mm[0].right = 0, mm[0].bot = 1000001;
        mm[1].left = 1000001, mm[1].bot = 1000001;
        mm[2].right = 0, mm[2].top = 0;
        mm[3].left = 1000001, mm[3].top = 0;
    
        left = bot = inf;
        right = top = -inf;
        cnt = 0;
        
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            int x, y;
            char str[50];
            scanf("%d%d%s", &x, &y, str);
            if (str[0] == 'B') {
                left = min(left, x);
                right = max(right ,x);                
                bot = min(bot, y);
                top = max(top, y);
            } else {
                pnt[cnt++] = CP(x, y);                
                scanf("%s", str);
            }
        }
        
        printf("Case #%d:\n", casen);
        
        int m;        
        if (cnt == n) {
            scanf("%d", &m);
            for (int i = 0; i < m; i++) {
                int x, y;
                scanf("%d%d", &x, &y);
                int ok = 1;
                for (int j = 0; j < cnt; j++) {
                    if (x == pnt[j].x && y == pnt[j].y) {
                        ok = 0;
                        break;
                    }
                }
                if (ok) {
                    printf("UNKNOWN\n");
                } else {
                    printf("NOT BIRD\n");
                }
            }
            continue;
        }
        
        proc();
        
        scanf("%d", &m);
        for (int i = 0; i < m; i++) {
            int x, y;
            scanf("%d%d", &x, &y);
            if (x >= left && x <= right && y >= bot && y <= top) {
                printf("BIRD\n");
            } else if (check(x, y)) {
                printf("NOT BIRD\n");
            } else {
                printf("UNKNOWN\n");
            }
        }
    }
    return 0;
}
