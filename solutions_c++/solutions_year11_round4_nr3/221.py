#include <algorithm>
#include <stdio.h>

#define MAX 1000010
#define ll long long

using namespace std;

int testCases;
ll sel[MAX], pr[MAX];

int main()
{
    freopen("c-small.in", "r", stdin);
    freopen("c-small.out", "w", stdout);

    for (int i = 2; i <= 1000000; i++)
        if (!sel[i])
        {
            pr[++pr[0]] = i;
            for (int j = i; j <= 1000000; j += i)
                sel[j] = 1;
        }
    pr[++pr[0]] = 1000000000;

    int test = 0;
    for (scanf("%d", &testCases); testCases; testCases--)
    {
        test++;
        printf("Case #%d: ", test);

        ll n, sol = 0;
        scanf("%lld", &n);
        for (int i = 1; pr[i] * pr[i] <= n; i++)
        {
            ll nr = pr[i];
            for (; nr * pr[i] <= n; nr *= pr[i], sol++);
        }

        if (n > 1)
            sol++;

        printf("%lld\n", sol);
        fprintf(stderr, "%d\n", testCases);
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}
