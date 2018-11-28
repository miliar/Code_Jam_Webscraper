#include <cstdio>

const int MAX = 60;

int X[MAX], V[MAX];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.out","w",stdout);
    int t, N, K, B, T, cas = 0;
    scanf("%d", &t);
    while (t--){
        scanf("%d %d %d %d", &N, &K, &B, &T);
        for (int i = 0; i < N; ++i) scanf("%d", &X[i]);
        for (int i = 0; i < N; ++i) scanf("%d", &V[i]);
        int slow = 0, ans = 0;
        for (int i = N-1; i >= 0 && K; --i){
            if ((long long)X[i]+(long long)V[i]*T < B) ++slow;
            else ans += slow, --K;
        }
        printf("Case #%d: ", ++cas);
        if (K) puts("IMPOSSIBLE");
        else printf("%d\n", ans);
    }
    return 0;
}
