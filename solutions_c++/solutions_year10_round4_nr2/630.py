#include <cstdio>
#include <vector>
#include <map>
#include <string>
#include <set>
#include <queue>
#include <cmath>
#include <cstring>
#include <algorithm>

const int inf = 100000000;

int n, k;
int m[1<<11];
int cost[11][1<<11];
int dp[11][1<<11][11];

int computeBest(int level, int game, int stillWillSee)
{
    if (level == k)
    {
        if (stillWillSee < k - m[game]) return inf;
        else return 0;
    }

    if (dp[level][game][stillWillSee] == -1)
    {
        int a = computeBest(level + 1, 2 * game, stillWillSee) + computeBest(level + 1, 2 * game + 1, stillWillSee);
        int b = cost[level][game] + computeBest(level + 1, 2 * game, 1 + stillWillSee) + computeBest(level + 1, 2 * game + 1, 1 + stillWillSee);
        dp[level][game][stillWillSee] = std::min(inf, std::min (a, b));
    }

    return dp[level][game][stillWillSee];
}

void gogo (int test)
{
    scanf ("%d", &n);
    k = n;
    n = 1 << n;


    for (int i = 0; i < n; ++i) scanf ("%d", &m[i]);

    for (int i = 0; i < k; ++i)
    {
        for (int j = 0; j < (1<<(k - i - 1)); ++j)
            scanf ("%d", &cost[k - i - 1][j]);
    }

    for (int i = 0; i <= k; ++i)
        for (int j = 0; j < (1<<k); ++j)
            for (int h = 0; h <= k; ++h)
                dp[i][j][h] = -1;

    printf ("Case #%d: %d\n", test, computeBest(0, 0, 0));
}

int main ()
{
    int tests = 0;
    scanf ("%d", &tests);

    for (int i = 1; i <= tests; ++i) gogo (i);
    return 0;
}
