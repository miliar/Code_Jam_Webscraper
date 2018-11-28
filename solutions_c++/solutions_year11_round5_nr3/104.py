#include <stdio.h>
#include <string.h>
char c[5][5];
int d[4][4];
int main(){
    int T, ri = 1, n, m, i, j, k, t, x, y, s, ans;
  //  freopen("C-small-attempt0", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        ans = 0;
        scanf("%d%d", &n, &m);
        for (i = 0; i < n; i++){
            scanf("%s", c[i]);
        }
        for (k = 0; k < (1<<(n*m)); k++){
            memset(d, 0, sizeof(d));
            s = 0;
            for (i = 0; i < n; i++){
                for (j = 0; j < m; j++){
                    t = i * m + j;
                    if (k & (1<<t)){
                        if (c[i][j] == '-'){
                            x = i;
                            y = (j - 1 + m) % m;
                        }
                        else if (c[i][j] == '|'){
                            x = (i - 1 + n) % n;
                            y = j;
                        }
                        else if (c[i][j] == '\\'){
                            x = (i - 1 + n) % n;
                            y = (j - 1 + m) % m;
                        }
                        else{
                            x = (i - 1 + n) % n;
                            y = (j + 1) % m;
                        }
                    }
                    else{
                        if (c[i][j] == '-'){
                            x = i;
                            y = (j + 1) % m;
                        }
                        else if (c[i][j] == '|'){
                            x = (i + 1) % n;
                            y = j;
                        }
                        else if (c[i][j] == '\\'){
                            x = (i + 1) % n;
                            y = (j + 1) % m;
                        }
                        else{
                            x = (i + 1) % n;
                            y = (j - 1 + m) % m;
                        }
                    }
                    if (x >= n || y >= m || x < 0 || y < 0) while(1);
                    d[x][y]++;
                    if (d[x][y] > 1){
                        s = 1;
                    }
                }
            }
            if (!s){
                ans++;
            }
        }
        printf("Case #%d: %d\n", ri++, ans % 1000003);
    }
    return 0;
}
