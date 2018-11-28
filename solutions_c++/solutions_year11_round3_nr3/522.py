#include <cstdio>
#include <algorithm>
using namespace std;
int r[111];

int main() {
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int T, ct = 1, f, low, hi, f2, n, i, j;
    scanf("%d",&T);
    while (T--) {
        scanf("%d %d %d",&n, &low, &hi);
        for (i = 0; i < n; ++i) {
            scanf("%d",r+i);
        }
        
        f = 0;
        for (i = low; i <= hi; ++i) {
            f2 = 0;
            for (j = 0; j < n; ++j) {
                if (i >= r[j]) {
                    if (i % r[j] != 0) {
                        f2 = 1;
                        break;
                    }
                }
                else {
                    if (r[j] % i != 0) {
                        f2 = 1;
                        break;
                    }               
                }
            }
            if (f2 == 0) {
                f = 1;
                break;
            }
        }
  
        if (f) printf("Case #%d: %d\n",ct++, i);
        else   printf("Case #%d: NO\n",ct++);
    }
    return 0;
}
