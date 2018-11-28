#include <stdio.h>

bool solve(int n, int k)
{
    long long x = 1LL << n;
    k = k % x;
    x--;
    return k ==x;
}

int main()
{
    int ttttttt;
    scanf("%d", &ttttttt);

    int tcase = 1;
    while(ttttttt--)
    {
        long long n, k;
        scanf("%lld %lld", &n, &k);
        printf("Case #%d: %s\n", tcase++, solve(n, k) ? "ON" : "OFF");
    }
}
