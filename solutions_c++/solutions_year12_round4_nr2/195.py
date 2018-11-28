#include <stdio.h>
#include <algorithm>
using namespace std;
struct abc{
    int r, id;
    bool operator < (const abc &a) const{
        return r > a.r;
    }
}c[1010];
int x[1010], y[1010];
int main(){
    int T, ri = 1, n, w, l, i, y0, y1;
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        scanf("%d%d%d", &n, &w, &l);
        for (i = 0; i < n; i++){
            scanf("%d", &c[i].r);
            c[i].id = i;
        }
        sort(c, c + n);
        x[c[0].id] = y[c[0].id] = 0;
        y0 = 0;
        y1 = c[0].r;
        for (i = 1; i < n; i++){
            if (x[c[i - 1].id] + c[i - 1].r + c[i].r <= w){
                x[c[i].id] = x[c[i - 1].id] + c[i - 1].r + c[i].r;
                y[c[i].id] = y0;
            }else{
                y0 = y1 + c[i].r;
                y1 = y0 + c[i].r;
                x[c[i].id] = 0;
                y[c[i].id] = y0;
            }
        }
        printf("Case #%d:", ri++);
        for (i = 0; i < n; i++){
            printf(" %d.0 %d.0", x[i], y[i]);
        }
        printf("\n");
    }
    return 0;
}
