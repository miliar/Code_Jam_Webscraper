#include <stdio.h>
#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;

#define INF (1<<30)
int ABS(int x) { return x > 0 ? x : -x; }
int MAX(int x, int y) { return x > y ? x : y;}

int sum;
int p;

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C.out", "w", stdout);

    int cs, csnum, i, j, k, id, d, n, mn;
    char ch;

    scanf ("%d", &csnum);
    for (cs = 1; cs <= csnum; cs++)
    {
        sum = 0;
        mn = INF;
        p = 0;

        scanf ("%d", &n);
        for (i = 0; i < n; i++)
        {
            scanf ("%d", &k);
            p ^= k;
            //cout << "p " << p << endl;
            sum += k;
            if (k < mn) mn = k;
        }
        if (p != 0)
            printf ("Case #%d: NO\n", cs);
        else
            printf ("Case #%d: %d\n", cs, sum - mn);
    }
}
/*
10
4 O 1 O 2 O 3 B 6

*/

