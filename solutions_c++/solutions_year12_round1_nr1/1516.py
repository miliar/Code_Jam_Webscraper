#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
#define maxA 100000
#define maxB 100000
double p[maxA];
double l[maxA];
double ans[maxA + 10];
int T;
int main()
{
    int a,b;
    int i;
    double sum;
    double kk;
    int cs;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    while(scanf("%d",&T)!=EOF)
    {
        cs = 1;
        while(T--)
        {
            sum = 1.0;
            scanf("%d%d",&a,&b);
            for(i = 0; i < a; i++)
            {
                scanf("%lf",&l[i]);
            }
            for(i = 0; i < a; i++)
            {
                if( i == 0)
                    p[i] = 1 - l[i];
                else
                    p[i] =  sum * (1 - l[i]);
                sum = sum * l[i];
            }
            ans[0] = sum * (b - a + 1) + (1 - sum) * ( 2 *b - a + 2);
            double tmp;
            for(i = 1; i <= a; i++)
            {
                tmp = sum + p[a - i];
                ans[i] = tmp * (b - a + 1 + i * 2) + (1 - tmp) * (b - a + 1 + i * 2 + b + 1);
            }
            sort(ans,ans + a + 1);
            printf("Case #%d: ",cs++);
            kk = b + 2;
            if(kk < ans[0])
                printf("%.6lf\n",kk);
            else
                printf("%.6lf\n",ans[0]);
        }
    }
    return 0;
}
