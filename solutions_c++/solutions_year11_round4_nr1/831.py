#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#define max(a,b)    a>b?a:b;
#define min(a,b)    a<b?a:b;
#define INF 0x3fffffff
#define eps 1e-6
struct node
{
    long long b,e,v;
};
struct node con[1005];
int cmp(const void *a,const void *b)
{
    struct node *c=(node *)a;
    struct node *d=(node *)b;
    if(c->v!=d->v)   return c->v-d->v;
    else             return c->b-d->b;
}
long long n;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    long long t,s,r,x;
    double ans,time,base;
    scanf("%d",&t);
    for(long long cas=1;cas<=t;cas++)
    {
        scanf("%I64d%I64d%I64d%lf%I64d",&x,&s,&r,&time,&n);
        long long left=x;
        ans=0;
        for(long long i=1;i<=n;i++)
        {
            scanf("%I64d%I64d%I64d",&con[i].b,&con[i].e,&con[i].v);
            left=left-(con[i].e-con[i].b);
            ans=ans+(con[i].e-con[i].b)*1.0/(con[i].v+s);
        }
        qsort(&con[1],n,sizeof(con[0]),cmp);
        if(left>=r*time)
        {
            ans=ans+time+(left-r*time)*1.0/s;
        }
        else if(left<r*time)
        {
            ans+=left*1.0/r;
            time=time-left*1.0/r;
            for(long long i=1;i<=n;i++)
            {
                if(time<=eps&&time>=-eps) break;
                ans=ans-(con[i].e-con[i].b)*1.0/(con[i].v+s);
                if(time*(con[i].v+r)-(con[i].e-con[i].b)*1.0>eps)
                {
                    ans=ans+(con[i].e-con[i].b)*1.0/(con[i].v+r);
                    time=time-(con[i].e-con[i].b)*1.0/(con[i].v+r);
                }
                else
                {
                    ans=ans+time+(con[i].e-con[i].b-(con[i].v+r)*time)*1.0/(con[i].v+s);
                    time=0;
                }
            }
        }
        printf("Case #%I64d: %lf\n",cas,ans);
    }
    return 0;
}
