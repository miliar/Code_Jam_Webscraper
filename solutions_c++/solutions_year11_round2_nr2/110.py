#include <stdio.h>
#include <algorithm>
using namespace std;
struct abc{
    long long p;
    int v;
    bool operator < (const abc & a) const{
        return p < a.p;
    }
}c[210];
int n;
long long d;
long long t18 = 1000000000000000000ll;
long long t6 = 1000000;
bool pd(long long t){
    long long x;
    int i, j;
    x = -2 * t18;
    for (i = 0; i < n; i++){
        for (j = 0; j < c[i].v; j++){
            x = max(x + d, c[i].p - t);
            if (x > c[i].p + t){
                return false;
            }
        }
    }
    return true;
}
int main(){
    int T, ri = 1, i;
    long long l, r, z;
    freopen("B-large (1).in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        scanf("%d%lld", &n, &d);
        d *= 1000000;
        for (i = 0; i < n; i++){
            scanf("%lld%d", &c[i].p, &c[i].v);
            c[i].p *= t6;
        }
        sort(c, c + n);
        l = -1;
        r = 3 * t18;
        while (l + 1 < r){
            z = (l + r) / 2;
            if (pd(z)){
                r = z;
            }
            else{
                l = z;
            }
        }
        printf("Case #%d: %lld.%06lld\n", ri++, r / 1000000, r % 1000000);
    }
    return 0;
}
