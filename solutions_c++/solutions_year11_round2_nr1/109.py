#include <stdio.h>
char c[110][110];
double w[110], ow[110], oow[110];
int wc[110], lc[110];
double f(int x, int y){
    int dx = 0, dy = 0;
    if (c[x][y] == '1'){
        dx = dy = -1;
    }
    if (c[x][y] == '0'){
        dy = -1;
    }
    return (wc[x] + dx) * 1.0 / (lc[x] + dy);
}
int main(){
    int T, ri = 1, n, i, j, x, y;
    double s;
    freopen("A-large (1).in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        scanf("%d", &n);
        for (i = 0; i < n; i++){
            scanf("%s", c[i]);
            x = y = 0;
            for (j = 0; j < n; j++){
                if (c[i][j] == '1'){
                    x++;
                    y++;
                }
                else if (c[i][j] == '0'){
                    y++;
                }
            }
            wc[i] = x;
            lc[i] = y;
            w[i] = x * 1.0 / y;
        }
        for (i = 0; i < n; i++){
            s = x = 0;
            for (j = 0; j < n; j++){
                if (c[i][j] != '.'){
                    s += f(j, i);
                    x++;
                }
            }
            ow[i] = s / x;
        }
        for (i = 0; i < n; i++){
            s = x = 0;
            for (j = 0; j < n; j++){
                if (c[i][j] != '.'){
                    s += ow[j];
                    x++;
                }
            }
            oow[i] = s / x;
        }
        printf("Case #%d:\n", ri++);
        for (i = 0; i < n; i++){
            printf("%.10f\n", 0.25 * w[i] + 0.50 * ow[i] + 0.25 * oow[i]);
        }
    }
    return 0;
}
