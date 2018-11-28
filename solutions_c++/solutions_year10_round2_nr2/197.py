#include <stdio.h>
int x[55],v[55];
int main() {
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int ca;
    scanf("%d", &ca);
    for(int vv=1; vv<=ca; vv++) {
        int n,k,b,t;
        scanf("%d%d%d%d", &n, &k, &b, &t);
        for(int i=0; i<n; i++) {
            scanf("%d", &x[i]);
            x[i] = b-x[i];
        }
        for(int i=0; i<n; i++) {
            scanf("%d", &v[i]);
        }
        int ret = 0, ok=0;
        for(int i=n-1; i>=0; i--) {
            if(x[i] <= t*v[i]) {
                for(int j=i+1; j<n; j++) {
                    if(x[j] > t*v[j]) ret++;
                }
                ok++;
                if(ok == k) break;
            }
        }
        if(ok < k) printf("Case #%d: IMPOSSIBLE\n", vv);
        else printf("Case #%d: %d\n", vv, ret);
    }
    return 0;
}
