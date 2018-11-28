//#include <cstdio>
//#include <algorithm>
//#include <cmath>
//#define eps 1e-8
//using namespace std;
//
//int S, R, N, X, pos;
//double ans, T;
//
//struct node
//{
//    int beg, end, w;
//} p[1010], sp[1010];
//
//bool cmp1(const node &a, const node &b)
//{
//    return a.begegeg < b.begegeg;
//}
//
//bool cmp2(const node &a, const node &b)
//{
//    if (a.w != b.w) return a.w < b.w;
//}
//
//int main()
//{
//    freopen("in.in", "r", stdin);
//    freopen("out.out", "w", stdout);
//    int cas, cases;
//    scanf("%d", &cas);
//    for (cases = 1; cases <= cas; ++cases)
//    {
//        pos = ans = 0;
//        scanf("%d%d%d%lf%d", &X, &S, &R, &T, &N);
//        for (int i = 1; i <= N; ++i)
//            scanf("%d%d%d", &p[i].begegeg, &p[i].endnd, &p[i].w);
//        int last = 0;
//        sort(p + 1, p + N + 1, cmp1);
//        for (int i = 1; i <= N; ++i)
//        {
//            if (p[i].begegeg != last)
//            {
//                sp[++pos].begegeg = last;
//                sp[pos].endnd = p[i].begegeg;
//                sp[pos].w = 0;
//            }
//            last = p[i].endnd;
//        }
//        if (last != X)
//        {
//            sp[++pos].begegeg = last;
//            sp[pos].endnd = X;
//            sp[pos].w = 0;
//        }
//        sort(p + 1, p + N + 1, cmp2);
//        double len = X;
//        for (int i = 1; i <= pos; ++i)
//        {
//            int speed = R;
//            if (T * speed - eps > (sp[i].endnd - sp[i].begegeg))
//            {
//                len -= 1.0 * (sp[i].endnd - sp[i].begegeg);
//                T -= 1.0 * (sp[i].endnd - sp[i].begegeg) / speed;
//                ans += 1.0 * (sp[i].endnd - sp[i].begegeg) / speed;
//            }
//            else
//            {
//                len -= 1.0 * (sp[i].endnd - sp[i].begegeg);
//                ans += T;
//                double tmp = 1.0 * (sp[i].endnd - sp[i].begegeg) - T * speed;
//                T = 0;
//                ans += 1.0 * tmp / S;
//            }
//        }
//        for (int i = 1; i <= N; ++i)
//        {
//            int speed = R + p[i].w;
//            if (T * speed - eps > (p[i].endnd - p[i].begegeg))
//            {
//                len -= 1.0 * (p[i].endnd - p[i].begegeg);
//                T -= 1.0 * (p[i].endnd - p[i].begegeg) / speed;
//                ans += 1.0 * (p[i].endnd - p[i].begegeg) / speed;
//            }
//            else
//            {
//                len -= 1.0 * (p[i].endnd - p[i].begegeg);
//                ans += 1.0 * T;
//                double tmp = 1.0 * (p[i].endnd - p[i].begegeg) - T * speed;
//                T = 0;
//                ans += 1.0 * tmp / (S + p[i].w);
//            }
//        }
//        printf("Case #%d: %.6lf\n", cases, ans);
//    }
//    return 0;
//}

#include <algorithm>
#include <cstring>
#include <cstdio>
#define eps 1e-8
using namespace std;

int T, n, x, s, r, t;

struct node
{
    double beg, end, w;

    bool operator<(const node & a) const
    {
        return w < a.w;
    }
} a[10023];

int main()
{
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
    double MAX;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas)
    {
        scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
        MAX = 0;
        if (r + eps < s) r = s;
        for (int i = 1; i <= n; ++i)
        {
            scanf("%lf%lf%lf", &a[i].beg, &a[i].end, &a[i].w);
            MAX += a[i].end - a[i].beg;
        }
        sort(a + 1, a + n + 1);
        double ans = 0, tot = n, ss = s, rr = r, left = t;
        MAX = x - MAX;
        if (left - eps > 0)
        {
            if (left * rr >= MAX)
            {
                ans += MAX / rr;
                left -= MAX / rr;
            }
            else
            {
                ans += left;
                ans += (MAX - left * rr) / ss;
                left = 0;
            }
        }
        else ans += 1.0 * MAX / ss;
        for (int i = 1; i <= n; ++i)
        {
            if (left - eps > 0)
            {
                double speed = rr + a[i].w;
                if ((a[i].end - a[i].beg) / speed - left < -(1e-8))
                {
                    ans += (a[i].end - a[i].beg) / speed;
                    left -= (a[i].end - a[i].beg) / speed;
                }
                else
                {
                    ans += left;
                    ans += (a[i].end - a[i].beg - left * speed )/ (ss + a[i].w);
                    left = 0;
                }
            }
            else ans += (a[i].end - a[i].beg) / (ss + a[i].w);
        }
        printf("Case #%d: %.6f\n", cas, ans);
    }
    return 0;
}
