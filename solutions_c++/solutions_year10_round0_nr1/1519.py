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

int n, k;

int main(){
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int t, Cas = 0;
    int l;
    scanf("%d", &t);
    while (t --){
        scanf("%d%d", &n, &k);
        l = (1 << n);
        k %= l;
        if (k != l - 1){
            printf("Case #%d: OFF\n", ++ Cas);
        }
        else{
            printf("Case #%d: ON\n", ++ Cas);
        }
    }
    return 0;
}

        
    
