#include <cstdio>
#include <cstdlib>
#include <cmath>

int times(int x) {
    return log(x)/log(10) + 1;
}

int old[11], oldcnt;

int find(int k) {
    int i;
    for (i=0; i<oldcnt; i++) {
        if ( old[i] == k ) return 1;
    }
    
    return 0;
}

int main(void) {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T, A, B, p10[20], i, j, k;
    long long ans;

    p10[0] = 1;
    for (i=1; i<=8; i++) {
        p10[i] = p10[i-1] * 10;
    }

    scanf("%d", &T);

    for (int t=1; t<=T; ++t) {
        scanf("%d %d", &A, &B);
        ans = 0;

        for (i=A; i<B; i++) {
            int lm = times(i);
            oldcnt = 0;

            for (j=1; j<lm; ++j) {
                k = i/p10[j];
                k = k + (i%p10[j])*p10[lm-j];

                if ( k > i && k <= B ) {
                    if ( find(k) ) continue;
                    ans++;
                    old[oldcnt++] = k;
                }
            }
        }

        printf("Case #%d: %lld\n", t, ans);
    }

    return 0;
}
