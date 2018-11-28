#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

int g[10000000];

int main(int argc, char *argv[])
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int T, cn;
    int R, k, N, i, j, cur, all, times, from, x;
    long long money;
    
    scanf("%d", &T);
    for (cn = 1; cn <= T; ++cn)
    {
        scanf("%d%d%d", &R, &k, &N);
        for (i = 0; i < N; ++i) {
            scanf("%d", &g[i]);
        }
        cur = 0;
        all = 0;
        money = 0;
        times = 0;
        while (times < R) {
            ++times;
            all = 0;
            //printf("times #%d:", times);
            from = cur;
            while ( (all == 0 || cur != from) &&
                   g[cur] + all <= k) {
                all += g[cur];
                //printf(" %d", g[cur]);
                ++cur;
                if (cur >= N) {
                    cur = 0;
                }
            }
            //printf("\n");
            money += all;
            if (0 == cur && money != 0) {
                if (R - times > times) {
                    x = (R - times) / times;
                    money += x * money;
                    times += x * times;
                }
            }
        }
        printf("Case #%d: %I64d\n", cn, money);
    }
    
	return 0;
}
