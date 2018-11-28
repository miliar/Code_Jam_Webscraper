#include <stdio.h>
#include <algorithm>
using namespace std;
struct abc{
    int x, id;
    bool operator < (const abc &a) const{
        return x < a.x;
    }
}a[1010];
int main(){
    int T, n, i, ri = 1, t;
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    scanf("%d", &T);
    while (T--){
        scanf("%d", &n);
        for (i = 0; i < n; i++){
            scanf("%d", &a[i].x);
            a[i].id = i;
        }
        sort(a, a + n);
        t = 0;
        for (i = 0; i < n; i++){
            if (a[i].id != i){
                t++;
            }
        }
        printf("Case #%d: %d.000000\n", ri++, t);
    }
    return 0;
}
