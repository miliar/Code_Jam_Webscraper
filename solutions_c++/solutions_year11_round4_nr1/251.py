#include <iostream>
using namespace std;

struct rec
{
       int x,y,a;
};

bool cmp(rec a, rec b)
{
     return a.a<b.a;
}

rec f[2000];

int x,s,r,n;
double t;

int main()
{
    freopen("a3.in","r",stdin);
    freopen("a3.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++)
    {
        scanf("%d%d%d%lf%d",&x,&s,&r,&t,&n);
        int tot=x;
        double ans=0;
        for (int i=1;i<=n;i++)
        {
            scanf("%d%d%d",&f[i].x,&f[i].y,&f[i].a);
            tot-=f[i].y-f[i].x;
            ans+=double(f[i].y-f[i].x)/(s+f[i].a);
        }
        sort(f+1,f+n+1,cmp);
        if (double(tot)/r>=t)
        {
            ans+=t;
            ans+=double(tot-r*t)/s;
        }
        else
        {
            ans+=double(tot)/r;
            t-=double(tot)/r;
            for (int i=1;i<=n&&t>0;i++)
            {
                double zy=double(f[i].y-f[i].x)/(r+f[i].a);
                if (zy<=t)
                {
                    ans-=double(f[i].y-f[i].x)/(s+f[i].a);
                    ans+=zy;
                    t-=zy;
                }
                else
                {
                    ans-=double(f[i].y-f[i].x)/(s+f[i].a);
                    ans+=t;
                    ans+=double(f[i].y-f[i].x-t*(r+f[i].a))/(s+f[i].a);
                    t=0;
                }
            }    
        }
        printf("Case #%d: %.8lf\n",cas,ans);
    }
    return 0;                   
}
            
        
        
