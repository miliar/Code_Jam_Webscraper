#include<cstdio>
#include<cstdlib>
#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>

using namespace std;

int segsize[1100];
int segspeed[1100];
int order[1100];

int comp(const void *a, const void *b)
{
    return segspeed[*((int*)a)] - segspeed[*((int*)b)];
}

int main()
{
    int teste, t;
    scanf("%d", &teste);
    for (t=0; t<teste; t++)
    {
        int n;
        int x;
        int walking;
        int running;
        int time;
        scanf("%d %d %d %d %d", &x, &walking, &running, &time, &n);

        int i;
        int remain = x;
        int a, b;
        for (i = 0; i < n; i++)
        {
            scanf("%d %d %d", &a, &b, &segspeed[i]);
            remain -= b - a;
            segsize[i] = b - a;
            order[i] = i;
        }

        if (remain > 0)
        {
            segsize[n] = remain;
            segspeed[n] = 0;
            order[n] = n;
            n++;
        }

        qsort(order, n, sizeof(int), comp);

        double rtime = time;
        double ans = 0;
        for (i = 0; i < n; i++)
        {
            double need = ((double)segsize[order[i]]) / (segspeed[order[i]] + running);
            //printf("%d %d %d %lf %lf %lf\n", order[i], segsize[order[i]], segspeed[order[i]], need, rtime, ans);
            if (rtime > 0)
            {
                if (need > rtime)
                {
                    ans += rtime;
                    double rdist = segsize[order[i]] - rtime * (segspeed[order[i]] + running);
                    ans += rdist / (segspeed[order[i]] + walking);
                    rtime = 0;
                }
                else
                {
                    ans += need;
                    rtime -= need;
                }
            }
            else
            {
                ans += ((double)segsize[order[i]]) / (segspeed[order[i]] + walking);
            }
        }

        printf("Case #%d: %lf\n", t+1, ans);
    }
    return 0;
}
