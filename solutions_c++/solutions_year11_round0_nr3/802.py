#include <cstdio>

const int N = 1010;
const int INF = 1<<29;

int n;

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t, x, v, cas = 0;
    scanf("%d", &t);
    while (t--){
        scanf("%d", &n);
        x = INF;
        long long sum = 0, xsum = 0;
        while (n--){
            scanf("%d", &v);
            if (x > v) x = v;
            sum += v;
            xsum ^= v;
        }
        printf("Case #%d:", ++cas);
        if (xsum) puts(" NO");
        else printf(" %lld\n", sum-x);
    }
    return 0;
}
