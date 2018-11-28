/*
 * summary:
 *
 */

#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <string>
#include <map>
#include <vector>
#include <stack>
#include <queue>
#include <string.h>
#define INF (1<<30)
#define MAX 0
#define EPS 0
using namespace std;

int gcd(int a, int b)
{
    if(a < b) swap(a, b);
    if(b == 0) return a;
    return gcd(a % b, b);
}

int main()
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);

    int T, D, G;
    long long N;
    scanf("%d", &T);
    for(int tcase = 1; tcase <= T; tcase++)
    {
        printf("Case #%d: ", tcase);
        scanf("%lld%d%d", &N, &D, &G);
//        printf("%lld\n", N);
        int td = gcd(D, 100);
        int tg = gcd(G, 100);
        D /= td;
        G /= tg;
        td = 100 / td;
        tg = 100 / tg;
        if((D != 0 && G == 0) || (D != td && G == tg))
        {
            printf("Broken\n");
            continue;
        }
        if(td <= N)
        {
            printf("Possible\n");
        }
        else
        {
            printf("Broken\n");
        }
    }

    return 0;
}
