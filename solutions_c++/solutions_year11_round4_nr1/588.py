#include <cstdio>
#include <algorithm>
#include <utility>
using namespace std;

typedef pair<int, int> P;

double t;
int X, S, R, N;
bool cp(const P& a, const P& b)
{
    return 1.0 / (a.second + S) - 1.0 / (a.second + R) > 1.0 / (b.second + S) - 1.0 / (b.second +R);
}

double f(int len, double& t, int S, int R, int W)
{
    double m = len / (double)(R + W);
    if(m <= t)
    {
        t -= m;
  //      printf("!%lf\n", m);
        return m;
    }
    else
    {
        double aa = t + (len - t * (R + W)) / (double)(S + W);
        t = 0;
//        printf("?%lf\n", aa);
        return aa;
    }
}

P ps[1024];

int main()
{
    int T;
    scanf("%d", &T);

    for(int testnum = 1; testnum  <= T; testnum++)
    {
        double ans = 0.0;
        double total = 0;
        scanf("%d%d%d%lf%d", &X, &S, &R, &t, &N);

        int last = 0;
        for(int i = 0; i < N; i++)
        {
            int s, e, w;
            scanf("%d%d%d", &s, &e, &w);
        
            total += s - last;
            ps[i] = P(e - s, w);
  //          ans += f(s - last, t, S, R, 0);
    //        ans += f(e - s, t, S, R, w);
            last = e;
        }
        total += X - last;

//printf("%lf!\n", total);
//        ans += f(X - last, t, S, R, 0);
        ps[N] = P(total, 0);

        sort(ps, ps + N + 1, cp);
        for(int i = 0; i <= N; i++)
            ans += f(ps[i].first, t, S, R, ps[i].second);
        printf("Case #%d: %.10lf\n", testnum, ans);
    }
    return 0;
}
