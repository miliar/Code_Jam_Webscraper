#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int cas, tt;
    scanf("%d", &tt);
    for (cas = 1; cas <= tt; cas ++) {
        int n, sum = 0, mini = 10000000, res = 0, x;
        scanf("%d", &n);
        for (int i = 0; i < n; i ++) {
            scanf("%d", &x);
            sum += x;
            res ^= x;
            mini = min(mini, x);
        }
        if (res == 0)
            printf("Case #%d: %d\n", cas, sum - mini);
        else printf("Case #%d: NO\n", cas);
    }
    return 0;
}

