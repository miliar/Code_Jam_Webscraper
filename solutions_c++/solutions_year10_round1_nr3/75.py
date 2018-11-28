
#define __STDC_FORMAT_MACROS

#include <cstdio>
#include <inttypes.h>

int T;

int fl[1000001] = {-1, 1, 2};

static int range_intersect(int a1, int a2, int b1, int b2)
{
    if (b1 > a1)
        a1 = b1;
    if (b2 < a2)
        a2 = b2;
    if (a1 > a2)
        return 0;
    return a2 - a1 + 1;
}

int main()
{
    for (int i = 3; i <= 1000000; i++) {
        int ja = 1;
        int jb = i-1;
        while (jb != ja) {
            int jx = (ja+jb)/2;
//            printf("probing %d; first winner (%d) = %d;\n", jx, jx, fl[jx] + jx);
            /* first winner */
            if (fl[jx] + jx <= i) {
                ja = jx + 1;
            } else {
                jb = jx;
            }
        }
        fl[i] = ja;
//        printf("first loser a=%d: %d\n", i, fl[i]);
    }

    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        uint64_t r = 0;

        int a1, a2, b1, b2;
        scanf("%d %d %d %d", &a1, &a2, &b1, &b2);
        for (int a = a1; a <= a2; a++) {
            r += range_intersect(b1, b2, 1, fl[a] - 1);
            r += range_intersect(b1, b2, fl[a] + a, 1000000);
        }
        printf("Case #%d: %" PRIu64 "\n", t, r);
    }

    return 0;
}

