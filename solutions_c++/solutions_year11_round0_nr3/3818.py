#include <cstdio>
#include <algorithm>
using namespace std;
const int M = 1<<15;
int v[1010];
char r[M];

int main() {
    freopen("C-small-attempt3.in","r",stdin);
    freopen("C-small-attempt3.out","w",stdout);
    int T, i, j, n, c1, c2, t1, t2, f, ct = 1, s1, s2, ans;
    scanf("%d",&T);
    while (T--) {
        scanf("%d",&n);
        for (i = 0; i < n; ++i)
            scanf("%d",v+i);
        f = 0;
        ans = 0;
        for (i = 0; i <= ( (1<<n) -  1); ++i) {
            c1 = c2 = 0;
            t1 = t2 = 0;
            //printf("%d\n",i);
            for (j = 0; j < n; ++j) {
                //printf("%d %d\n",(i & (1<<j)),j);
                if ( (i & (1<<j)) != 0) {
                   if (c1 == 0) s1 = v[j];
                   else         s1 ^= v[j];
                   t1 += v[j];
                   c1++;
                   //printf("1 %d\n",j);
                }
                else if ( (i & (1<<j)) == 0) {
                   if (c2 == 0) s2 = v[j];
                   else         s2 ^= v[j];
                   t2 += v[j];
                   c2++;
                   //printf("0 %d\n",j);
                }
            }
            
            if (s1 == s2 && c1 && c2) {
                //printf("%d %d\n",s1,s2);
                f = 1;
                ans = max( max(t1, t2), ans );
            }
        }
        if (f) printf("Case #%d: %d\n",ct++, ans);
        else   printf("Case #%d: NO\n",ct++);
    }
    return 0;
}
