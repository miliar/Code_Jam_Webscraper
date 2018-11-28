#include <cstdio>
#include <algorithm>

int main() {
    int T = 0;
    int n, opos, bpos, olast, blast, time, p;
    char r[2];
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d", &n);
        olast = blast = 0;
        opos = bpos = 1;
        for (int i = 0; i < n; i++) {
            scanf("%s%d", r, &p);
            if (r[0] == 'O') {
                time = std::abs(p - opos);
                olast += time;
                if (olast < blast)
                    olast = blast;
                olast++;
                opos = p;
            } else {
                time = std::abs(p - bpos);
                blast += time;
                if (blast < olast)
                    blast = olast;
                blast++;
                bpos = p;
            }
            //printf("(%d, %d), (%d, %d)\n", olast, blast, opos, bpos);
        }
        printf("Case #%d: %d\n", t, std::max(olast, blast));
    }
}
