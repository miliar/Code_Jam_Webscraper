#include <cstdio>
#include <cstdlib>
#include <cstring>

int t, ans, sum;
char ss[5][5];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &t);
    for (int i = 1; i <= t; i ++ ) {
        sum = 0;
        for (int j = 0; j < 4; j ++ ) {
            scanf("%s", ss[j]);
            for (int k = 0; k < 4; k ++ )
                if (ss[j][k] == '.') sum ++ ;
        }
        ans = -1;
        int o, x, ts;
        for (int j = 0; j < 4; j ++ ) {
            o = x = ts = 0;
            for (int k = 0; k < 4; k ++ )
                if (ss[k][j] == 'O') o ++ ;
                else if (ss[k][j] == 'X') x ++ ;
                else if (ss[k][j] == 'T') ts ++ ;
            if (o + ts == 4) {
                ans = 1;
                break;
            }
            if (x + ts == 4) {
                ans = 2;
                break;
            }
            o = x = ts = 0;
            for (int k = 0; k < 4; k ++ )
                if (ss[j][k] == 'O') o ++ ;
                else if (ss[j][k] == 'X') x ++ ;
                else if (ss[j][k] == 'T') ts ++ ;
            if (o + ts == 4) {
                ans = 1;
                break;
            }
            if (x + ts == 4) {
                ans = 2;
                break;
            }
        }
        if (ans == -1) {
            o = x = ts = 0;
            for (int j = 0; j < 4; j ++ )
                if (ss[j][3 - j] == 'O') o ++ ;
                else if (ss[j][3 - j] == 'X') x ++ ;
                else if (ss[j][3 - j] == 'T') ts ++ ;
            if (o + ts == 4) ans = 1;
            if (x + ts == 4) ans = 2;
             o = x = ts = 0;
            for (int j = 0; j < 4; j ++ )
                if (ss[j][j] == 'O') o ++ ;
                else if (ss[j][j] == 'X') x ++ ;
                else if (ss[j][j] == 'T') ts ++ ;
            if (o + ts == 4) ans = 1;
            if (x + ts == 4) ans = 2;
        }
        if (ans == -1) {
            if (sum != 0) ans = 4;
            else ans = 3;
        }
        printf("Case #%d: ", i);
        if (ans == 2) printf("X won\n");
        else if (ans == 1) printf("O won\n");
        else if (ans == 3) printf("Draw\n");
        else printf("Game has not completed\n");
    }
    return 0;
}
