#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;

#define MAXN 110
int n, l, h;
int a[MAXN];

bool isok(int x)
{
    int i;
    for (i = 0; i < n; i++)
    {
        if ((a[i] > x && a[i] % x == 0)
            || (a[i] <= x && x % a[i] == 0)) continue;
        else break;
    }
    return i >= n;
}

int main()
{
    freopen("C-small-attempt0 (4).in", "r", stdin);
    freopen("1.out", "w", stdout);

    int i, j, cs, csnum;
    scanf ("%d", &csnum);

    for (cs = 1; cs <= csnum; cs++)
    {
        scanf ("%d %d %d", &n, &l, &h);
        for (i = 0; i < n; i++)
            scanf ("%d", &a[i]);

        for (i = l; i <= h; i++)
            if (isok(i)) break;
        if (i > h)
            printf ("Case #%d: NO\n", cs);
        else
            printf ("Case #%d: %d\n", cs, i);
    }
}

