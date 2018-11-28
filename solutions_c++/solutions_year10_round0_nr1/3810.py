#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

long t, n;
long long ans[35], k;

int main()
{
    freopen("snapper.in", "r", stdin);
    freopen("snapper.out", "w", stdout);
    scanf("%ld\n", &t);
    ans[1] = 1;
    for (long i = 2; i <= 30; i ++)
         ans[i] = (ans[i - 1] + 1) * 2 - 1;
    for (long i = 1; i <= t; i ++)
    {
         scanf("%ld %lld\n", &n, &k);
         k = k % (ans[n] + 1);
         if (k == ans[n]) printf("Case #%ld: ON\n", i); else printf("Case #%ld: OFF\n", i);
    }
}
