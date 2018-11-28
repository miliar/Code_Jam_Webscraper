#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
int x[3];
int y[3];
int r[3];
double ttt(int i)
{
    int j=(i+1)%3;
    int k=(i+2)%3;
    double ans = r[i];
    double foo = (hypot((double)(x[j]-x[k]),(double)(y[j]-y[k])) + r[j] + r[k])/2;
//    printf("%lf %lf\n",ans,foo);
    return max(foo,ans);
}
double tst()
{
    int c;
    scanf("%d",&c);
    for(int i=0;i<c;i++)
        scanf("%d%d%d",&x[i],&y[i],&r[i]);
    while(c<3)
    {
        x[c]=x[c-1];
        y[c]=y[c-1];
        r[c]=r[c-1];
        c++;
    }
    return min(ttt(0),min(ttt(1),ttt(2)));

}
int main()
{
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        printf("Case #%d: %.6lf\n",i,tst());
    }

}
