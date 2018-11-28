#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <algorithm>

using namespace std;

int fpow(int base, int exp, int mod) {
    //printf("base = %d, exp = %d, mod = %d\n", base, exp, mod);
    if(exp < 0) return -1;
    if(exp == 0) return 1;
    if(exp == 1) return base;
    int c = fpow(base, exp/2, mod)%mod;
    c = (c*c)%mod;
    if(exp%2==1)
        c = (c*(base%mod))%mod;
    return c%mod;
}

#define ones(x) (1<<x)-1

int main() {
    
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int t; scanf("%d", &t);
    for(int i=1; i<=t; ++i) {
        int n, k; scanf("%d %d", &n, &k);
        //printf("ones(%d) = %d, k=%d\n", n, ones(n), k);
        printf("Case #%d: ", i);
        if((k&ones(n))==ones(n))
            printf("ON\n");
        else
            printf("OFF\n");
    }
    
}
