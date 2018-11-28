#include <cstdio>
int T;
char a[5][5];

bool win(char p) {
    bool ok;
    for (int i=0;i<4;++i) {
        ok = true;
        for (int j=0;j<4;++j) {
            if (!(a[i][j] == p || a[i][j] == 'T')) {
                ok = false;
            }
        }
        if (ok) return true;
        
        ok = true;
        for (int j=0;j<4;++j) {
            if (!(a[j][i] == p || a[j][i] == 'T')) {
                ok = false;
            }
        }
        if (ok) return true;
    }
    ok = true;
    for (int i=0;i<4;++i) {
        if (!(a[i][i] == p || a[i][i] == 'T')) {
            ok = false;
        }
    }
    if (ok) return true;
    
    ok = true;
    for (int i=0;i<4;++i) {
        if (!(a[i][3-i] == p || a[i][3-i] == 'T')) {
            ok = false;
        }
    }
    if (ok) return true;
    
    return false;
}

int main() {
    scanf("%d", &T);
    for (int tc=1;tc<=T;++tc) {
        bool full = true;
        for (int i=0;i<4;++i) {
            scanf("%s", a[i]);
            for (int j=0;j<4;++j) if (a[i][j] == '.') full = false;
        }
        printf("Case #%d: ", tc);
        
        if (win('X')) puts("X won");
        else if (win('O')) puts("O won");
        else if (full) puts("Draw");
        else puts("Game has not completed");
    }
    return 0;
}
