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

long long n, pd, pg;
long long gcd(long long a, long long b)
{
    if (b == 0) return a;
    return gcd(b, a % b);
}
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        cin >> n >> pd >> pg;
        long long d1 = gcd(pd, 100);
        long long a = pd / d1;
        long long b = 100 / d1;
        long long d2 = gcd(pg, 100);
        long long c = pg / d2;
        long long d = 100 / d2;
        if (b > n || a > 0 && c == 0 ||
            pd < 100 && pg == 100) {
            printf("Case #%d: Broken\n", ca);
        } else {
            printf("Case #%d: Possible\n", ca);
        }
    }
    return 0;
}
