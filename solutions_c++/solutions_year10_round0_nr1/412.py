#include <iostream>

using namespace std;

void solve(int test)
{
    int n, k, dg[50];
    scanf("%d%d", &n, &k);
    memset(dg, 0, sizeof(dg));
    int t = 0;
    while (k > 0) t ++, dg[t] = k % 2, k /= 2;

    int good = 0;
    for (int i = 1; i <= n; i ++)
        if (dg[i] == 1) good ++;
    if (good == n) printf("Case #%d: ON\n", test); else
        printf("Case #%d: OFF\n", test);
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