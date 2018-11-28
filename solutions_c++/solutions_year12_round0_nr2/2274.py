#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int cases = 1; cases <= t; cases++) {
        int n, s, p, ans = 0;
        scanf("%d%d%d", &n, &s, &p);
        for (int i = 0; i < n; i++) {
            int x;
            scanf("%d", &x);
            int now = x / 3;
            if (x % 3) now++;
            if (now >= p) {
                ans++;
                continue;
            }
            now = x / 3 + x % 3;
            if (x % 3 == 0 && x) now++;
            if (s && now >= p) s--, ans++;
        }
        printf("Case #%d: %d\n", cases, ans);
    }
    return 0;
}
