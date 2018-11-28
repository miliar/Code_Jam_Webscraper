#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#define LL long long
using namespace std;
LL n;
LL a[3000], d[3000];
LL getR()
{
    return (rand() % 1000LL) * 1000LL + rand() % 1000LL;
}
void shuffle()
{
    for (LL i = 0; i < n; ++i)
        d[i] = getR();
    for (LL i = 0; i < n - 1; ++i)
        if (d[a[i]] < d[i])
            d[a[i]] = min(d[i] + getR(), 10000000LL);
}
bool check()
{
    for (LL i = 0;i < n - 1; ++i)
    {
        if (d[a[i]] < d[i]) return false;
        for (LL j = i + 1; j < a[i]; ++j)
            if ((d[a[i]] - d[i]) * (j - i) <= (d[j] - d[i]) * (a[i] - i)) return false;
        for (LL j = a[i] + 1; j < n; ++j)
            if ((d[a[i]] - d[i]) * (j - i) < (d[j] - d[i]) * (a[i] - i)) return false;
    }
    return true;
}
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    LL T;
    scanf("%lld", &T);
    for (LL ca = 1; ca <= T; ++ca)
    {
        scanf("%lld", &n);
        bool flag = false;
        for (LL i = 0; i < n - 1; ++i)
        {
            scanf("%lld", &a[i]);
            a[i]--;
            flag |= (a[i] == i);
        }
        if (flag)
        {
            printf("Case #%lld: Impossible\n", ca);
            continue;
        }
        flag = false;
        for (LL i = 0; i < 100000LL; ++i)
        {
            shuffle();
            flag = check();
            if (flag) break;
        }
        if (!flag)
        {
            printf("Case #%lld: Impossible\n", ca);
            continue;
        }
        printf("Case #%lld:", ca);
        for (LL i = 0; i < n; ++i) printf(" %lld", d[i]);
        printf("\n");
    }
    return 0;
}
