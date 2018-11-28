#include <cstdio>

int main(){
    int T;

    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++){
        int n, l, h;
        int a[200];
        scanf("%d%d%d", &n, &l, &h);
        for (int i = 0; i < n; i++)
            scanf("%d", a + i);
        int flag = 0, ans;
        for (int i = l; i <= h && !flag; i++){
            int f = 1; 
            for (int j = 0; j < n && f; j++)
                if ((a[j] % i) && (i % a[j]))
                    f = 0;
            if (f) {
                flag = 1;
                ans = i;
            }
        }
        printf("Case #%d: ", cas);
        if (!flag) printf("NO\n");
        else printf("%d\n", ans);
    }
    return 0;
}