#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <math.h>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
using namespace std;

int Ans[] = {1, 5, 27, 143, 751, 935, 607, 903, 991, 335, 47, 943, 471, 55,
            447,463, 991, 95, 607, 263, 151, 855, 527, 743, 351, 135, 407,
            903, 791, 135, 647};
int n;
int main(){
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int t, i;
    scanf("%d", &t);
    for ( i = 1; i <= t; ++ i ){
        scanf("%d", &n);
        printf("Case #%d: ", i);
        if ( Ans[n] < 100 ){
            printf("0");
        }
        if ( Ans[n] < 10 ){
            printf("0");
        }
        printf("%d\n", Ans[n]);
    }
    return 0;
}
