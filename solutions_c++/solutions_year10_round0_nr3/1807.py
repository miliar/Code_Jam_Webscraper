#include <stdio.h>

int T, t;

int R, k, N;
long long g[1000];
int i, j;
long long cnt, sum;
int used[1000], st;
int pos[1000], len;
long long v[1000];
int off, period;
long long sum_off, sum_period;

int main() {

    scanf("%d", &T);

    for (t = 1; t <= T; t++) {
        scanf("%d %d %d", &R, &k, &N);
        sum = 0;
        for (i = 0; i < N; i++) {
            scanf("%lld", &g[i]);
            sum += g[i];
        }

        if (sum <= k) {
            printf("Case #%d: %lld\n", t, sum * R);
            continue;
        }

        for (i = 0; i < N; i++) used[i] = 0;

        i = 0; len = 0;
        while (used[i] == 0) {
            st = i;
            sum = 0;
            while (sum + g[i] <= k) {
                sum += g[i];
                i++;
                if (i == N) i = 0;
            }
            used[st] = 1;
            pos[len] = st;
            v[len] = sum;
            len++;
        }
        
        //printf("len = %d i = %d\n", len, i);

        j = 0;
        while (pos[j] != i) j++;
        off = j; period = len - j;
        
        sum_off = 0;
        for (j = 0; j < off; j++) sum_off += v[j];
        sum_period = 0;
        for (j = off; j < len; j++) sum_period += v[j];
        
        if (R <= len) {
            sum = 0;
            for (j = 0; j < R; j++) sum += v[j];
            printf("Case #%d: %lld\n", t, sum);
            continue;
        }

        cnt = sum_off;
        R -= off;
        cnt += (R / period) * sum_period;
        
        for (j = 0; j < R % period; j++)
            cnt += v[off + j];

        printf("Case #%d: %lld\n", t, cnt);
    }

    return 0;
}