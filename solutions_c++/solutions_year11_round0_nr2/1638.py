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

char cc[26][26];
bool op[26][26];
char ss[200];
int n;
char ans[1000];
int m;
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        int c, d;
        memset(cc, -1, sizeof(cc));
        memset(op, false, sizeof(op));
        scanf("%d", &c);
        for (int i = 0; i < c; ++i) {
            scanf("%s", ss);
            int x = ss[0] - 'A', y = ss[1] - 'A';
            cc[x][y] = cc[y][x] = ss[2];
        }
        scanf("%d", &d);
        for (int i = 0; i < d; ++i) {
            scanf("%s", ss);
            int x = ss[0] - 'A', y = ss[1] - 'A';
            op[x][y] = op[y][x] = true;
        }
        scanf("%d", &n);
        scanf("%s", ss);
        m = 0;
        for (int i = 0; i < n; ++i) {
            if (m > 0 && cc[ans[m - 1] - 'A'][ss[i] - 'A'] >= 0) {
                ans[m - 1] = cc[ans[m - 1] - 'A'][ss[i] - 'A'];
            } else {
                bool hav = false;
                for (int j = 0; j < m; ++j) {
                    if (op[ans[j] - 'A'][ss[i] - 'A']) {
                        hav = true;
                        break;
                    }
                }
                if (hav) m = 0;
                else ans[m++] = ss[i];
            }
        }
        printf("Case #%d: [", ca);
        if (m) printf("%c", ans[0]);
        for (int i = 1; i < m; ++i)
            printf(", %c", ans[i]);
        printf("]\n");
    }
    return 0;
}
