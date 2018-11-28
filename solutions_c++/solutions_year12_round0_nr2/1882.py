#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>

using namespace std;

int n, s, p;
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        scanf("%d%d%d", &n, &s, &p);
        int ans = 0;
        int x;
        for (int i = 0; i < n; ++i) {
            scanf("%d", &x);
            int y = x / 3 + (x % 3 != 0);
            if (y >= p) {
                ans++;
                continue;
            }
            if (s <= 0 || x < 2 || x > 28 || x % 3 == 1) continue;
            if (y + 1 >= p) {
                s--;
                ans++;
            }
        }
        printf("Case #%d: %d\n", ca, ans);
    }
    return 0;
}
