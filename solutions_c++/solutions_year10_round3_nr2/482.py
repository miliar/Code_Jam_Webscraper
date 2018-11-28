#include <iostream>
#pragma comment (linker, "/STACK:1024000000")

using namespace std;

int d[1100][1100][11];

int calc(int l, int r, int c)
{
    if (d[l][r][c] != -1) return d[l][r][c];
    if (l * c >= r) {d[l][r][c] = 0; return 0;}

    d[l][r][c] = 1000000;
    for (int i = l + 1; i <= r - 1; i ++)
        d[l][r][c] = min(d[l][r][c], max(calc(l, i, c), calc(i, r, c)) + 1);

    return d[l][r][c];
}

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);

    for (int i = 1; i <= 1000; i ++)
        for (int j = i + 1; j <= 1000; j ++)
            for (int k = 2; k <= 10; k ++)
                d[i][j][k] = -1;

    int test;
    scanf("%d", &test);
    for (int i = 1; i <= test; i ++)
    {
        int l, p, c;
        scanf("%d%d%d", &l, &p, &c);
        printf("Case #%d: %d\n", i, calc(l, p, c));
    }

    return 0;
}