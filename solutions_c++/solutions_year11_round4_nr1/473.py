#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
typedef struct
{
    int b,e,w;
} node;
node p[3000];
int s,r;
bool cmp(node x,node y)
{
    return x.b<y.b;
}
bool cmp2(node x,node y)
{
    double num1= 1.0/(x.w+s)-1.0/(x.w+r);
    double num2= 1.0/(y.w+s)-1.0/(y.w+r);
    return num1>num2;

}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int ii=1;ii<=T;ii++)
    {
        int x;
        double t;
        int n;
        scanf("%d%d%d%lf%d",&x,&s,&r,&t,&n);
        for (int i=0;i<n;i++)
            scanf("%d%d%d",&p[i].b,&p[i].e,&p[i].w);
        sort(p,p+n,cmp);
        int start=0;
        int cnt=n;
        for (int i=0;i<n;i++)
        {
            p[cnt].b=start;
            p[cnt].e=p[i].b;
            p[cnt].w=0;
            start=p[i].e;
            cnt++;
        }
        p[cnt].b=start;
        p[cnt].e=x;
        p[cnt].w=0;
        cnt++;
        sort(p,p+cnt,cmp2);
        double total=0;
        for (int i=0;i<cnt;i++)
        {
            double timeneed=((p[i].e-p[i].b)*1.0)/(p[i].w+r);
            if (t>timeneed)
            {
                t-=timeneed;
                total+=((p[i].e-p[i].b)*1.0)/(p[i].w+r);
            }
            else
            {
                total+=t;
                total+=((p[i].e-p[i].b-(p[i].w+r)*t)*1.0)/(p[i].w+s);
                t=0;
            }
        }
        printf("Case #%d: %.10f\n",ii,total);
    }
    return 0;
}
