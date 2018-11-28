/*
 * Author: ahxgw
 * Created Time:  2011-6-4 22:11:18
 * Description: 
 */
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define out(v) fprintf(stderr, "%s: %I64d\n", #v, (long long)(v))
#define SZ(v) ((int)(v).size())
#define p_b push_back
#define m_p make_pair
const int maxint = -1u>>1;
template<class T> void toMax(T &a, T b) {if (b > a) a = b;}
template<class T> void toMin(T &a, T b) {if (b < a) a = b;}

const int MaxN = 1010;
const double eps = 1e-8;

int T, X, S, R, t, N;
struct Ja
{
    int b, e, w;
}ja[MaxN];

bool cmp(Ja x, Ja y)
{
    return x.w < y.w;
}

int main()
{
    freopen("A.out", "w", stdout);
    scanf("%d", &T);
    for (int _ = 1; _ <= T; _++)
    {
        scanf("%d%d%d%d%d", &X, &S, &R, &t, &N);
        double no = X;
        for (int i = 0; i < N; i++)
        {
            scanf("%d%d%d", &ja[i].b, &ja[i].e, &ja[i].w);
            no -= (ja[i].e - ja[i].b);
        }
        sort(ja, ja + N, cmp);
        double left = t;
        double time = (double)no / R;
        double ans = 0;
        if (time < left)
        {
            left -= time;
            ans += time;
        }
        else
        {
            no -= R * left;
            left = 0;
            ans += t;
            ans += no / S;
        }
        for (int i = 0; i < N; i++)
        {
            double len = ja[i].e - ja[i].b;
            if (fabs(left) > eps)
            {
                time = (double)(ja[i].e - ja[i].b) / (R + ja[i].w);
                if (time < left)
                {
                    left -= time;
                    ans += time;
                }
                else
                {
                    len -= (R + ja[i].w) * left;
                    ans += left;
                    left = 0;
                    ans += len / (S + ja[i].w);
                }
            }
            else
            {
                ans += len / (S + ja[i].w);
            }
        }
        printf("Case #%d: %f\n", _, ans);
    }

    return 0;
}
