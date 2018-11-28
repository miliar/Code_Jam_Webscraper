// A CZM1.1
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<vector>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;

#define oo 1000000000
#define PI acos(-1.0)
#define eps 1e-5
const static int maxN = 1000 + 1;

struct Node
{
    int b, e, w;
    double v;
    bool operator < (const Node& o) const
    {
        return v > o.v;
    }
} walk[maxN];

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    int T;
    int cas = 1;
    int X, S, R, t, N;
    double ans;
    double dt;
    int i;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%d%d%d%d%d", &X, &S, &R, &t, &N);
        for (i = 0; i < N; i++)
        {
            scanf("%d%d%d", &walk[i].b, &walk[i].e, &walk[i].w);
            walk[i].v = (double)(R + walk[i].w) / (S + walk[i].w);
            X -= walk[i].e - walk[i].b;
        }
        walk[i].b = 0, walk[i].e = X, walk[i].w = 0;
        walk[i].v = (double)(R + walk[i].w) / (S + walk[i].w);
        sort(walk, walk + N + 1);
        ans = 0;
        dt = t;
        for (i = 0; i <= N; i++)
        {
            if (dt > 0)
            {
                if (dt * (R + walk[i].w) < (walk[i].e - walk[i].b))
                {
                    ans += dt;
                    ans += (double)(walk[i].e - walk[i].b - dt * (R + walk[i].w)) / (S + walk[i].w);
                    dt = 0;
                }
                else
                {
                    ans += (double)(walk[i].e - walk[i].b) / (R + walk[i].w);
                    dt -= (double)(walk[i].e - walk[i].b) / (R + walk[i].w);
                }
            }
            else
            {
                ans += (double)(walk[i].e - walk[i].b) / (S + walk[i].w);
            }
        }
        printf("Case #%d: %.9lf\n", cas++, ans);
    }
    return 0;
}
