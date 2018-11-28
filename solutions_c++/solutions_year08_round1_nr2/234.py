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

vector <int> type[11][2];

int n, m;
int num[100], Ans[11], tmp[11], Ansn;
int i, j;

void input(){
    int i, j, T, a, b;
    scanf("%d%d", &n, &m);
    for ( i = 1; i <= n; ++ i ){
        type[i][0].clear();
        type[i][1].clear();
    }
    for ( i = 0; i < m; ++ i ){
        scanf("%d", &T);
        for ( j = 0; j < T; ++ j){
            scanf("%d%d", &a, &b);
            type[a][b].push_back(i);
        }
    }
}

void check_ans(){
    int i, p = 0;
    for ( i = 0; i < m; ++ i ){
        if ( !num[i] ){
            return;
        }
    }
    for ( i = 1; i <= n; ++ i ){
        p += tmp[i];
    }
    if ( p < Ansn ){
        memcpy(Ans, tmp, sizeof(tmp));
        Ansn = p;
    }
}

void Search(int x){
    if ( x > n ){
        check_ans();
        return;
    }
    tmp[x] = 0;
    for ( i = 0; i < type[x][0].size(); ++ i ){
        ++ num[ type[x][0][i] ];
    }
    Search(x + 1);
    for ( i = 0; i < type[x][0].size(); ++ i ){
        -- num[ type[x][0][i] ];
    }
    tmp[x] = 1;
    for ( i = 0; i < type[x][1].size(); ++ i ){
        ++ num[ type[x][1][i] ];
    }
    Search(x + 1);
    for ( i = 0; i < type[x][1].size(); ++ i ){
        -- num[ type[x][1][i] ];
    }
}
    

void solve(int ti){
    memset(num, 0, sizeof(num));
    memset(tmp, 0, sizeof(tmp));
    Ansn = n + 1;
    Search(1);
    printf("Case #%d: ", ti);
    if ( Ansn > n ){
        printf("IMPOSSIBLE\n");
    }
    else{
        for ( i = 1; i < n; ++ i){
            printf("%d ", Ans[i]);
        }
        printf("%d\n", Ans[n]);
    }
}

int main(){
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int t, i;
    scanf("%d", &t);
    for ( i = 1; i <= t; ++ i){
        input();
        solve(i);
    }
    return 0;
}
        
