#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
int pd[200][200];
int v[200];

int n, s, p;
int main () {
    int t;
    scanf("%d", &t);
    for (int lo = 1; lo <= t; lo++) {
        scanf("%d %d %d", &n, &s, &p);
        for (int c = 1; c <= n; c++) {
            scanf("%d", &v[c]);
        }
        pd[0][0] = 0;
        for (int c = 1; c <= n; c++) {
            for (int g = 0; g <= c; g++) {
                pd[c][g] = -1;
                if (g != c) {
                    if (v[c] >= 3*p-2) pd[c][g] = max(pd[c][g], 1+pd[c-1][g]);
                    else pd[c][g] = max(pd[c][g], pd[c-1][g]);
                }
                if (g != 0) {
                    if (v[c] >= 2 && v[c] >= 3*p-4 && v[c] <= 28) {
                        pd[c][g] = max(pd[c][g],1+pd[c-1][g-1]);
                    }
                    else pd[c][g] = max(pd[c][g],pd[c-1][g-1]);
                }
            }
        }
        printf("Case #%d: %d\n", lo, pd[n][s]);
    }
    return 0;
}
                    
        
        
    

