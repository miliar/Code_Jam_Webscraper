#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>

using namespace std;

bool check(int a, int b)
{
    if (b == 0) return true;
    bool r = check(b, a % b);
    int d = a / b;
    if (!r) return true;
    if (d == 1) return false;
    return true;
}
int main()
{
    //freopen("C-small-attempt0.in", "r", stdin);
    //freopen("C-small-attempt0.out", "w", stdout);
    int T, a1, a2, b1, b2;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        scanf("%d%d%d%d", &a1, &a2, &b1, &b2);
        int ans = 0;
        for (int i = a1; i <= a2; ++i)
            for (int j = b1; j <= b2; ++j) {
                if (check(max(i, j), min(i, j))) {
                    ans++;
                }
            }
        printf("Case #%d: %d\n", ca, ans);
    }

    return 0;
}
