#include <cstdio>
#include <cstring>

typedef long long i64;
const int MAXN = 1010;

int r,k,n;
int g[MAXN];
i64 acc[MAXN];

i64 sum(int i, int j) {
    if (i > j) {
        return sum(0,j) + sum(i,n-1);
    }
    return acc[j] - (i>0 ? acc[i-1] : 0);
}

int memo[MAXN];
int end(int i) {
    int &ref = memo[i];
    if (ref == -1) {
        i64 s = g[i], j;
        for (j = i+1; j%n != i && s+g[j%n]<=k; ++j) {
            s += g[j%n];
        }
        ref = (j+n-1)%n;
    }
    return ref;
}

int main() {
    int t,c = 0;

    for (scanf("%d", &t); t-- > 0; ) {
        scanf("%d %d %d", &r, &k, &n);
        for (int i = 0; i < n; ++i) {
            scanf("%d", &g[i]);
            acc[i] = g[i] + (i>0 ? acc[i-1] : 0);
        }

        memset(memo,-1,sizeof memo);

        i64 res = 0;
        for (int i = 0; r > 0; --r) {
            int j = end(i);
            res += sum(i,j);
            i = (j+1)%n;
        }

        printf("Case #%d: %lld\n", ++c, res);
    }

    return 0;
}
