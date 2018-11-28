#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#define SIZE 32

using namespace std;

int main()
{
   freopen("B-small.in", "r", stdin);
    freopen("B-small.out", "w", stdout);
    int C = 0, T;

    scanf("%d", &T);
    while (T--)
    {
        int N, a, b, c;
        scanf("%d %d %d", &N, &a, &b);
        int res = abs(b - a);
        if(N == 3)
        {
            scanf("%d", &c);
            res = __gcd(res, abs(c - b));
        }
        printf("Case #%d: %d\n", ++C, (res - (a % res)) % res);
    }

    return 0;
}
