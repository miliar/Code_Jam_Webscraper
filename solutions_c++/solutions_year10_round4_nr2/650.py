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


int Q[2048], p, n;
int M[2048];

void input(){
    int i, j;
    scanf("%d", &p);
    n = (1 << p);
    for (i = 0; i < n; ++ i){
        scanf("%d", M + i);
        M[i] = p - M[i];
    }
    for (i = 1; i < n; ++ i){
        scanf("%d", &j);
    }
}
int solve(){
    int i, j, k, ans = 0;
    //printf("%d %d\n", n, p);
    for (i = p; i >= 1; -- i){
        k = 1 << (p - i);
        for (j = 0; j < k; ++ j) Q[j] = 0;
        for (j = 0; j < n; ++ j){
            Q[j >> i] |= (M[j] >= (p-i + 1));
        }
        for (j = 0; j < k; ++ j) ans += Q[j];
        //printf("## %d %d %d\n", i, ta, k);
    }
    return ans;
}
int main(){
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    
    int T, ti = 0;
    scanf("%d", &T);
    while (T --){
        input();
        printf("Case #%d: %d\n", ++ ti, solve());
    }
    return 0;
}
