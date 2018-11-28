#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
using namespace std;

typedef long long lint;

const int INF = 0x0f0f0f0f;

const int M = 20001;


int change[M];
int gate[M];

int d[2][M];

int main()
{
    //freopen("A.in", "r", stdin);
    int cases;
    scanf("%d", &cases);
    for (int cs = 1; cs <= cases; ++cs)
    {
        memset(d, INF, sizeof(d));
        int m, v;
        scanf("%d %d", &m, &v);
        for (int i = 1; i <= (m-1) / 2; ++i)
        {
            scanf("%d %d", &gate[i], &change[i]);
        }
        for (int i = (m-1) / 2 + 1; i <= m; ++i)
        {
            int x;
            scanf("%d", &x);
            d[x][i] = 0;
        }

        for (int i = (m-1) / 2; i > 0; --i)
        {
            int c1 = 2*i;
            int c2 = 2*i + 1;
            int cost = (change[i] ? 1 : INF);
            // and gate
            d[0][i] = min(d[0][c1] + min(d[0][c2], d[1][c2]), 
                          d[0][c2] + min(d[0][c1], d[1][c1])) + (gate[i] ? 0 : cost);
            d[0][i] = min(d[0][i], INF);

            // or gate
            d[0][i] = min(d[0][i], d[0][c1] + d[0][c2] + (gate[i] ? cost : 0));
            d[0][i] = min(d[0][i], INF);

            // or gate
            d[1][i] = min(d[1][c1] + min(d[0][c2], d[1][c2]), 
                          d[1][c2] + min(d[0][c1], d[1][c1])) + (gate[i] ? cost : 0);
            d[1][i] = min(d[1][i], INF);

            // and gate
            d[1][i] = min(d[1][i], d[1][c1] + d[1][c2] + (gate[i] ? 0 : cost));
            d[1][i] = min(d[1][i], INF);
        }
        if (d[v][1] < INF) printf("Case #%d: %d\n", cs, d[v][1]);
        else printf("Case #%d: IMPOSSIBLE\n", cs, d[v][1]);
    }
    return 0;
}
