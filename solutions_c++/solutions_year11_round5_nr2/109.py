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

int n;
int cc[10005];
int now[10001];
int dn;
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        scanf("%d", &n);
        if (!n) {
            printf("Case #%d: 0\n", ca);
            continue;
        }
        memset(cc, 0, sizeof(cc));
        int x;
        int m1 = 10000000, m2 = 0;
        for (int i = 0; i < n; ++i) {
            scanf("%d", &x);
            m1 = min(m1, x);
            m2 = max(m2, x);
            cc[x]++;
        }
        int ans = 100000000;
        dn = 0;
        m2++;
        for (int i = m1; i <= m2; ++i) {
            if (cc[i] > dn) {
                for (int j = dn - 1; j >= 0; --j)
                    now[j + cc[i] - dn] = now[j] + 1;
                for (int j = 0; j < cc[i] - dn; ++j)
                    now[j] = 1;
                dn = cc[i];
            } else {
                for (int j = 0; j < cc[i]; ++j)
                    now[j]++;
                for (int j = cc[i]; j < dn; ++j)
                    ans = min(ans, now[j]);
                dn = cc[i];
            }
        }
        printf("Case #%d: %d\n", ca, ans);
    }
    return 0;
}
