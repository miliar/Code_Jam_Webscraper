#include <iostream>
#include <stdio.h>
#include <limits.h>

using namespace std;

int main()
{
    int t, cases, n, now, sum, min, i, x;
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &t);
    for (cases = 1; cases <= t; cases++) {
        scanf("%d", &n);
        now = 0; sum = 0; min = INT_MAX;
        for (i = 1; i <= n; i++) {
            scanf("%d", &x);
            if (x < min) min = x;
            now = now ^ x;
            sum += x;
        }
        if (now > 0) printf("Case #%d: NO\n", cases);
        else printf("Case #%d: %d\n", cases, sum - min);
    }
    return 0;
}
