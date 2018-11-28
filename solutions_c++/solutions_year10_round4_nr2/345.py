#include <iostream>
#include <string>
#include <string.h>
#include <cstring>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#pragma comment (linker, "/STACK:256000000")

using namespace std;

int p, n, k;
int a[3000];
int c[3000];
long long d[3000][20];

long long mn(long long a, long long b)
{
    return (a < b ? a : b);
}

long long calc(int m, int sub)
{
    if (d[m][sub] != -1) return d[m][sub];
    if (m >= n) 
    {
        int cur = m - n + 1;
        if (a[cur] - sub < 0) d[m][sub] = 1000000000000LL; else
            d[m][sub] = 0;
        return d[m][sub];
    }

    d[m][sub] = 1000000000000LL;
    d[m][sub] = mn(d[m][sub], calc(2 * m, sub) + calc(2 * m + 1, sub) + (long long)(c[m]));
    d[m][sub] = mn(d[m][sub], calc(2 * m, sub + 1) + calc(2 * m + 1, sub + 1));
    return d[m][sub];
}

void solve(int test)
{
    scanf("%d", &p);
    for (int i = 1; i <= (1 << p); i ++)
        scanf("%d", &a[i]);
    for (int i = 1; i <= p; i ++)
        for (int j = (1 << (p - i)); j < (1 << (p - i + 1)); j ++)
            scanf("%d", &c[j]);

    for (int i = 1; i <= (1 << (p + 1)); i ++)
        for (int j = 0; j <= 12; j ++)
            d[i][j] = -1;
    n = (1 << p);
    k = n / 2;

    printf("Case #%d: %d\n", test, calc(1, 0));
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