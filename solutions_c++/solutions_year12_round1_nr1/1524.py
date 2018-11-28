#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;
typedef long long ll;

const int maxn=100000+123;
double dp[maxn];
double f[maxn];
double p[maxn];


int main ()
{
    freopen ("aa.in", "r", stdin);
    freopen ("a.out", "w", stdout);
    int cas; scanf("%d", &cas);
    int A, B;
    for (int I=1; I<=cas; ++I)
    {
        scanf("%d %d", &A, &B);
        double ans=B+2.0;//
        double pp=1.0;
        for (int i=0; i<A; ++i)
        {
            scanf("%lf", p+i);
            pp*=p[i];
        }
        double tmp=pp*(B-A+1)+(2*B-A+2)*(1-pp);
        //printf("%lf\n", tmp);
        ans=min(tmp, ans);
        for (int i=1; i<=A; ++i)
        {
            pp/=p[A-i];
            tmp=(B-A+2*i+1)*pp+(B-A+2*i+2+B)*(1-pp);
            //printf("%d %lf\n", i, tmp);
            ans=min(tmp, ans);
        }

        printf("Case #%d: %lf\n", I, ans);
    }
    return 0;
}
