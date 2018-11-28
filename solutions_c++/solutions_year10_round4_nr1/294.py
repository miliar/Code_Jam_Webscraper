#include <cstdio>
#include <vector>
#include <map>
#include <string>
#include <set>
#include <queue>
#include <cmath>
#include <cstring>
#include <algorithm>

int result = 0, k;
int T[202][202];
int G[10000][2];
int n;

bool check (int value)
{
    return false;
}

void gogo (int test)
{
    scanf ("%d", &k);

    for (int i = 0; i < 2 * k; ++i)
        for(int j = 0; j < 2 * k; ++j)
            T[i][j] = 0;

    int sx = k - 1;
    int sy = k - 1;

    n = 0;

    for (int i = 0; i < k; ++i)
        for (int j = 0; j <= i; ++j)
        {
            int py = sx - i + 2 * j;
            int px = i;
            scanf ("%d", &T[px][py]);
            G[n][0] = px;
            G[n][1] = py;
            ++n;
        }

    for (int i = k; i < 2 * k - 1; ++i)
        for (int j = 0; j < 2 * k - i - 1; ++j)
        {
            int py = i - k  + 1 + 2 * j;
            int px = i;
            scanf ("%d", &T[px][py]);
            G[n][0] = px;
            G[n][1] = py;
            ++n;
        }

    int best = 2 * k - 1;
    for (int i = 0; i < 2 * k; ++i)
        for (int j = 0; j < 2 * k; ++j)
        {
            int qx = i;
            int qy = j;
            int gut = 1;

            int cost = abs(qx - sx) + abs (qy - sy);

            for (int h = 0; h < n; ++h)
            {
                int x = G[h][0];
                int y = G[h][1];

                int nx = x + (qx - x) * 2;
                int ny = y + (qy - y) * 2;

                if (nx >= 0 && nx < 2 * k && T[nx][y] != 0 && T[nx][y] != T[x][y]) gut = 0;
                if (ny >= 0 && ny < 2 * k && T[x][ny] != 0 && T[x][ny] != T[x][y]) gut = 0;

                if (gut == 0) break;
            }

            if (gut) best = std::min (best, cost);
        }

    int c1 = 0;
    k = k + best;
    for (int i = 0; i < k; ++i)
        for (int j = 0; j <= i; ++j) 
            c1++;

    for (int i = k; i < 2 * k - 1; ++i)
        for (int j = 0; j < 2 * k - i - 1; ++j)
            c1++;

    printf ("Case #%d: %d\n", test, c1 - n);
}

int main ()
{
    int tests = 0;
    scanf ("%d", &tests);

    for (int i = 1; i <= tests; ++i) gogo (i);
    return 0;
}
