#include<iostream>
#include<cmath>

using namespace std;

int n;
int t[1000];
int gcd;

int main()
{
    int T, Ti;
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("task3.out.txt", "w", stdout);
    scanf("%d", &T);
    for(Ti = 1; Ti <= T; ++Ti)
    {
        int i, j;
        scanf("%d", &n);
        for(i = 0; i < n; ++i)
            scanf("%d", t+i);
        sort(t, t+n);
        gcd = t[1] - t[0];
        for(i = 0; i < n - 1; ++i)
            for(j = i + 1; j < n; ++j)
                gcd = __gcd(gcd, t[j] - t[i]);
        printf("Case #%d: %d\n", Ti, (gcd - t[0] % gcd) % gcd);
    }
    return 0;
}
