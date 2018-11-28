#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const int MAXN = 500;

int g[MAXN+10][MAXN+10];

inline bool is_ok(int cr, int cc, int sz) {
    int tx = 0, ty = 0;
    int sx = cr - sz/2, sy = cc - sz/2, x, y;
    for (int r = 0; r < sz; r++) {
        x = sx + r;
        for (int c = 0; c < sz; c++) {
            if ((c == 0 && r == 0) || (c == 0 && r == sz-1) || (c == sz-1 && r == 0) || (c == sz-1 && r == sz-1)) continue;
            y = sy + c;
            tx += g[x][y] * ((x-cr)*2);
            ty += g[x][y] * ((y-cc)*2);
        }
    }
    //cout << cr << "," << cc << " : " << sz << " == " << tx << "," << ty << endl;///
    return (tx == 0 && ty == 0);
}

inline bool is_ok2(int cr, int cc, int sz) {
    int tx = 0, ty = 0;
    int sx = cr - sz/2+1, sy = cc - sz/2+1, x, y;
    for (int r = 0; r < sz; r++) {
        x = sx + r;
        for (int c = 0; c < sz; c++) {
            if ((c == 0 && r == 0) || (c == 0 && r == sz-1) || (c == sz-1 && r == 0) || (c == sz-1 && r == sz-1)) continue;
            y = sy + c;
            tx += g[x][y] * ((x-cr)*2-1);
            ty += g[x][y] * ((y-cc)*2-1);
        }
    }
    //cout << cr << "," << cc << " : " << sz << " == " << tx << "," << ty << endl;///
    return (tx == 0 && ty == 0);
}

int main() {
    freopen("D:\\TopCoder\\gcj2011\\R2\\B.in", "r", stdin);
    freopen("D:\\TopCoder\\gcj2011\\R2\\B.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ca++) {
        int R, C, D;
        scanf("%d %d %d", &R, &C, &D);
        int n = min(R, C);        
        char s[C+10];
        for (int r = 1; r <= R; r++) {
            scanf("%s", s);
            for (int c = 0; c < C; c++) {
                g[r][c+1] = s[c]-'0' + D;
            }
        }
        
        int ans = 0;
        for (int i = 3; i <= n; i += 2) {
            for (int r = i/2+1; r <= R-i/2; r++) {
                for (int c = i/2+1; c <= C-i/2; c++) {
                    if (is_ok(r, c, i)) {
                        //cout << r << "," << c << " : " << i << endl;//
                        ans = i;
                        goto LABEL;
                    }
                }
            }
LABEL:     
            ; 
        }
        
        for (int i = max(ans, 3)+1; i <= n; i += 2) {
            for (int r = i/2; r <= R-i/2; r++) {
                for (int c = i/2; c <= C-i/2; c++) {
                    if (is_ok2(r, c, i)) {
                        //cout << r << "," << c << " : " << i << endl;//
                        ans = i;
                        goto LABEL2;
                    }
                }
            }
LABEL2:     
            ; 
        }
        
        printf("Case #%d: ", ca);
        if (ans == 0) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        printf("%d\n", ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
