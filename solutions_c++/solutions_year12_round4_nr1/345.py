#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;

const int MAXN = 10010;

int tot, n, dist;
int d[MAXN], l[MAXN], far[MAXN];

int main() {
    freopen("a.in", "r", stdin);
    freopen("ou.txt", "w", stdout);
    scanf("%d", &tot);
    int num = 0;
    while (tot > num) {
        ++num;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i)
            scanf("%d%d", &d[i], &l[i]);
        scanf("%d", &dist);
        memset(far, -1, sizeof(far));
        for (int i = 0; i < n; ++i)
            if (l[i] >= d[i])
                far[i] = d[i]*2;
        bool ans = false;
        int en = 1;
        for (int i = 0; i < n; ++i) {
            if (far[i] < 0)  continue;
            while (en < n && d[en] <= far[i]) {
                if (d[en]-d[i] > l[en])
                    far[en] = d[en] + l[en];
                else
                    far[en] = 2*d[en]-d[i];
                ++en;
            }
            if (far[i] >= dist)
                ans = true;
        }
        printf("Case #%d: ", num);
        if (ans)
            printf("YES\n");
        else
            printf("NO\n");
    }
}
