#include <cstdio>
#include <algorithm>

#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define FORD(i,a,b) for(int i=(int)(a);i>=(int)(b);--i)
#define FORE(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();++i)
#define FORED(i,c) for(__typeof((c).begin()) i=(c).end();i!=(c).begin();--i)
#define ITER(c) __typeof((c).begin())
#define SZ(a) (int)(a).size()

#define MAXN 1337

typedef long long LL;
typedef unsigned long long ULL;

using namespace std;

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w+", stdout);
    int n;
    scanf("%d", &n);
    REP(i, n) {
        int nb, nms[MAXN], test = 0;
        LL sum = 0LL;
        scanf("%d", &nb);
        REP(j, nb) {
            scanf("%d", &nms[j]);
            test ^= nms[j];
        }

        if (test == 0) {
            sort(nms, nms + nb);
            FOR(j, 1, nb - 1) sum += nms[j];
        }
        
        if (sum == 0)
            printf("Case #%d: NO\n", i + 1);
        else
            printf("Case #%d: %lld\n", i + 1, sum);
    }
    fclose(stdin);
    fclose(stdout);
}
