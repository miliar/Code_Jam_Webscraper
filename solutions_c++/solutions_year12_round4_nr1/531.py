#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>

using namespace std;

int n;
int aa[10005], bb[10005];
int dd;
int ss[10005];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%d%d", &aa[i], &bb[i]);
        }
        scanf("%d", &dd);
        bool ok = false;
        memset(ss, -1, sizeof(ss));
        ss[0] = aa[0];
        for (int i = 0; i < n; ++i) {
            if (ss[i] < 0) break;
            if (ss[i] + aa[i] >= dd) {
                ok = true;
                break;
            }
            for (int j = i + 1; j < n && aa[i] + ss[i] >= aa[j]; ++j) {
                int t = aa[j] - aa[i];
                if (t > bb[j]) t = bb[j];
                if (ss[j] < 0 || t > ss[j]) ss[j] = t;
            }
        }
        if (ok) printf("Case #%d: YES\n", ca);
        else printf("Case #%d: NO\n", ca);
    }
    return 0;
}
