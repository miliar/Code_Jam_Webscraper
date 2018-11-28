#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

int main() {
    freopen("D:\\TopCoder\\gcj2011\\QR\\C\\C.in", "r", stdin);
    freopen("D:\\TopCoder\\gcj2011\\QR\\C\\C.out", "w", stdout);
    int T;
    scanf("%d", &T);
    
    for (int ca = 1; ca <= T; ca++) {
        int n;
        scanf("%d", &n);
        int candy[n];
        int sum = 0, mnum = 1000000+20, xr = 0;
        for (int i = 0; i < n; i++) {
            scanf("%d", &candy[i]);
            xr ^= candy[i];
            sum += candy[i];
            mnum = min(mnum, candy[i]);
        }
        if (xr) {
            printf("Case #%d: NO\n", ca);
            continue;
        }
        printf("Case #%d: %d\n", ca, sum-mnum);
    }
            
    fclose(stdin);
    fclose(stdout);
    return 0;
}


