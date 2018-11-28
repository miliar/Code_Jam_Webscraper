#include <cstdio>
using namespace std;

const int INF = 1<<20;

int main() {
    int t, n, a[1010], b[1010], stars, sum, levels, posa, maxb;
    bool fa, fb;
    
    scanf("%d", &t);
    for (int k = 1; k <= t; k++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%d %d", &a[i], &b[i]);
        }
        
        sum = levels = stars = 0;
        fa = 1;
        while ((fa || fb) && (levels < n)) {
            sum++;
            fa = fb = 0;
            maxb = -1;
            for (int i = 0; i < n; i++) {
                if (stars >= b[i]) {
                    levels++;
                    if (a[i] == INF) {
                        stars += 1;
                        b[i] = INF;
                    } else {
                        stars += 2;
                        a[i] = b[i] = INF;
                    }
                    fb = 1;
                    break;
                } else if (stars >= a[i]) {
                    fa = 1;
                    if (maxb < b[i]) {
                        maxb = b[i];
                        posa = i;
                    }
                }
            }
            
            if (fa && !fb) {
                stars += 1;
                a[posa] = INF;
            }
        }
        
        if (levels == n) {
            printf("Case #%d: %d\n", k, sum);
        } else {
            printf("Case #%d: Too Bad\n", k);
        }
    }
}
