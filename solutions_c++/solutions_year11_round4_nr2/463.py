// vim:set ts=8 sw=4 et smarttab:
// Round 2 2011

#include <cstdio>
#include <cassert>
#include <algorithm>

int n, m, d;
int map[500][500];
long long table_mx[501][501];
long long table_my[501][501];
long long table_m[501][501];

long long mx(int i1, int i2, int j1, int j2)
{
    return table_mx[i2 + 1][j2 + 1] - table_mx[i2 + 1][j1] - table_mx[i1][j2 + 1] + table_mx[i1][j1];
}

long long my(int i1, int i2, int j1, int j2)
{
    return table_my[i2 + 1][j2 + 1] - table_my[i2 + 1][j1] - table_my[i1][j2 + 1] + table_my[i1][j1];
}

long long mm(int i1, int i2, int j1, int j2)
{
    return table_m[i2 + 1][j2 + 1] - table_m[i2 + 1][j1] - table_m[i1][j2 + 1] + table_m[i1][j1];
}

long long calc_mx(int i, int j, int k)
{
    long long ret = mx(i, i + k - 1, j, j + k - 1);
    ret -= i * map[i][j];
    ret -= i * map[i][j + k - 1];
    ret -= (i + k - 1) * map[i + k - 1][j];
    ret -= (i + k - 1) * map[i + k - 1][j + k - 1];
    return ret;
}

long long calc_my(int i, int j, int k)
{
    long long ret = my(i, i + k - 1, j, j + k - 1);
    ret -= j * map[i][j];
    ret -= j * map[i + k - 1][j];
    ret -= (j + k - 1) * map[i][j + k - 1];
    ret -= (j + k - 1) * map[i + k - 1][j + k - 1];
    return ret;
}

long long calc_m(int i, int j, int k)
{
    long long ret = mm(i, i + k - 1, j, j + k - 1);
    ret -= map[i][j];
    ret -= map[i + k - 1][j];
    ret -= map[i][j + k - 1];
    ret -= map[i + k - 1][j + k - 1];
    return ret;
}

bool tryijk(int i, int j, int k)
{
    if (calc_mx(i, j, k) * 2 != calc_m(i, j, k) * (2 * i + k - 1))
        return false;
    if (calc_my(i, j, k) * 2 != calc_m(i, j, k) * (2 * j + k - 1))
        return false;
    return true;
}

bool tryk(int k)
{
    for (int i = 0; i <= n - k; ++i)
        for (int j = 0; j <= m - k; ++j)
            if (tryijk(i, j, k))
                return true;
    return false;
}

int solve()
{
    for (int j = 0; j < m; ++j)
        table_m[1][j + 1] = table_m[1][j] + map[0][j];
    for (int i = 1; i < n; ++i)
    {
        long long sum = 0;
        for (int j = 0; j < m; ++j)
        {
            sum += map[i][j];
            table_m[i + 1][j + 1] = table_m[i][j + 1] + sum;
        }
    }

    for (int j = 0; j < m; ++j)
        table_mx[1][j + 1] = table_mx[1][j] + map[0][j] * 0;
    for (int i = 1; i < n; ++i)
    {
        long long sum = 0;
        for (int j = 0; j < m; ++j)
        {
            sum += map[i][j] * i;
            table_mx[i + 1][j + 1] = table_mx[i][j + 1] + sum;
        }
    }

    for (int j = 0; j < m; ++j)
        table_my[1][j + 1] = table_my[1][j] + map[0][j] * j;
    for (int i = 1; i < n; ++i)
    {
        long long sum = 0;
        for (int j = 0; j < m; ++j)
        {
            sum += map[i][j] * j;
            table_my[i + 1][j + 1] = table_my[i][j + 1] + sum;
        }
    }

    int ret = -1;
    for (int k = 3; k <= std::min(n, m); ++k)
        if (tryk(k))
            ret = k;
    return ret;
}

int main()
{
    int ntc;
    scanf("%d", &ntc);
    for (int tc = 1; tc <= ntc; ++tc)
    {
        scanf("%d%d%d", &n, &m, &d);
        for (int i = 0; i < n; ++i)
        {
            char temp[1000];
            scanf("%s", temp);
            for (int j = 0; j < m; ++j)
                map[i][j] = temp[j] - '0';
        }
        int answer = solve();
        if (answer >= 0)
            printf("Case #%d: %d\n", tc, answer);
        else
            printf("Case #%d: IMPOSSIBLE\n", tc);
    }
}
