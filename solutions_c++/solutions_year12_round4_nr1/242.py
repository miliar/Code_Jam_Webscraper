#include <stdio.h>
#include <algorithm>
using namespace std;
struct abc{
    long long d, l;
}c[10010];
int n, ri;
long long m;
int a[10010][10010];
bool pd(int x, int y){
    if (a[x][y] == ri) return false;
    a[x][y] = ri;
    int l = min(2 * c[y].d - c[x].d, c[y].d + c[y].l);
    if (l >= m) return true;
    for (int i = y + 1; i <= n; i++){
        if (c[i].d <= l){
            if (pd(y, i)) return true;
        }else break;
    }
    return false;
}
int main(){
    int T, i;
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    ri = 1;
    while (T--){
        scanf("%d", &n);
        c[0].d = 0;
        for (i = 1; i <= n; i++){
            scanf("%lld%lld", &c[i].d, &c[i].l);
        }
        scanf("%lld", &m);
        printf("Case #%d: ", ri++);
        if (pd(0, 1)){
            printf("YES\n");
        }else{
            printf("NO\n");
        }
    }
    return 0;
}
