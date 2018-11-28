#include <iostream>
#include <string>
#include <string.h>
#include <cstring>

using namespace std;

int n, m;
char s[200];
int a[600][600];
int d[600][600], used[600][600];
int b[600][600];

int have[600];

int t[600][600];

int sum (int x, int y)
{
	int result = 0;
	for (int i = x; i >= 0; i = (i & (i + 1)) - 1)
		for (int j = y; j >= 0; j = (j & (j + 1)) - 1)
			result += t[i][j];
	return result;
}

void inc (int x, int y, int delta)
{
	for (int i = x; i < n; i = (i | (i + 1)))
		for (int j = y; j < m; j = (j | (j + 1)))
			t[i][j] += delta;
}

int val(char c)
{
    if (c >= '0' && c <= '9') return c - '0';
    return c - 'A' + 10;
}

int calc(int x, int y, int p)
{
    int l = 1, r = max(2, p);
    while (r - l > 1)
    {
        int key = (l + r) / 2;
        if (x + key > n || y + key > m) {r = key; continue;}
        if (d[x + 1][y] >= key - 1 && d[x][y + 1] >= key - 1 && a[x][y] != a[x + 1][y] && a[x][y] != a[x][y + 1] && 
            a[x + key - 1][y + key - 1] != a[x + key - 2][y + key - 1] && a[x + key - 1][y + key - 1] != a[x + key - 1][y + key - 2])
            l = key; else r = key;
    }

    if (x + r > n || y + r > m) return l;
    if (d[x + 1][y] >= r - 1 && d[x][y + 1] >= r - 1 && a[x][y] != a[x + 1][y] && a[x][y] != a[x][y + 1] && 
            a[x + r - 1][y + r - 1] != a[x + r - 2][y + r - 1] && a[x + r - 1][y + r - 1] != a[x + r - 1][y + r - 2]) return r;
    return l;
}

int calc(int x, int y)
{
    int l = 1, r = d[x][y];
    if (used[x][y]) return 0;
    while (r - l > 1)
    {
        int key = (l + r) / 2;
        //if (b[x][y] - b[x + key][y] - b[x][y + key] + b[x + key][y + key] == 0) l = key; else r = key;
        if (sum(x + key - 1, y + key - 1) - sum(x + key - 1, y - 1) - sum(x - 1, y + key - 1) + sum(x - 1, y - 1) == 0)
            l = key; else r = key;
    }

    if (sum(x + r - 1, y + r - 1) - sum(x + r - 1, y - 1) - sum(x - 1, y + r - 1) + sum(x - 1, y - 1) == 0) return r;
    if (sum(x + l - 1, y + l - 1) - sum(x + l - 1, y - 1) - sum(x - 1, y + l - 1) + sum(x - 1, y - 1) == 0) return l;
    return 0;
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);

    int test;
    scanf("%d", &test);
    for (int it = 1; it <= test; it ++)
    {
        scanf("%d%d\n", &n, &m);
        for (int i = 0; i < n; i ++)
        {
            gets(s);
            for (int j = 0; j < m / 4; j ++)
            {
                int x = val(s[j]);
                a[i][4 * j + 3] = x % 2;
                a[i][4 * j + 2] = (x / 2) % 2;
                a[i][4 * j + 1] = (x / 4) % 2;
                a[i][4 * j + 0] = (x / 8) % 2;
            }
        }

        d[n - 1][m - 1] = 1;
        for (int i = 0; i < m; i ++)
            d[n - 1][i] = 1;
        for (int i = 0; i < n; i ++)
            d[i][m - 1] = 1;

        int p = max(n, m);
        for (int i = n - 2; i >= 0; i --)
            for (int j = m - 2; j >= 0; j --)
                d[i][j] = calc(i, j, p);

        for (int i = 0; i <= 550; i ++)
            have[i] = 0;

        for (int i = 0; i <= n + 5; i ++)
            for (int j = 0; j <= m + 5; j ++)
                b[i][j] = 0, used[i][j] = false, t[i][j] = 0;

        while (true)
        {
            int best = 0, bx = -1, by = -1;
            for (int i = 0; i < n; i ++)
                for (int j = 0; j < m; j ++)
                {
                    int cur = calc(i, j);
                    if (cur > best) best = cur, bx = i, by = j;
                }

            if (!best) break;
            if (best == 1)
            {
                for (int i = 0; i < n; i ++)
                    for (int j = 0; j < m; j ++)
                        if (!used[i][j]) have[1] ++;
                break;
            }
            have[best] ++;
            for (int i = bx; i < bx + best; i ++)
                for (int j = by; j < by + best; j ++)
                    used[i][j] = true, inc(i, j, 1);
            /*for (int i = n - 1; i >= 0; i --)
                for (int j = m - 1; j >= 0; j --)
                    b[i][j] = b[i + 1][j] + b[i][j + 1] - b[i + 1][j + 1] + used[i][j];*/
        }

        int res = 0;
        for (int i = 550; i >= 0; i --)
            if (have[i]) res ++;
        printf("Case #%d: %d\n", it, res);
        for (int i = 550; i >= 0; i --)
            if (have[i]) printf("%d %d\n", i, have[i]);
    }
    return 0;
}