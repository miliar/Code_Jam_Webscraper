#include <stdio.h>
#include <algorithm>
using namespace std;
struct abc{
    int l, z;
    double t;
    bool operator < (const abc &a) const{
        return z < a.z;
    }
}a[1010];
int main(){
    int T, l, s, r, n, i, x, y, ri = 1;
    double t, ans, tt;
    freopen("A-large (2).in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        scanf("%d%d%d%lf%d", &l, &s, &r, &t, &n);
        r -= s;
        ans = 0;
        for (i = 0; i < n; i++){
            scanf("%d%d%d", &x, &y, &a[i].z);
            a[i].z += s;
            a[i].l = y - x;
            l -= y - x;
            a[i].t = a[i].l * 1.0 / a[i].z;
            ans += a[i].t;
        }
        a[n].z = s;
        a[n].l = l;
        a[n].t = a[i].l * 1.0 / a[i].z;
        ans += a[n++].t;
        sort(a, a + n);
        for (i = 0; i < n; i++){
            tt = a[i].l * 1.0 / (a[i].z + r);
            tt = min(t, tt);
            ans += tt + (a[i].l - (a[i].z + r) * tt) / a[i].z - a[i].t;
            t -= tt;
            if (t < 1e-8){
                break;
            }
        }
        printf("Case #%d: %.8f\n", ri++, ans);
    }
    return 0;
}
