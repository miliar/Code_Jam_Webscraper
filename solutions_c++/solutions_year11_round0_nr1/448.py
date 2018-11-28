/*
    Qualification Round 2011 -
    Bot Trust
    by Dave Chang
*/
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std ;

    int T, N;
    int to, tb, ans;
    int po, pb;
    char prev;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &T);
    for(int z=1; z<=T; ++z) {
        scanf("%d", &N);
        to = tb = ans = 0;
        po = pb = 1;
        char tp[2];
        int place;
        for(int i=0; i<N; ++i) {
            scanf("%s %d", tp, &place);
            int dist, add;
            prev = '\0';
            if(tp[0]=='O') {
                dist = abs(place-po);
                po = place;
                add = max(0, dist-to) + 1;
                ans += add;
                tb += add;
                to = 0;
            }
            else {
                dist = abs(place-pb);
                pb = place;
                add = max(0, dist-tb) + 1;
                ans += add;
                to += add;
                tb = 0;
            }
            prev = tp[0];
            //printf("A: %d TB: %d TO: %d\n", ans, tb, to);
        }
        printf("Case #%d: %d\n", z, ans);
    }
    return 0;
}
