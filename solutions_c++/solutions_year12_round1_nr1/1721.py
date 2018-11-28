#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
using namespace std;
#define M 100007
int a,b;
double p[M];
double dp[M];
int main()
{
    int Ta,Case;
    freopen("D:\\A.in","r",stdin);
    freopen("D:\\A.out","w",stdout);
    scanf("%d",&Ta);
    for (Case = 1;Case<=Ta; Case ++ )
    {
        memset(p,0,sizeof(p));
        memset(dp,0,sizeof(dp));
        scanf("%d%d",&a,&b);
        int i,j;
        for (i=1;i<=a;i++)
            scanf("%lf",&p[i]);
        double sum1=1,sum2=1;
        for (i=1;i<=a-1;i++)
            sum1*=p[i];
        sum2=sum1*p[a];
        double ans;
        ans = sum2*(b-a+1) + (1-sum2)*(b-a+1+b+1);
        ans = min(ans, sum1*(b-a+3) + (1-sum1)*(b-a+3+b+1));
        ans = min(ans, b+2.0);
        printf("Case #%d: %.6lf\n",Case,ans);
    }
    return 0;
}
