
#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;

int n;
struct ad
{
    double x,y,v,len;
};

bool cmp(ad a,ad b)
{
    return a.v<b.v;
}

ad a[1010];
int main()
{
    freopen("a.in","r",stdin);
    freopen("1.out","w",stdout);
    int T,i,j;
    scanf("%d",&T);
    int cs=0;
    double len,s,r,t;
    while(T--)
    {
        scanf("%lf%lf%lf%lf%d",&len,&s,&r,&t,&n);
        double tot=len;
        for(i=0;i<n;i++)
        {
        scanf("%lf%lf%lf",&a[i].x,&a[i].y,&a[i].v);
        a[i].len=a[i].y-a[i].x;
        tot-=a[i].len;
        }
        sort(a,a+n,cmp);
        printf("Case #%d: ",++cs);
        double ans=0;
        if(t*r<tot)
        {
            ans+=t;
            ans+=(tot-t*r)/s;
            t=0;
        }
        else
        {
            ans+=tot/r;
            t-=ans;
        }
        i=0;
        double lf;
        while(t>0&&i<n)
        {
          if(a[i].len/(r+a[i].v)<t)
          {
              ans+=a[i].len/(r+a[i].v);
              t-=a[i].len/(r+a[i].v);
              i++;
          }
          else
          {
              ans+=t;
             lf=a[i].len-t*(a[i].v+r);
             ans+=lf/(s+a[i].v);
             i++;
             break;
          }
        }

            for(;i<n;i++) ans+=a[i].len/(s+a[i].v);
            printf("%f\n",ans);
    }
    return 0;
}




