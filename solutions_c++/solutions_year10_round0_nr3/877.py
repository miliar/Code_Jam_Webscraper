#include <cstdio>
#include <algorithm>
#define FOR(i,a,b) for (int i=(a);i<(b);++i)

using namespace std;

typedef long long LL;

const int MN = 1009;

LL Q[MN];
LL B[MN];
int D[MN];

int main() {
    int lw;
    scanf("%d",&lw);
    FOR(l,1,lw+1) {
        int R; LL k;
        int n;
        scanf("%d%lld%d",&R,&k,&n);
        FOR(i,0,n)
            scanf("%lld",&Q[i]);
        FOR(i,0,n) {
            B[i] = Q[i];
            int j = (i+1)%n;
            while (i!=j && B[i]+Q[j] <= k) {
                B[i] += Q[j];
                j = (j+1)%n;
            }
            D[i] = j;
        }
        int act = 0;
        LL res = 0;
        FOR(i,0,R) {
            res += B[act];
            act = D[act];
        }
        printf("Case #%d: %lld\n",l,res);
    }
    return 0;
}
