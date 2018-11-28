#include <cstdio>
#include <vector>
#include <map>
#include <string>
#include <set>
#include <queue>
#include <cmath>
#include <cstring>
#include <algorithm>

int T[302][302];
int n;

void gogo (int test)
{
    for (int i  = 0; i <= 100; ++i)
        for (int j  = 0; j <= 100; ++j)
            T[i][j] = 0;

    scanf ("%d", &n);
    for (int i = 0; i < n; ++i)
    {
        int a, b, c, d;
        scanf ("%d %d %d %d", &a, &b, &c, &d);
        if (a > c) std::swap (a, c);
        if (b > d) std::swap (b, d);
        for (int j = b; j <= d; ++j)
            for (int k = a; k <= c; ++k)
                T[j][k] = 1;
    }

    int iter = 0;

    while (true)
    {
        int found = 0;
        for (int i  = 100; i > 0; --i)
            for (int j  = 100; j > 0; --j)
                {
                    if (T[i][j]) found = 1;

                    if (T[i-1][j] == 0 && T[i][j-1] == 0 && T[i][j] == 1) T[i][j] = 0;
                    else if (T[i-1][j] == 1 && T[i][j-1] == 1 && T[i][j] == 0) T[i][j] = 1;
                }


        if (!found) break;
        ++iter;
    }

    printf ("Case #%d: %d\n", test, iter);
}

int main ()
{
    int tests = 0;
    scanf ("%d", &tests);

    for (int i = 1; i <= tests; ++i) gogo (i);
    return 0;
}
