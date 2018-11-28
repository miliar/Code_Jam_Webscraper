#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <string>
#include <vector>
#include <string.h>
using namespace std;

int m[10];
int p[1024];
int n;

int main() {
    int T;
    scanf("%d", &T);
    int c, i, j, k;
    int res;
    int R;
    int n1, n2;
    int start = 0;
    int j1,k1,j2,k2;
    int count;
    for (c = 1; c <= T; c++) {
        scanf("%d", &n);
        for (i = 0; i < (1<<n); i++) {
            scanf("%d", &m[i]);
        }
        start = 0;
        count = 2;
        for (i = 0; i < (1<<n) - 1; i++) {
            scanf("%*d");
        }
        n1 = n - 1;
        res = 0;
        for (j = 0; j < n; j++) {
            
            for (i = 0; i < (1 << n1); i++) {
                //printf("%d %d\n", start, count);
                for (k = start; k < start + count ; k++) {
                    if (m[k] < j + 1) break;
                }
                if (k >= start + count) res++;
                start += count;
            }
            n1--;
            count <<= 1;
            start = 0;
        }        
        
        printf("Case #%d: %d\n", c, (1<<n) - 1 - res);
    }
    return 0;
}
