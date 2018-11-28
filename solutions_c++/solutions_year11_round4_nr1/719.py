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
#define EPS 1e-7
using namespace std;

int be[1005], en[1005];
int w[1005];
double speed[1005];

int sgn(double x)
{
    return (x > EPS) - (x < -EPS);
}

int main()
{
    freopen("data1.in", "r", stdin);
    freopen("data.out", "w", stdout);

    int T;
    double X, S, R, t, N;
    scanf("%d", &T);
    for(int tcase = 1; tcase <= T; tcase++)
    {
        memset(speed, 0, sizeof(speed));
        scanf("%lf%lf%lf%lf%lf", &X, &S, &R, &t, &N);
        speed[0] = X;
        for(int i = 0; i < N; i++)
        {
            scanf("%d%d%d", &be[i], &en[i], &w[i]);
            speed[ w[i] ] += (en[i] - be[i]);
            speed[0] -= (en[i] - be[i]);
        }
//        for(int i = 0; i <= 3; i++)
//            printf("%lf\n", speed[i]);
        double ans = 0;
        for(int i = 0; i <= 100; i++)
        {
            if(sgn(t) > 0)
            {
                double timet = speed[i] / (i + R);
//                printf("%lf\n", timet);
                if(sgn(timet - t) <= 0)
                {
                    ans += timet;
                    t -= timet;
                }
                else
                {
                    speed[i] -= t * (i + R);
                    ans += t;
                    t = 0;
                    ans += (speed[i] / (i + S));
                }
            }
            else
            {
                ans += (speed[i] / (i + S));
            }
        }
        printf("Case #%d: %.6lf\n", tcase, ans);
    }

    return 0;
}
