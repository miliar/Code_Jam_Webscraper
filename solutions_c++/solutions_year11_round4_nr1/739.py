#include <iostream>
#include<cstdio>
#include<algorithm>

using namespace std;

struct In
{
    int e,b,w;
}ss[11000000];
bool cmp(In a,In b)
{
    return a.w<b.w;
}
int main()
{
    int i,j,k,tt,l,x,s,r,t,n;
    double len,ans,dt;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&tt);
    for(l=1;l<=tt;l++)
    {
        scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
        ans=0.0;
        for(i=1;i<=n;i++)
        {
            scanf("%d%d%d",&ss[i].b,&ss[i].e,&ss[i].w);
            x-=(ss[i].e-ss[i].b);
        }
        dt=t*1.0;
        ss[0].b=0;
        ss[0].e=x;
        ss[0].w=0;
        ans=0.0;
        sort(ss,ss+n+1,cmp);
        for(i=0;i<=n;i++)
        {
            if(dt>0)
            {
                len=(ss[i].e-ss[i].b)*1.0/(ss[i].w+r);
                if(len<=dt)
                {
                    ans+=len;
                    dt-=len;
                }
                else
                {
                    len=ss[i].e-ss[i].b-(ss[i].w+r)*dt;
                    ans+=dt;
                    dt=-1.0;
                    ans+=len/(ss[i].w+s);
                }
            }
            else
            {
                ans+=(ss[i].e-ss[i].b)*1.0/(ss[i].w+s);
            }
        }
        printf("Case #%d: %.10lf\n",l,ans);

    }
    return 0;
}
