#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;
char c[10];
int main(){
    int T, n, px, py, p, t, tx, ty, tn, ri = 1;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &T);
    while (T--){
        scanf("%d", &n);
        t = 0;
        px = py = 1;
        tx = ty = 0;
        while (n--){
            scanf("%s%d", c, &p);
            if (c[0] == 'O'){
                tn = abs(p - px);
                tn = max(0, tn - (t - tx)) + 1;
                t = t + tn;
                tx = t;
                px = p;
            }
            else{
                tn = abs(p - py);
                tn = max(0, tn - (t - ty)) + 1;
                t = t + tn;
                ty = t;
                py = p;
            }
        }
        printf("Case #%d: %d\n", ri++, t);
    }
    return 0;
}
