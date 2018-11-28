#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstdlib>
#include<ctime>
#include<vector>
#include<map>
#include<set>
using namespace std;

struct Node
{
    int Len, v;
};

int B[1024], E[1024], W[1024];
Node s[2048];

int cmp(Node s1, Node s2)
{
    return s1.v < s2.v;
}

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int T, tt, X, S, R, N, n, i;
    double t, ans, t2;
    scanf("%d", &T);
    for(tt = 1; tt <= T; tt++)
    {
        scanf("%d%d%d%lf%d", &X, &S, &R, &t, &N);
        for(i = 0; i < N; i++) scanf("%d%d%d", &B[i], &E[i], &W[i]);
        n = 1;
        s[0].Len = B[0];
        s[0].v = S;
        for(i = 0; i < N; i++)
        {
            if(i > 0)
            {
                s[n].Len = B[i] - E[i-1];
                s[n].v = S;
                n++;
            }
            s[n].Len = E[i] - B[i];
            s[n].v = S + W[i];
            n++;
        }
        s[n].Len = X - E[N - 1];
        s[n].v = S;
        n++;
        sort(s, s + n, cmp);
        R -= S;
        ans  = 0;
        for(i = 0; i < n; i++)
        {
            t2 = double(s[i].Len) / (s[i].v + R);
            if(t2 < t)
            {
                ans += t2;
                t -= t2;
            }
            else
            {
                t2 = (s[i].Len - (s[i].v + R) * t) / s[i].v;
                ans += t + t2;
                t = 0;
            }
        }
        printf("Case #%d: %.8lf\n", tt, ans);
    }

    return 0;
}
