#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <math.h>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
using namespace std;

int n, n2, d[100][100];

void input(){
    int i, j;
    scanf("%d", &n);
    n2 = (n << 1) - 1;
    for (i = 1; i <= n2; ++ i){
        for (j = 1; j <= n2; ++ j){
            d[i][j] = -1;
        }
    }

    for (i = 1; i <= n; ++ i){
        for (j = 1; j <= i; ++ j){
            scanf("%d", &d[i][2 * j + n - i - 1]);
        }
    }
    for (i = n - 1; i >= 1; -- i){
        for (j = 1; j <= i; ++ j){
            scanf("%d", &d[n2 - i + 1][2 * j + n - i - 1]);
        }
    }
/*    putchar(10);
    for (i = 1; i <= n2; ++ i){
        for (j = 1; j <= n2; ++ j){
            if (d[i][j]<0){
                putchar(32);
            }
            else{
                printf("%d", d[i][j]);
            }
        }
        putchar(10);
    }
*/
}

bool judgex(int m){
    int i, j, x;
    for (i = 1; i <= n2; ++ i){
        for (j = 1; j <= n2; ++ j){
            if (d[i][j] == -1) continue;
            x = m * 2 - i;
            if (x > n2 || x <= 0) continue;
            if (d[x][j] == -1) continue;
            if (d[i][j] != d[x][j]) return false;
        }
    }
    return true;
}

bool judgey(int m){
    int i, j, y;
    for (i = 1; i <= n2; ++ i){
        for (j = 1; j <= n2; ++ j){
            if (d[i][j] == -1) continue;
            y = m * 2 - j;
            if (y > n2 || y <= 0) continue;
            if (d[i][y] == -1) continue;
            if (d[i][j] != d[i][y]) return false;
        }
    }
    return true;
}

int solve(){
    int i, j, mx, my, m;
    for (i = 0; i <= n; ++ i){
        mx = i;
        if (judgex(n - mx)) break;
        if (judgex(n + mx)) break;
    }
    for (i = 0; i <= n; ++ i){
        my = i;
        if (judgey(n + my)) break;
        if (judgey(n - my)) break;
    }
    m = n;
    m = (m + my) ;
    m = (m + mx) ;
    //printf("## %d %d\n", mx, my);
    //printf("## %d\n", m);
    return m * m - n * n;
}
    

int main(){
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T, ti = 0;
    scanf("%d", &T);
    while (T --){
        input();
        printf("Case #%d: %d\n", ++ ti, solve());
    }
    return 0;
}
