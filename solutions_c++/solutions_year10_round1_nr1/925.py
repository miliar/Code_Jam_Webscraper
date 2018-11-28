#include <stdio.h>
char c[60][60];
int a[60][60];
int dx[4] = {0, 1, 1, 1};
int dy[4] = {1, 0, 1, -1};
int main(){
    int rep, ri, n, i, j, m, k, r, b, x, y;
    freopen("aaa.txt", "r", stdin);
    freopen("bbb.txt", "w", stdout);
    scanf("%d", &rep);
    for (ri = 1; ri <= rep; ri++){
        scanf("%d%d", &n, &m);
        for (i = 0; i < n; i++){
            for (j = 0; j < n; j++){
                a[i][j] = 0;
            }
        }
        for (i = 0; i < n; i++){
            scanf("%s", c[i]);
        }
        for (i = 0; i < n; i++){
            k = n - 1;
            for (j = n - 1; j >= 0; j--){
                if (c[n - 1 - i][j] == 'R'){
                    a[k--][i] = 1;
                }
                else if (c[n - 1 - i][j] == 'B'){
                    a[k--][i] = 2;
                }
            }
        }
        r = b = 0;
        for (i = 0; i < n; i++){
            for (j = 0; j < 4; j++){
                x = 0;
                y = i;
                k = 1;
                while (x + dx[j] >= 0 && x + dx[j] < n && y + dy[j] >= 0 && y + dy[j] < n){
                    if (a[x][y] == a[x + dx[j]][y + dy[j]]){
                        k++;
                    }
                    else{
                        if (k >= m && a[x][y]){
                            if (a[x][y] == 1){
                                r = 1;
                            }
                            else{
                                b = 1;
                            }
                        }
                        k = 1;
                    }
                    x += dx[j];
                    y += dy[j];
                }
                if (k >= m && a[x][y]){
                    if (a[x][y] == 1){
                        r = 1;
                    }
                    else{
                        b = 1;
                    }
                }
            }
            for (j = 0; j < 4; j++){
                x = n - 1;
                y = i;
                k = 1;
                while (x + dx[j] >= 0 && x + dx[j] < n && y + dy[j] >= 0 && y + dy[j] < n){
                    if (a[x][y] == a[x + dx[j]][y + dy[j]]){
                        k++;
                    }
                    else{
                        if (k >= m && a[x][y]){
                            if (a[x][y] == 1){
                                r = 1;
                            }
                            else{
                                b = 1;
                            }
                        }
                        k = 1;
                    }
                    x += dx[j];
                    y += dy[j];
                }
                if (k >= m && a[x][y]){
                    if (a[x][y] == 1){
                        r = 1;
                    }
                    else{
                        b = 1;
                    }
                }
            }
            for (j = 0; j < 4; j++){
                x = i;
                y = 0;
                k = 1;
                while (x + dx[j] >= 0 && x + dx[j] < n && y + dy[j] >= 0 && y + dy[j] < n){
                    if (a[x][y] == a[x + dx[j]][y + dy[j]]){
                        k++;
                    }
                    else{
                        if (k >= m && a[x][y]){
                            if (a[x][y] == 1){
                                r = 1;
                            }
                            else{
                                b = 1;
                            }
                        }
                        k = 1;
                    }
                    x += dx[j];
                    y += dy[j];
                }
                if (k >= m && a[x][y]){
                    if (a[x][y] == 1){
                        r = 1;
                    }
                    else{
                        b = 1;
                    }
                }
            }
            for (j = 0; j < 4; j++){
                x = i;
                y = n - 1;
                k = 1;
                while (x + dx[j] >= 0 && x + dx[j] < n && y + dy[j] >= 0 && y + dy[j] < n){
                    if (a[x][y] == a[x + dx[j]][y + dy[j]]){
                        k++;
                    }
                    else{
                        if (k >= m && a[x][y]){
                            if (a[x][y] == 1){
                                r = 1;
                            }
                            else{
                                b = 1;
                            }
                        }
                        k = 1;
                    }
                    x += dx[j];
                    y += dy[j];
                }
                if (k >= m && a[x][y]){
                    if (a[x][y] == 1){
                        r = 1;
                    }
                    else{
                        b = 1;
                    }
                }
            }
        }
        printf("Case #%d: ", ri);
        if (r && b){
            printf("Both\n");
        }
        else if (r){
            printf("Red\n");
        }
        else if (b){
            printf("Blue\n");
        }
        else{
            printf("Neither\n");
        }
    }
    return 0;
}
