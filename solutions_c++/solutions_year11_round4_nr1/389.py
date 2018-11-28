#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#define MAXN 1000
using namespace std;

struct Walkway
{
    int b;
    int e;
    int w;
};

Walkway way[MAXN+1];
int x,s,r,t,n;
double dt;

bool operator<(const Walkway &a,const Walkway &b)
{
    if(a.w<b.w)
    {
        return true;
    }
    else
    {
        return false;
    }
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j,k,p,q,sum;
    double ans;
    scanf("%d",&q);
    for(p=0;p<q;p++)
    {
        scanf("%d %d %d %d %d",&x,&s,&r,&t,&n);
        sum=0;
        for(i=0;i<n;i++)
        {
            scanf("%d %d %d",&way[i].b,&way[i].e,&way[i].w);
        }
        sum=sum+way[0].b;
        for(i=0;i+1<n;i++)
        {
            sum=sum+way[i+1].b-way[i].e;
        }
        sum=sum+x-way[n-1].e;
        if(sum>=r*t)
        {
            ans=t+1.0*(sum-r*t)/s;
            dt=0.0;
        }
        else
        {
            ans=1.0*sum/r;
            dt=t-1.0*sum/r;
        }
        sort(way,way+n);
        for(i=0;i<n;i++)
        {
            if((r+way[i].w)*dt>=way[i].e-way[i].b)
            {
                dt=dt-1.0*(way[i].e-way[i].b)/(r+way[i].w);
                ans=ans+1.0*(way[i].e-way[i].b)/(r+way[i].w);
            }
            else if(dt>0.000001)
            {
                ans=ans+dt+1.0*(way[i].e-way[i].b-(r+way[i].w)*dt)/(s+way[i].w);
                dt=0.0;
            }
            else
            {
                ans=ans+1.0*(way[i].e-way[i].b)/(s+way[i].w);
            }
        }
        printf("Case #%d: %.6f\n",p+1,ans);
    }
    return 0;
}
