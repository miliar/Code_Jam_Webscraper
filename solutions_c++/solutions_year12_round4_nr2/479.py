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

int rr[1005];
int n, R, C;
struct node {
    int id, r;
    bool operator < (const node &w) const {
        return r > w.r;
    }
};
node dd[1005];
struct point {
    int x, y;
};
point pp[1005];
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        scanf("%d%d%d", &n, &R, &C);
        for (int i = 0; i < n; ++i) {
            scanf("%d", &rr[i]);
            dd[i].id = i; dd[i].r = rr[i];
        }
        sort(dd, dd + n);
        int x = 0, y = 0;
        int ny = dd[0].r;
        for (int i = 0; i < n; ++i) {
            pp[dd[i].id].x = x; pp[dd[i].id].y = y;
            x += dd[i].r;
            if (i < n - 1) x += dd[i + 1].r;
            if (x > R) {
                x = 0;
                y = ny + dd[i].r;
                ny += 2 * dd[i].r;
            }
        }
        printf("Case #%d:", ca);
        for (int i = 0; i < n; ++i) {
            printf(" %d %d", pp[i].x, pp[i].y);
        }
        printf("\n");
    }
    return 0;
}
