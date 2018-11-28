#include <cstdio>
#include <algorithm>
#define FOR(i,a,b) for (int i=(a);i<(b);++i)

using namespace std;

typedef long long LL;

int main() {
    int lw;
    scanf("%d",&lw);
    FOR(l,1,lw+1) {
        LL n, k;
        scanf("%lld%lld",&n,&k);
        printf("Case #%d: ",l);
        if ((k&((1<<n)-1)) == ((1<<n)-1))
            printf("ON\n");
        else
            printf("OFF\n");
    }
    return 0;
}
