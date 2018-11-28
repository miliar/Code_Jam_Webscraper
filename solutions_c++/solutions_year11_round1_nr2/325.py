#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <sstream>
#include <fstream>
#include <cstring>
#include <string>

using namespace std;

#define MP make_pair
#define PB push_back
#define LB lower_bound
#define UB upper_bound

const double eps = 1e-8;
const double pi = acos(-1.0);

char sh[30], na[120][30];
int n, m, tim, can[120], le[120], Not[30];
int main()
{
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int T, tt = 0;
    for (scanf("%d", &T); T; T--) {
        printf("Case #%d:", ++tt);
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; i++) {
            scanf(" %s", na[i]);
            le[i] = strlen(na[i]);
        }
        memset(can, 0, sizeof(can));
        tim = 0;
        for (int i = 0; i < m; i++) {
            scanf(" %s", sh);
            int ans = -1, r;
            for (int x = 0; x < n; x++) {
                int opt = 0, now = 0;
                memset(Not, 0, sizeof(Not));
                for (int j = 0; j < 26; j++) {
                    bool flag = 0;
                    for (int y = 0; y < n; y++)
                        if (le[x] == le[y]) {
                            tim++;
                            bool may = 1;
                            for (int w = 0; w < le[x]; w++)
                                if (((1 << w) & opt)) {
                                    if (na[y][w] != na[x][w])
                                        may = 0;
                                    can[na[y][w] - 'a'] = tim;
                                } else
                                    if (Not[na[y][w] - 'a'])
                                        may = 0;
                            for (int w = 0; w < le[x]; w++)
                                if (!((1 << w) & opt) && can[na[y][w] - 'a'] == tim)
                                    may = 0;
                            if (may)
                                for (int w = 0; w < le[x]; w++)
                                    if (sh[j] == na[y][w])
                                        flag = 1;
                            if (flag)
                                break;
                        }
                    if (flag) {
                        int cc = 1;
                        for (int w = 0; w < le[x]; w++)
                            if (na[x][w] == sh[j]) {
                                opt |= (1 << w);
                                cc = 0;
                            }
                        now += cc;
                    }
                    Not[sh[j] - 'a'] = 1;
                }
                if (ans < now) {
                    ans = now;
                    r = x;
                }
            }
            printf(" %s", na[r]);
        }
        puts("");
    }
}

