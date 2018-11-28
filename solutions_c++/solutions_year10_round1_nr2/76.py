
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <climits>

int T;
int cur[256];
int next[256];

static int max(int a, int b)
{
    if (a > b)
        return a;
    else
        return b;
}

static void makemin(int& x, int y)
{
    if (y < x)
        x = y;
}

int main()
{
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        int D, I, M, N;
        scanf("%d %d %d %d", &D, &I, &M, &N);
        for (int i = 0; i < 256; i++)
            cur[i] = 0;

        for (int pos = 0; pos < N; pos++)
        {
            int a;
            scanf("%d", &a);

//            printf("pos %d = %d\n", pos+1, a);

            /* delete this one */
            for (int i = 0; i < 256; i++) {
                next[i] = cur[i] + D;
            }

            /* change it to value i */
            for (int i = 0; i < 256; i++) {
                /* and previous one was j */
                for (int j = max(0, i - M); j < 256 && j <= i + M; j++) {
                    makemin(next[i], cur[j] + abs(a - i));
                }
//                printf("dp[%d] = %d\n", i, next[i]);
            }

            memcpy(cur, next, sizeof(cur));

            bool flag = true;
            /* extra rounds: insert */
            while (flag) {
                flag = false;

                /* insert intermediate value i */
                for (int i = 0; i < 256; i++) {
                    /* and previous one was j */
                    for (int j = max(0, i - M); j < 256 && j <= i + M; j++) {
                        int tmp = cur[j] + I;
                        if (tmp < next[i]) {
                            flag = true;
                            next[i] = tmp;
                        }
                    }
                }

                memcpy(cur, next, sizeof(cur));
            }
        }

        int r = INT_MAX;
        for (int i = 0; i < 256; i++)
            makemin(r, cur[i]);

        printf("Case #%d: %d\n", t, r);
    }

    return 0;
}

