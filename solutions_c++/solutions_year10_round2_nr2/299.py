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

const int Max = 100;

int dis[Max], v[Max];
int n, b, k, t;

void input(){
    int i;
    scanf("%d%d%d%d", &n, &k, &b, &t);
    for (i = 1; i <= n; ++ i){
        scanf("%d", dis + i);
        dis[i] = b - dis[i];
    }
    for (i = 1; i <= n; ++ i) scanf("%d", v + i);
}

void solve(){
    int i, j, ans = 0, r = 0, tk = 0;
    for (i = n; i > 0; -- i){
        if (dis[i] > t * v[i]){
            ++ r;
        }
        else{
            ans += r;
            ++ tk;
        }
        if (tk >= k){
            printf("%d\n", ans);
            return;
        }
    }
    puts("IMPOSSIBLE");
}

int main(){
    int T, ti = 0;
    scanf("%d", &T);
    while (T --){
        input();
        printf("Case #%d: ", ++ ti);
        solve();
    }
    return 0;
}
    
