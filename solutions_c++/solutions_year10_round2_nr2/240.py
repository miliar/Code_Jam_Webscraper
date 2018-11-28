#include <cstdio>
using namespace std;
int N, K, B, T,C;
int x[60], v[60];
bool flag[60];
void init();
void solve();
int main(){
    freopen("bl.in", "r", stdin);
    freopen("bl.out", "w", stdout);
    scanf("%d", &C);
    for (int t = 1; t <= C; ++t) {
        init();
        printf("Case #%d: ", t);
        solve();
    }
    return 0;
}
void solve(){
    int ans = 0 , cost = 0;
    for (int i = N-1; i >= 0; --i) {
        if (x[i] + v[i] * T >= B) {
            flag[i] = true;
            --K;
            ans += cost;
        }
        else ++cost;
        if ( K == 0) break;
    }
    if ( K > 0) printf("IMPOSSIBLE\n");
    else printf("%d\n", ans);
}
void init(){
    scanf("%d%d%d%d", &N, &K, &B, &T);
    
    for (int i = 0; i < N; ++i) {
        scanf("%d", &x[i]);
    }
    for (int i = 0; i < N; ++i) {
        scanf("%d", &v[i]);
    }
    
    for (int i = 0; i < N; ++i) {
        flag[i] = false;
    }
    
}
