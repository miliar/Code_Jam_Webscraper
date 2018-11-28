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

const int Maxn = 10;
const int Move[5][2] = { {0, 0}, {0, -1}, {0, 1}, {-1, 1}, {-1, -1}};
int Map[Maxn + 2][Maxn + 2], Ans;
char str[Maxn + 2];
int n, m;

void input(){
    int i, j;
    scanf("%d%d", &n, &m);
    memset(Map, 0, sizeof(Map));
    for ( i = 1; i <= n; ++ i ){
        scanf("%s", str);
        for ( j = 0; j < m; ++ j){
            Map[i][j + 1] = (str[j] == 'x');
        }
    }
}

inline void fill(int x, int y, int f){
    int i;
    for ( i = 0; i < 5; ++ i ){
        Map[x + Move[i][0]][y + Move[i][1]] += f;
    }
}

void solve(int x, int y, int Maxv){
    if ( y == 0 ){
        -- x;
        y = m;
    }
    while ( Map[x][y] && x){
        -- y;
        if ( y == 0 ){
            -- x;
            y = m;
        }
    }
    if ( !x ){
        Ans = Maxv > Ans ? Maxv : Ans;
        return;
    }
    if ( Map[x][y] == 0 ){
        fill(x, y, 1);
        solve(x, y - 1, Maxv + 1);
        fill(x, y, -1);
    }
    solve(x, y - 1, Maxv);
}

int main(){
    int t, ti;
    scanf("%d", &t);
    for ( ti = 1; ti <= t; ++ ti ){
        input();
        Ans = 0;
        solve(n, m, 0);
        printf("Case #%d: %d\n", ti, Ans);
    }
    return 0;
}
        

