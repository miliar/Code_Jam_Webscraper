#include <stdio.h>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;
int a[2010], n;
bool pd(){
    int i, j;
    for (i = 1; i < n; i++){
        for (j = i + 1; j < a[i]; j++){
            if (a[j] > a[i]) return false;
        }
    }
    return true;
}
int base = 10000;
int h[2010];
int main(){
    int T, ri = 1, i, j, k, x, low, high;
    srand(time(0));
    freopen("C-small-attempt3.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        scanf("%d", &n);
        for (i = 1; i < n; i++){
            scanf("%d", &a[i]);
        }
        printf("Case #%d:", ri++);
        if (!pd()){
            printf(" Impossible\n");
            continue;
        }
        h[1] = base;
        printf(" %d", base);
        for (i = 2; i <= n; i++){
            low = 0;
            high = 10000;
            for (j = 1; j < i; j++){
                if (a[j] == i){
                    for (k = j + 1; k < i; k++){
                        x = i;
                        low = max(low, (int)ceil((h[k] - h[j] * 1.0) / (k - j) * (x - j) + h[j] + 1));
                    }
                }else if (a[j] < i){
                    x = a[j];
                    k = i;
                    high = min(high, (int)floor((h[x] - h[j] * 1.0) / (x - j) * (k - j) + h[j] - 1));
                }
            }
            if (low < base){
                h[i] = max(min(min(high, base) + 1000 - rand() % 2000, high), low);
            }else{
                h[i] = low;
            }
            if (low > high) printf("Dam!!");
            printf(" %d", h[i]);
        }
        printf("\n");
    }
    return 0;
}
