#include <cstdio>

const int N = 1010;

int n;

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t, cas = 0, x;
    scanf("%d", &t);
    while (t--){
        scanf("%d", &n);
        int ans = 0;
        for (int i = 1; i <= n; ++i){
            scanf("%d", &x);
            if (x != i) ++ans;
        }
        printf("Case #%d: %.6lf\n", ++cas, 1.0*ans);
    }
    return 0;
}
