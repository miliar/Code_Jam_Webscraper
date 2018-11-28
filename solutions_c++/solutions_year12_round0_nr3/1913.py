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

int a, b;
bool visit[2000001];
int dd[10], ww[10], tt[10];
int ss[10];
int dn;
int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    tt[0] = 1;
    for (int i = 1; i <= 8; ++i)
        tt[i] = tt[i - 1] * 10;
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        scanf("%d%d", &a, &b);
        memset(visit + a, false, b - a + 1);
        int ans = 0;
        for (int i = a; i <= b; ++i) {
            if (visit[i]) continue;
            int cnt = 1;
            visit[i] = true;
            dn = 1;
            int s = i;
            int x = s % 10;
            dd[0] = x;
            ss[0] = x;
            s /= 10;
            ww[0] = s;
            while (s) {
                x = s % 10;
                ss[dn] = x;
                dd[dn] = x * tt[dn] + dd[dn - 1];
                s /= 10;
                ww[dn] = s;
                dn++;
            }
            int v;
            for (int j = 0; j < dn - 1; ++j) {
                if (ss[j] == 0) continue;
                v = dd[j] * tt[dn - j - 1] + ww[j];
                if (v >= a && v <= b && !visit[v]) {
                    visit[v] = true;
                    cnt++;
                }
            }
            ans += ((cnt * (cnt - 1)) >> 1);
        }
        printf("Case #%d: %d\n", ca, ans);
    }
    return 0;
}
