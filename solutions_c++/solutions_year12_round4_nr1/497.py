#include <cstdio>
#include <vector>
#include <cstring>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define VAR(v,w) __typeof(w) v=(w)
#define FORE(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define PB push_back
#define MP make_pair
#define FT first
#define SD second

int n,d;
int pos[1000000], len[1000000], hang[1000000];

void test() {
    scanf("%d", &n);
    REP(i,n) {
        scanf("%d%d", &pos[i], &len[i]);
        hang[i] = -1;
    }
    scanf("%d", &d);
    int e = 1;
    hang[0] = pos[0];
    for (int s = 0; s < n; s++) {
        if (hang[s] < 0) continue;
        int od = hang[s] + pos[s];
        for (; e < n; e++) {
            if (od < pos[e]) break;
            hang[e] = min(pos[e]-pos[s], len[e]);
        }
    }
    REP(i,n) if (pos[i] + hang[i] >= d) {
        puts("YES");
        return;
    }
    puts("NO");
}

main() {
    int z; scanf("%d", &z);
    REP(i,z) {
        printf("Case #%d: ", i+1); test();
    }
}
