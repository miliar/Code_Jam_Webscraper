#include <cstdio>
#include <cstring>

#define bint long long int

using namespace std;

bint T, C=1;
bint r, k, n;
bint v[1024];
bint prox[1024];
bint total[1024];

inline bint p(bint a) {
    return (a+1)%n;
}

inline bint a(bint b) {
    if (b == 0) return n-1;
    return b-1;
}

int main() {

    scanf("%lld",&T);
    while (T--) {
        scanf("%lld %lld %lld",&r, &k, &n);
        for(bint i=0;i<n;i++)
            scanf("%lld",&v[i]);

        //pre
        for (bint i=0;i<n;i++) {
            bint j=i;
            bint tot = 0;
            bint foi = 0;
            while (tot+v[j] <= k and foi < n) {
                tot += v[j]; foi++; j=p(j);
            }
            prox[i] = a(j);
            total[i] = tot;
        }

        bint resp=0;
        bint j=0;
        for (bint i=0;i<r;i++) {
            resp+= total[j];
            j = p(prox[j]);
        }
        printf("Case #%lld: %lld\n",C++,resp);
    }

    return 0;
}
