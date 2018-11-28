#include <iostream>
#include <string>
#include <string.h>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <vector>

using namespace std;

int n, k;
char c[100][100], s[500];

pair < int, int > calc(int n, char s[])
{
    int a1 = 0, a2 = 0;

    int cur = 0;
    for (int i = 0; i < n; i ++)
        if (s[i] == 'R') cur ++, a1 = max(a1, cur); else cur = 0;
    cur = 0;
    for (int i = 0; i < n; i ++)
        if (s[i] == 'B') cur ++, a2 = max(a2, cur); else cur = 0;
    return make_pair(a1, a2);
}

bool val(int x, int y) {return (0 <= x && x < n && 0 <= y && y < n);}

void solve(int test)
{
    scanf("%d%d\n", &n, &k);
    for (int i = 0; i < n; i ++)
        gets(c[i]);

    for (int i = 0; i < n; i ++)
    {
        int p = n;
        for (int j = n - 1; j >= 0; j --)
            if (c[i][j] != '.') p --, c[i][p] = c[i][j];
        for (int j = p - 1; j >= 0; j --)
            c[i][j] = '.';
    }

    bool f1 = false, f2 = false;
    for (int i = 0; i < n; i ++)
    {
        for (int j = 0; j < n; j ++)
            s[j] = c[i][j];
        pair < int, int > p = calc(n, s);
        if (p.first >= k) f1 = true;
        if (p.second >= k) f2 = true;

        for (int j = 0; j < n; j ++)
            s[j] = c[j][i];
        p = calc(n, s);
        if (p.first >= k) f1 = true;
        if (p.second >= k) f2 = true;
    }

    for (int i = 0; i <= 2 * n; i ++)
    {
        int q = -1;
        for (int j = 0; j <= i; j ++)
            if (val(i - j, j)) q ++, s[q] = c[i - j][j];

        pair < int, int > p = calc(q + 1, s);
        if (p.first >= k) f1 = true;
        if (p.second >= k) f2 = true;

        q = -1;
        for (int j = n - 1; j >= 0; j --)
            if (val(j, i - (n - 1 - j))) q ++, s[q] = c[j][i - (n - 1 - j)];

        p = calc(q + 1, s);
        if (p.first >= k) f1 = true;
        if (p.second >= k) f2 = true;
    }

    if (f1 && f2) printf("Case #%d: Both\n", test);
    if (f1 && !f2) printf("Case #%d: Red\n", test);
    if (!f1 && f2) printf("Case #%d: Blue\n", test);
    if (!f1 && !f2) printf("Case #%d: Neither\n", test);
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int test;
    scanf("%d", &test);
    for (int i = 1; i <= test; i ++)
        solve(i);
    return 0;
}