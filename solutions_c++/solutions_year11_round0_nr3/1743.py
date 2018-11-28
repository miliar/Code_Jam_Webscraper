#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>

using namespace std;

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int T, n;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        scanf("%d", &n);
        int x = 0, y = 100000000, s = 0, w;
        for (int i = 0; i < n; ++i) {
            scanf("%d", &w);
            x ^= w;
            y = min(y, w);
            s += w;
        }
        if (x != 0) printf("Case #%d: NO\n", ca);
        else printf("Case #%d: %d\n", ca, s - y);
    }
    return 0;
}
