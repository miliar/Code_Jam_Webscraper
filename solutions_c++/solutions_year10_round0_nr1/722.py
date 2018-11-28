#include <cstdio>

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);
    int t, cas = 0;
    scanf("%d", &t);
    while (t--){
        long long n, k, x;
        scanf("%I64d %I64d", &n, &k);
        x = (1<<n)-1;
        printf("Case #%d: %s\n", ++cas, (k&x) == x ? "ON" : "OFF");
    }
    return 0;
}
