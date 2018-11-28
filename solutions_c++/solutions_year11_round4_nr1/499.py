#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
const double eps=1e-8;
struct node{
    int x,y,w;
} e[3000];

bool cmp(const node &u,const node &v)
{
    return u.w<v.w;
}

int main()
{
    int cas;
    int x,s,r,t,n;

    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&cas);
    for(int ll=1;ll<=cas;ll++)
    {
        scanf("%d %d %d %d %d",&x,&s,&r,&t,&n);
        for(int i=0;i<n;i++)
        {
            scanf("%d %d %d",&e[i].x,&e[i].y,&e[i].w);
            e[i].w+=s;
        }
        int nn=n;
        if (e[0].x>0)
        {
            e[nn].x=0;e[nn].y=e[0].x;e[nn].w=s;
            nn++;
        }
        for(int i=0;i<n-1;i++)
        {
            if (e[i].y!=e[i+1].x)
            {
                e[nn].x=e[i].y;
                e[nn].y=e[i+1].x;
                e[nn].w=s;
                nn++;
            }
        }
        if (e[n-1].y!=x)
        {
            e[nn].x=e[n-1].y;e[nn].y=x;e[nn].w=s;
            nn++;
        }
        sort(e,e+nn,cmp);
        double use=t;
        double ans=0;
        r-=s;
        for(int i=0;i<nn;i++)
        {
            if (use>eps)
            {
                double len=use*(r+e[i].w);
                if (len>e[i].y-e[i].x)
                {
                    double now=(e[i].y-e[i].x)*1.0/(r+e[i].w);
                    ans+=now;
                    use-=now;
                } else
                {
                    ans+=use;
                    len=e[i].y-e[i].x-use*(r+e[i].w);
                    use=0;
                    ans+=len/e[i].w;
                }
            } else ans+=(e[i].y-e[i].x)*1.0/e[i].w;
            //printf("%.2f ",ans);
        }
        printf("Case #%d: %.8f\n",ll,ans);
    }
    return 0;
}





