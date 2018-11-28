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

int x[801], y[801], n;
long long Ans, Xt, Yt;

int main(){
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int t, ti, i;
    scanf("%d", &t);
    for ( ti = 1; ti <= t; ++ ti ){
        scanf("%d", &n);
        for ( i = 0; i < n; ++ i ){
            scanf("%d", &x[i]);
        }
        for ( i = 0; i < n; ++ i ){
            scanf("%d", &y[i]);
        }
        sort(x, x + n);
        sort(y, y + n);
        Ans = 0;
        for ( i = 0;i < n; ++ i ){
            Xt = x[i];
            Yt = y[n - i - 1];
            Ans += Xt * Yt;
        }
        printf("Case #%d: %I64d\n", ti, Ans);
    }
    return 0;
}
