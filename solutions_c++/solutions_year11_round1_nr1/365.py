#include <cstdio>
using namespace std;

typedef long long LL;
long long ans[102][102];

long long solve(int pd, int pg) {
    if (pg == 100 && pd == 100) return 1;
    if (pg == 0 && pd == 0) return 1;
    if (pg == 100) return -1;
    if (pg == 0) return -1;
    // printf("pd:%d pg:%d\n",pd,pg);
    LL D, up_G, lo, hi;
    if (100 - pd <= 100 - pg) {
        for (D = 1 ; D <= 1000000000000000LL; D++) {
            if (D * pd % 100) continue;
            else return D;
        }
    } else {
        for (D = 1 ; D <= 1000000000000000LL; D++) {
            if (D * pd % 100) continue;
            else return D;
        }
    }
    return -1;
}

int main() {
    freopen("a-large.in","r",stdin);
    freopen("a-large.out","w",stdout);
    int pd, pg, ca, T;
    LL N;
    for (pd = 0 ; pd <= 100 ; ++pd)
        for (pg = 0 ; pg <= 100 ; ++pg) {
            ans[pd][pg] = solve(pd, pg);
        }
    scanf("%d",&T);
    for (ca = 1 ; ca <= T ; ++ca) {
        scanf("%I64d%d%d",&N,&pd,&pg);
        printf("Case #%d: ",ca);
        if (ans[pd][pg] == -1 || ans[pd][pg] > N)
            printf("Broken\n");
        else
            printf("Possible\n");
    }
    return 0;
}
