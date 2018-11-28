#include <cstdio>
#include <cstring>

#define MAXN 10

char f[MAXN][MAXN];
char s[MAXN];

int judge(int x, int y, int dx, int dy) {
    int xc, oc, t, i;
    for(xc = oc = t = i = 0; i<4; ++i, x += dx, y += dy) {
        if (f[y][x] == 'T') t++;
        if (f[y][x] == 'X') xc++;
        if (f[y][x] == 'O') oc++;
    }
    if (xc + t == 4) return 1;
    if (oc + t == 4) return 2;
    return 0;
}

int main() {
    int tc;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    scanf("%i", &tc);
    for(int tt=1; tt<=tc; ++tt) {

        int cnt = 0;
        for(int i=0; i<4; ++i) {
            scanf("%s", &f[i][0]);
            for(int j=0; j<4; ++j) if (f[i][j] != '.') cnt++;
        }

        int res = judge(0, 0, 1, 1) | judge(3, 0, -1, 1);
        for(int i=0; i<4; ++i) res = res | judge(i, 0, 0, 1) | judge(0, i, 1, 0);
        
        if (cnt < 16 && !res) res = -1;   

        switch(res) {
            case 1: strcpy(s, "X won"); break;
            case 2: strcpy(s, "O won"); break;
            case 0: strcpy(s, "Draw");  break;
            case -1: strcpy(s, "Game has not completed"); break;
        }      

        printf("Case #%i: %s\n", tt, s);


    }
}